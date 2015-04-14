#!/usr/bin/ipython

# this file stores functions that are needed for the nltk lessons.
# if somebody is having trouble getting something to work, they can
# often solve it by importing something from here.

def searchtree(tree, query):
    "Searches a tree with Tregex and returns matching terminals"
    ! echo "$tree" > "tmp.tree"
    tregex_command = 'sh ./tregex.sh -o -t \'' + query + '\' tmp.tree 2>/dev/null | grep -vP \'^\s*$\''
    result = !$tregex_command
    ! rm "tmp.tree"
    return result

def quicktree(sentence):
    """Parse a sentence and return a visual representation in IPython"""
    from nltk import Tree
    from nltk.draw.util import CanvasFrame
    from nltk.draw import TreeWidget
    from stat_parser import Parser
    from IPython.display import display
    from IPython.display import Image
    parser = Parser()
    parsed = parser.parse(sentence)
    cf = CanvasFrame()
    tc = TreeWidget(cf.canvas(),parsed)
    cf.add_widget(tc,10,10) # (10,10) offsets
    cf.print_to_file('tree.ps')
    cf.destroy()
    ! convert tree.ps tree.png
    ! rm tree.ps
    return Image(filename='tree.png')
    ! rm tree.png

def parse_metadata(text):
    "Parses Fraser Corpus metadata"
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