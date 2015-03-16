#!/usr/bin/python

#   Building scripts: make corpus of just 
#   basic dependencies from Stanford CoreNLP xml files
#   Author: Daniel McDonald

def get_dependencies(path, newpath, dep_type = 'basic-dependencies'):
    """Get just one kind of dependencies from a corpus with subcorpora.

    path: path to subcopora as string
    newpath: path for new corpus
    dep_type: specify type of dependencies:
                    'basic-dependencies'
                    'collapsed-dependencies'
                    'collapsed-ccprocessed-dependencies'
                    '"""
    import os
    from bs4 import BeautifulSoup
    sorted_dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path,d))]
    sorted_dirs.sort(key=int)
    for d in sorted_dirs:
        print 'Doing ' + d + ' ...'
        new_subcorpus_directory = os.path.join(newpath, d)
        if not os.path.exists(new_subcorpus_directory):
            os.makedirs(new_subcorpus_directory)
        filelist = os.listdir(os.path.join(path, d))
        for f in filelist:
            bits_to_keep = []
            with open(os.path.join(path, d, f), "r") as text:
                data = text.read()
                soup = BeautifulSoup(data)
                for dep_elem in soup.find_all('dependencies'):
                    deptype = dep_elem.attrs.get('type')
                    # get just parts matching dep_type
                    if deptype == dep_type:
                        bits_to_keep.append(dep_elem)
            with open(os.path.join(newpath, d, f), "w") as newfile:
                for bit in bits_to_keep:
                    newfile.write(str(bit))        

# running it:
#print 'Doing years ... '
#get_dependencies("data/nyt/years", "data/basic-dep/years")
#print 'Doing politics ... '
#get_dependencies("data/nyt/politics", "data/basic-dep/politics")
#print 'Doing health ... '
#get_dependencies("data/nyt/health", "data/basic-dep/health")
#print 'Doing economics ... '
#get_dependencies("data/nyt/economics", "data/basic-dep/economics")

def get_trees(path, newpath):
    """Get just parse trees from a corpus of CoreNLP output with subcorpora.

    path: path to subcopora as string
    newpath: path for new corpus
                    '"""
    import os
    from bs4 import BeautifulSoup
    sorted_dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path,d))]
    sorted_dirs.sort(key=int)
    for d in sorted_dirs:
        print 'Doing ' + d + ' ...'
        new_subcorpus_directory = os.path.join(newpath, d)
        if not os.path.exists(new_subcorpus_directory):
            os.makedirs(new_subcorpus_directory)
        filelist = os.listdir(os.path.join(path, d))
        for f in filelist:
            bits_to_keep = []
            with open(os.path.join(path, d, f), "r") as text:
                data = text.read()
                soup = BeautifulSoup(data)
                for dep_elem in soup.find_all('parse'):
                    bits_to_keep.append(dep_elem)
            with open(os.path.join(newpath, d, f), "w") as newfile:
                for bit in bits_to_keep:
                    newfile.write(str(bit))
    print 'Done!\n'


get_dependencies('data/bipolar/postcounts', 'data/bipolar/basic-dep/postcounts')