#!/usr/bin/ipython

# this file stores functions that are needed for the nltk lessons.
# if somebody is having trouble getting something to work, they can
# often solve it by importing something from here.

def searchtree(tree, query):
    "Searches a tree with Tregex and returns matching terminals"
        # check if we are in ipython
    import os
    try:
        get_ipython().getoutput()
    except TypeError:
        have_ipython = True
    except NameError:
        import subprocess
        have_ipython = False
    fo = open('tree.tmp',"w")
    fo.write(tree + '\n')
    fo.close()
    if have_ipython:
        tregex_command = 'tregex.sh -o -t \'%s\' tree.tmp 2>/dev/null | grep -vP \'^\s*$\'' % query
        result = get_ipython().getoutput(tregex_command)
    else:
        tregex_command = ["tregex.sh", "-o", "-t", '%s' % query, "tree.tmp"]
        FNULL = open(os.devnull, 'w')
        result = subprocess.check_output(tregex_command, stderr=FNULL)
        result = os.linesep.join([s for s in result.splitlines() if s]).split('\n')
    tregex_command = 'sh ./tregex.sh -o -t \'' + query + '\' tmp.tree 2>/dev/null | grep -vP \'^\s*$\''
    os.remove("tmp.tree")
    return result

def quicktree(sentence):
    """Parse a sentence and return a visual representation in IPython"""
    import os
    from nltk import Tree
    from nltk.draw.util import CanvasFrame
    from nltk.draw import TreeWidget
    from stat_parser import Parser
    try:
        from IPython.display import display
        from IPython.display import Image
    except:
        pass
    try:
        get_ipython().getoutput()
    except TypeError:
        have_ipython = True
    except NameError:
        import subprocess
        have_ipython = False
    parser = Parser()
    parsed = parser.parse(sentence)
    cf = CanvasFrame()
    tc = TreeWidget(cf.canvas(),parsed)
    cf.add_widget(tc,10,10) # (10,10) offsets
    cf.print_to_file('tree.ps')
    cf.destroy()
    if have_ipython:
        tregex_command = 'convert tree.ps tree.png'
        result = get_ipython().getoutput(tregex_command)
    else:
        tregex_command = ["convert", "tree.ps", "tree.png"]
        result = subprocess.check_output(tregex_command)    
    os.remove("tree.ps")
    return Image(filename='tree.png')
    os.remove("tree.png")

def parse_metadata(text):
    "Parses Fraser Corpus metadata"
    # should we make compatible with files, whole texts?
    metadata = {}
    for line in text.split('\r\n'):
        if not line:
            continue
        if line[0] == '<':
            continue
        element = line.split(':', 1)
        metadata[element[0]] = element[-1].strip(' ')
    return metadata
    
def structure_corpus(oldpath, newpath):
    """structure our corpus by year"""
    # oldpath = corpora/UMA_Fraser_Radio_Talks
    # newpath = 'corpora/fraser-annual'
    import re
    #if not os.path.exists(newpath):
        #os.makedirs(newpath)
    files = os.listdir(oldpath)
    # define a regex to match year portion of date
    yearfinder = re.compile('[0-9]{4}')
    for filename in files:
        # split file contents at end of metadata
        data = open(os.path.join(oldpath, filename)).read().split("<!--end metadata-->")
        # get date from data[0]
        # use our metadata parser to get metadata
        metadata = parse_metadata(data[0])
        #look up date field of dict entry
        date = metadata.get('Date')
        # search date for year
        yearmatch = re.search(yearfinder, str(date))
        #get the year as a string
        year = str(yearmatch.group())
        # make a directory with the year name
        if not os.path.exists(os.path.join(newpath, year)):
            os.makedirs(os.path.join(newpath, year))
        # make a new file with the same name as the old one in the new dir
        fo = open(os.path.join(newpath, year, filename),"w")
        # write the content portion, without metadata
        fo.write(data[1])
        fo.close()
    
#!/usr/bin/ipython

#   Interrogating parsed corpora and plotting the results: plot()
#   For use in ResBaz NLTK stream
#   Author: Daniel McDonald


