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
    