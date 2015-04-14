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

def plot(title, results, fract_of = False, y_label = False, 
    num_to_plot = 7, multiplier = 100, yearspan = False,
     justyears = False, csvmake = False, x_label = False):
    """
    Takes interrogator output and plots it with matplotlib

    title: String for chart title
    results: results in interrogator() output format.
        Results created with -C will not generate a legend.
    fract_of: a list of totals by which results will be divided. 
        The list should be in interrogator() -C output format. 
        By default, results will be multiplied by 100. 
        Absolute frequencies are given if false/omitted.
    num_to_plot: the top n results to be plotted (default 10)
    y_label: name for the y-axis (optional)
    multiplier: result * multiplier / total. 
        Use 100 for percentage, 1 for ratio.
    projection: project or do not project 1963 and 2014
    justyears = a list of years as integers to plot
    csvmake: enter filename as a string to make a csv file
    """

    # new options plan: smooth lines ...

    import matplotlib.pyplot as plt
    import pylab
    import numpy as np
    import os
    from time import localtime, strftime
    from IPython.display import display, clear_output
    from matplotlib.ticker import MaxNLocator
    from pylab import rcParams
    rcParams['figure.figsize'] = 9.6, 4.8

    def yearskipper(interrogator_list, justyears):
        """Takes a list and returns only results from the years listed in justyears"""
        
        skipped = []
        skipped.append(interrogator_list[0]) # append word
        for item in interrogator_list:
            if type(item) != unicode and type(item) != str:
                for year in justyears:
                    if item[0] == year:
                        skipped.append(item)
        return skipped

    def yearspanner(interrogator_list, yearspan):
        """Takes a list and returns results from between the first and last year in yearspan"""
        
        skipped = []
        skipped.append(interrogator_list[0]) # append word
        for item in interrogator_list:
            if type(item) != unicode and type(item) != str:
                if item[0] >= yearspan[0]:
                    if item [0] <= yearspan[-1]:
                        skipped.append(item)
        return skipped

    def fraction_maker(first_list, second_list):
        """Takes two lists and returns fraction totals for plotting"""
        fractioned = []
        for entry in first_list:
            fractioned_entry = []
            fractioned_entry.append(entry[0]) # append word
            for part in entry[1:]:
                numerator = part[1]
                denominator_datum = second_list[entry.index(part)]
                if denominator_datum[1] == 0:
                    fraction = 0
                else:
                    fraction = numerator * multiplier / float(denominator_datum[1])
                datum = [part[0], fraction]
                fractioned_entry.append(datum)
            fractioned.append(fractioned_entry)
        return fractioned

    def csvmaker(csvdata, csvalldata, csvmake):
        """Takes whatever ended up getting plotted and puts it into a csv file"""
        csv = []
        yearlist = []
        # get list of years
        for entry in csvdata[0]:
            if type(entry) == list:
                yearlist.append(str(entry[0]))
        # make first line
        years = ','.join(yearlist)
        # title then years for top row
        topline = title + ',' + years
        csv.append(topline)
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
        years = ','.join(yearlist)
        # title then years for top row
        topline = title + ',' + years
        csvall.append(topline)
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
            raise ValueError("CSV error: " + csvmake + " already exists in current directory.")
        try:
            fo=open(csvmake,"w")
        except IOError:
            print "Error writing CSV file."
        fo.write('Plotted results:\n\n'.encode("UTF-8"))
        fo.write(csv.encode("UTF-8"))
        fo.write('\n\nAll results:\n\n'.encode("UTF-8"))
        fo.write(csvall.encode("UTF-8"))
        fo.close()
        time = strftime("%H:%M:%S", localtime())
        print time + ": " + csvmake + " written to currect directory."

    ##################################################################

    # copy results and embed in list if need be.
    if type(results[0]) == unicode or type(results[0]) == str:
        legend = False
        data = [list(results)]
        alldata = [list(results)]
    else:
        legend = True
        data = list(results)
        alldata = list(results)

    # find out if we're doing years or not:
    if x_label:
        x_lab = x_label
    else:
        check_x_axis = data[0] # get first entry
        check_x_axis = check_x_axis[1] # get second entry of first entry (year, count)
        if 1500 < check_x_axis[0] < 2050:
            x_lab = 'Year'
        else:
            x_lab = 'Group'
    # copy totals data so as to not edit it
    if fract_of:
        totals = list(fract_of)
        # make fractions
        fractdata = fraction_maker(data, totals)
        data = list(fractdata)
        alldata = list(fractdata)

    csvdata = []
    csvalldata = []
    final = []
    # watercolour style:
    #colours = ["#66C2A5", "#FC8D62", "#8DA0CB", "#E78AC3", "#A6D854", "#FFD92F", "#E5C494", "#B3B3B3"]
    #colours = ["#4D4D4D", "#5DA5DA", "#FAA43A", "#60BD68", "#F17CB0", "#B2912F", "#B276B2", "#DECF3F", "#F15854"]
    colours = ["#1f78b4", "#33a02c", "#e31a1c", "#ff7f00", "#6a3d9a", "#a6cee3", "#b2df8a", "#fb9a99", "#fdbf6f", "#cab2d6"]

    c = 0
    # get an all data version if making csv
    if csvmake:
        for entry in alldata:
            # run called processes
            if yearspan:
                entry = yearspanner(entry, yearspan)
            if justyears:
                entry = yearskipper(entry, justyears)
            # get word
            word = entry[0]
            # for each datum [year, count]:

            # If anybody is reading this, the following sections are nonfunctional 
            #in ResBaz code, as they are mostly for use in NYT investigation. Sorry!

            toplot = []
            xvalsbelow = []
            yvalsbelow = []
            xvalsabove = []
            yvalsabove = []
            d = 1 # first tuple, maybe not very stable
            tups = len(entry) - 2 # all tuples minus 1
            for _ in range(tups):
                firstpart = entry[d] # first tuple
                firstyear = firstpart[0]
                nextpart = entry[d + 1]
                nextyear = nextpart[0]
                diff = nextyear - firstyear
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
            csvalldata.append(entry)
        # end repeated code
    
    # do code for actual plotting
    
    for entry in data[:num_to_plot]:
        # run called processes
        if justyears:
            entry = yearskipper(entry, justyears)
        if yearspan:
            entry = yearspanner(entry, yearspan)
        # get word
        word = entry[0]
        # for each datum [year, count]:
        toplot = []
        xvalsbelow = []
        yvalsbelow = []
        xvalsabove = []
        yvalsabove = []
        d = 1 # first tuple, maybe not very stable
        # could use list index
        tups = len(entry) - 2 # all tuples minus 1
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
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    # make axis labels
    plt.xlabel(x_lab)
    if not y_label:
        #print "Warning: no name given for y-axis. Using default."
        if fract_of:
            y_label = 'Percentage'
        if not fract_of:
            y_label = 'Total frequency'
    # no decimals on x axis:
    # make the chart
    plt.gca().get_xaxis().set_major_locator(MaxNLocator(integer=True))
    plt.ylabel(y_label)
    pylab.title(title)
    plt.ticklabel_format(useOffset=False, axis='x', style = 'plain')
    plt.grid()
    plt.show()

    if csvmake:
        csvmaker(csvdata, csvalldata, csvmake)
        