def plot(title, results, sort_by = 'total', fract_of = False, y_label = False, 
    num_to_plot = 7, significance_level = 0.05,
    multiplier = 100, yearspan = False, proj63 = 5,
    justyears = False, csvmake = False, x_label = False, legend_p = False,
    legend_totals = False, log = False, figsize = 11, save = False, 
    only_below_p = False, skip63 = False, projection = True):
    """
    Visualise interrogator() results, optionally generating a csv as well.

    Parameters
    ----------

    title : string
        Chart title
    results : list
        interrogator() results or totals (deaults to results)
    sort_by : string
        'total': sort by most frequent
        'increase': calculate linear regression, sort by steepest up slope
        'decrease': calculate linear regression, sort by steepest down slope 
        'static': calculate linear regression, sort by least slope
    fract_of : list
        measure results as a fraction (default: as a percentage) of this list.
        usually, use interrogator() totals
    multiplier : int
        mutliply results list before dividing by fract_of list
        Default is 100 (for percentage), can use 1 for ratios
    y_label : string
        text for y-axis label (default is 'Absolute frequency'/'Percentage') 
    X_label : string
        text for x-axis label (default is 'Group'/'Year')
    num_to_plot : int
        How many top entries to show
    significance_level : float
        If using sort_by, set the p threshold (default 0.05)
    only_below_p : Boolean
        Do not plot any results above p value
    yearspan : list with two ints
        Get only results between the specified ints
    justyears : list of ints
        Get only results from the listed subcorpora
    csvmake : True/False/string
        Generate a CSV of plotted and all results with string as filename
        If True, 'title' string is used
    legend_totals : Boolean
        Show total frequency of each result, or overall percentage if fract_of
    legend_p : Boolean
        Show p-value for slope when using sort_by
    log : False/'x'/'y'/'x, y'
        Use logarithmic axes
    figsize = int
        Size of image
    save = True/False/string
        Generate save image with string as filename
        If True, 'title' string is used for name

    NYT-only parameters
    -----
    skip63 : boolean
        Skip 1963 results (for NYT investigation)
    projection : boolean
        Project 1963/2014 results (for NYT investigation)
    proj63 : int
        The amount to project 1963 results by

    Example
    -----
    from corpkit import interrogator, plotter
    corpus = 'path/to/corpus'
    adjectives = interrogator(corpus, 'words', r'/JJ.?/ < __')
    plotter('Most common adjectives', adjectives.results, fract_of = adjectives.totals,
            csvmake = True, legend_totals = True)

    """

    import os
    import warnings
    import copy
    from time import localtime, strftime
    
    import matplotlib.pyplot as plt
    from matplotlib import rc
    from matplotlib.ticker import MaxNLocator, ScalarFormatter
    import pylab
    from pylab import rcParams
    try:
        get_ipython().getoutput()
    except TypeError:
        have_ipython = True
    except NameError:
        import subprocess
        have_ipython = False
    try:
        from IPython.display import display, clear_output
    except ImportError:
        pass
    from corpkit.query import check_dit, check_pytex, check_tex
    from corpkit.edit import resorter, mather

    # setup:

    # size:
    rcParams['figure.figsize'] = figsize, figsize/2
    
    #font
    rcParams.update({'font.size': (figsize / 2) + 7}) # half your size plus seven
    
    # check what we're doing here.
    have_python_tex = check_pytex()
    on_cloud = check_dit()
    have_tex = check_tex(have_ipython = have_ipython)


    def skipper(interrogator_list):
        """Takes a list and returns a version without 1963"""
        skipped = []
        skipped.append(interrogator_list[0]) # append word
        for item in interrogator_list[1:]:
            if type(item) != unicode and type(item) != str and item[0] != 1963:
                skipped.append(item)
        return skipped

    def yearskipper(interrogator_list, justyears):
        """Takes a list and returns only results from the years listed in justyears"""
        skipped = []
        skipped.append(interrogator_list[0]) # append word
        for item in interrogator_list[1:]:
            if type(item) != unicode and type(item) != str:
                for year in justyears:
                    if item[0] == year:
                        skipped.append(item)
        return skipped

    def yearspanner(interrogator_list, yearspan):
        """Takes a list and returns results from between the first and last year in yearspan"""
        
        skipped = [interrogator_list[0]] # append word
        for item in interrogator_list[1:]:
            if type(item) != unicode and type(item) != str:
                if item[0] >= yearspan[0]:
                    if item [0] <= yearspan[-1] + 1:
                        skipped.append(item)
        return skipped

    def projector(interrogator_list):
        """Takes a list and returns a version with projections"""
        projected = []
        projected.append(interrogator_list[0]) # append word
        for item in interrogator_list[1:]:
            if type(item) != str and type(item) != str and item[0] == 1963:
                newtotal = item[1] * proj63
                datum = [item[0], newtotal]
                projected.append(datum)
            elif type(item) != str and type(item) != str and item[0] == 2014:
                newtotal = item[1] * 1.37
                datum = [item[0], newtotal]
                projected.append(datum)
            else:
                projected.append(item)
        return projected

    def csvmaker(csvdata, csvalldata, csvmake):
        """Takes whatever ended up getting plotted and puts it into a csv file"""
        # now that I know about Pandas, I could probably make this much less painful.
        csv = []
        yearlist = []
        # get list of years
        for entry in csvdata[0]:
            if type(entry) == list:
                yearlist.append(str(entry[0]))
        # make first line
        csv.append(title)
        # make the second line
        years = ',' + ','.join(yearlist)
        csv.append(years)
        # for each word
        for entry in csvdata:
            csvline = []
            csvcounts = []
            csvline.append(entry[0]) # append word
            for part in entry[1:]:
                csvcounts.append(str(part[1])) # append just the count
            counts = ','.join(csvcounts)
            csvline.append(counts)
            line = ','.join(csvline)
            csv.append(line)
        csv = '\n'.join(csv)
        # now do all data
        csvall = []
        yearlist = []
        # get list of years
        for entry in csvalldata[0]:
            if type(entry) == list:
                yearlist.append(str(entry[0]))
        # make first line
        csvall.append(title)
        # make the second line
        years = ',' + ','.join(yearlist)
        csvall.append(years)
        # for each word
        for entry in csvalldata:
            csvallline = []
            csvallcounts = []
            csvallline.append(entry[0]) # append word
            for part in entry[1:]:
                csvallcounts.append(str(part[1])) # append just the count
            counts = ','.join(csvallcounts)
            csvallline.append(counts)
            line = ','.join(csvallline)
            csvall.append(line)
        csvall = '\n'.join(csvall)
        # write the csvall file?
        if os.path.isfile(csvmake):
            raise ValueError("CSV error: %s already exists in current directory. \
                    Move it, delete it, or change the name of the new .csv file." % csvmake)
        try:
            fo=open(csvmake,"w")
        except IOError:
            print "Error writing CSV file."
        fo.write('Plotted results:\n'.encode("UTF-8"))
        fo.write(csv.encode("UTF-8"))
        fo.write('\n\nAll results:\n'.encode("UTF-8"))
        fo.write(csvall.encode("UTF-8"))
        fo.close()
        time = strftime("%H:%M:%S", localtime())
        print time + ": " + csvmake + " written to currect directory."

    ##################################################################

    # check for tex and use it if it's there
    if have_tex:
        rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
        rc('text', usetex=True)

    #image directory
    if have_python_tex:
        imagefolder = '../images'
    else:
        imagefolder = 'images'

    # Use .results branch if branch is unspecified
    if isinstance(results, tuple) is True:
        warnings.warn('\nNo branch of results selected. Using .results ... ')
        results = results.results
    if only_below_p:
        if sort_by == 'static':
            warnings.warn('\nStatic trajectories will confirm the null hypothesis, so it might ' +
                              'not be helpful to use both the static and only_below_p options together.')
        if sort_by == 'total' or sort_by == 'name':
            warnings.warn("\nP value has not been calculated. No entries will be excluded") 
    
    # cut short to save time if later results aren't useful
    if csvmake or sort_by != 'total':
        cutoff = len(results)
    else:
        cutoff = num_to_plot
    
    # if plotting one entry/a totals list, wrap it in another list
    if type(results[0]) == unicode or type(results[0]) == str:
        legend = False
        alldata = [copy.deepcopy(results)][:cutoff]
        num_to_plot = 1
    else:
        legend = True
        alldata = copy.deepcopy(results[:cutoff])

    # determine if no subcorpora and thus barchart
    if len(results[0]) == 3 or len(results[0]) == 4:
        barchart = True
    else:
        barchart = False

    # if no x_label, guess 'year' or 'group'
    if x_label:
        x_lab = x_label
    else:
        if not barchart:
            check_x_axis = alldata[0] # get first entry
            check_x_axis = check_x_axis[1] # get second entry of first entry (year, count)
            if 1500 < check_x_axis[0] < 2050:
                x_lab = 'Year'
            else:
                x_lab = 'Group'
        else:
            x_lab = False


    # select totals if no branch selected
    if fract_of:
        if isinstance(fract_of, tuple) is True:
            warnings.warn('\nNo branch of fract_of selected. Using .totals ... ')
            fract_of = fract_of.totals
        # copy this, to be safe!
        totals = copy.deepcopy(fract_of)

        #use mather to make percentage results
        fractdata = []
        for entry in alldata:
            fractdata.append(mather(entry, '%', totals, multiplier = multiplier))
        alldata = copy.deepcopy(fractdata)
    
    # sort_by with resorter
    if sort_by != 'total':
        do_stats = True
        alldata = resorter(alldata, sort_by = sort_by, 
                           keep_stats = True, only_below_p = only_below_p, 
                           significance_level = significance_level, skip63 = skip63)
    else:
        do_stats = False
    csvdata = []
    csvalldata = []
    final = []
    colours = ["#1f78b4", "#33a02c", "#e31a1c", "#ff7f00", "#6a3d9a", "#a6cee3", "#b2df8a", "#fb9a99", "#fdbf6f", "#cab2d6"]
    c = 0
    
    if num_to_plot > len(alldata):
        warnings.warn("There are not %d entries to show.\nPlotting all %d results..." % (num_to_plot, len(alldata)))
    
    if not csvmake:
        cutoff = num_to_plot
    
    if not barchart:
        for index, entry in enumerate(alldata[:cutoff]):
            # run called processes
            if skip63:
                entry = skipper(entry)
            if yearspan:
                entry = yearspanner(entry, yearspan)
            if justyears:
                entry = yearskipper(entry, justyears)
            if projection:
                if not fract_of:
                    entry = projector(entry)
            # get word
            word = entry[0]
            if do_stats:
                pval = entry[-1][3]
                p_short = "%.4f" % pval
                p_string = ' (p=%s)' % p_short   
                # remove stats, we're done with them.
                entry.pop() 
            # get totals ... horrible code
            total = 0
            if fract_of:
                if entry[-1][0] == 'Total':
                    num = entry[-1][1]
                    total = "%.2f" % num
                    #total = str(float(entry[-1][1]))[:5]
                totalstring = ' (' + str(total) + '\%)'     
            else:
                if entry[-1][0] == 'Total':
                    total = entry[-1][1]
                totalstring = ' (n=%d)' % total
    
            entry.pop() # get rid of total. good or bad?
            csvalldata.append(entry) 
    
            if index < num_to_plot:
                csvdata.append(entry)
                toplot = []
                xvalsbelow = []
                yvalsbelow = []
                xvalsabove = []
                yvalsabove = []
                d = 1 # first tuple, maybe not very stable
                tups = len(entry) - 2 # all tuples minus 2 (to skip totals tuple)
                for _ in range(tups):
                    firstpart = entry[d] # first tuple
                    firstyear = firstpart[0]
                    nextpart = entry[d + 1]
                    nextyear = nextpart[0]
                    if nextyear - firstyear > 50: # change to 1 for nyt
                        xvalsbelow.append(firstpart[0])
                        yvalsbelow.append(firstpart[1])
                        xvalsbelow.append(nextpart[0])
                        yvalsbelow.append(nextpart[1])
                    else:
                        xvalsabove.append(firstpart[0])
                        yvalsabove.append(firstpart[1])
                        xvalsabove.append(nextpart[0])
                        yvalsabove.append(nextpart[1])
                    d += 1
                if csvmake: # append exactly what was plotted...
                    csvdata.append(entry)
        
                # do actual plotting
                plt.plot(xvalsbelow, yvalsbelow, '--', color=colours[c])
                plt.plot(xvalsabove, yvalsabove, '-', label=word, color=colours[c])
                plt.plot(xvalsabove, yvalsabove, '.', color=colours[c]) # delete for nyt

                if c == 8:
                    c = 0 # unpythonic
                c += 1
            
            # old way to plot everything at once
            #plt.plot(*zip(*toplot), label=word) # this is other projects...
        
        #make legend
        if legend:
            lgd = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fancybox=True, framealpha=0.5)

    elif barchart:
        rcParams['figure.figsize'] = figsize, figsize/2
        cutoff = len(alldata)
        import numpy as np
        scores = [entry[1][1] for entry in alldata[:cutoff]]
        ind = np.arange(cutoff)  # the x locations for the groups
        width = 0.35       # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(ind, scores, width, color="#1f78b4")
        
        if len(results[0]) == 4:
            compscores = [entry[2][1] for entry in alldata[:cutoff]]
            rects2 = ax.bar(ind+width, compscores, width, color="#33a02c")
        
        # add some text for labels, title and axes ticks
        
        ax.set_xticks(ind+width)
        
        # get labels
        labels = [entry[0] for entry in alldata[:cutoff]]
        
        longest = len(max(labels, key=len))
        if longest > 7:
            if figsize < 20:
                if num_to_plot > 6:
                    ax.set_xticklabels(labels, rotation=45)
        else:
            ax.set_xticklabels(labels)

        # rotate the labels if they're long:

        
        #def autolabel(rects):
            # attach some text labels
            #for rect in rects:
                #height = rect.get_height()
                #ax.text(rect.get_x()+rect.get_width()/2., 1.0*height, '%d'%int(height),
                        #ha='center', va='bottom')
        
        #autolabel(rects1)
        #if len(results[0]) == 4:
            #autolabel(rects2)
        legend_labels = [alldata[0][1][0], alldata[0][2][0]]
        ax.legend( (rects1[0], rects2[0]), legend_labels )

    # make axis labels
    if x_lab:
        plt.xlabel(x_lab)

    if not y_label:
        #print "Warning: no name given for y-axis. Using default."
        if fract_of:
            y_label = 'Percentage'
        if not fract_of:
            y_label = 'Total frequency'
    plt.ylabel(y_label)
    pylab.title(title)

    if not barchart:
        plt.gca().get_xaxis().set_major_locator(MaxNLocator(integer=True))
        
        if log == 'x':
            plt.xscale('log')
            plt.gca().get_xaxis().set_major_formatter(ScalarFormatter())
        elif log == 'y':
            plt.yscale('log')
            plt.gca().get_yaxis().set_major_formatter(ScalarFormatter())
        elif log == 'x, y':
            plt.xscale('log')
            plt.gca().get_xaxis().set_major_formatter(ScalarFormatter())
            plt.yscale('log')
            plt.gca().get_yaxis().set_major_formatter(ScalarFormatter())
        else:
            plt.ticklabel_format(useOffset=False, axis='x', style = 'plain')
    plt.grid()
    fig1 = plt.gcf()
    if not have_python_tex:
        plt.show()

    def urlify(s):
            import re
            s = s.lower()
            s = re.sub(r"[^\w\s]", '', s)
            s = re.sub(r"\s+", '-', s)
            return s     
    
    if save:
        if type(save) == str:
            savename = os.path.join(imagefolder, urlify(save) + '.png')
        else:
            savename = os.path.join(imagefolder, urlify(title) + '.png')
        if legend and not barchart:
                fig1.savefig(savename, bbox_extra_artists=(lgd,), bbox_inches='tight', dpi=150, transparent=True)
        else:
            fig1.savefig(savename, dpi=150, transparent=True)
        time = strftime("%H:%M:%S", localtime())
        if os.path.isfile(savename):
            print time + ": " + savename + " created."
        else:
            raise ValueError("Error making %s." % savename)
    if csvmake:
        if type(csvmake) == bool:
            csvmake = urlify(title) + '.csv'    
        csvmaker(csvdata, csvalldata, csvmake)
