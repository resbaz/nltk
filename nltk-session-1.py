# <markdowncell>
# <br>
# <img style="float:left" src="http://ipython.org/_static/IPy_header.png" />
# <br>

# <headingcell level=1>
# Session 1: Orientation

# <markdowncell>
# <br>
# Welcome to the *IPython Notebook*. Through this interface, you'll be learning a lot of things:

# * A Programming language: **Python**
# * A Python library: **NLTK**
# * Overlapping research areas: **Corpus linguistics**, **Natural language processing**, **Distant reading**
# * Additional skills: **Regular Expressions**, some **Shell commands**, and **tips on managing your data**

# You can head [here](https://github.com/resbaz/lessons/blob/master/nltk/README.md) for the fully articulated overview of the course, but we'll almost always stay within IPython. 
# Remember, everything we cover here will remain available to you after ResBaz is over, including these Notebooks. It's all accessible at the [ResBaz GitHub](https://github.com/resbaz/lessons/tree/master/nltk).

# **Any questions before we begin?**

# Alright, we're off!

# <headingcell level=2>
# Text as data

# <markdowncell>
# Programming languages like Python are great for processing data. In order to apply it to *text*, we need to think about our text as data.
# This means being aware of how text is structured, what extra information might be encoded in it, and how to manage to give the best results. 

# <headingcell level=2>
# What is the Natural Language Toolkit?

# <markdowncell>
# <br>
# We'll be covering some of the theory behind corpus linguistics later on, but let's start by looking at some of the tasks NLTK can help you with. 

# <markdowncell>
# NLTK is a Python Library for working with written language data. It is free and extensively documented. Many areas we'll be covering are treated in more detail in the NLTK Book, available free online from [here](http://www.nltk.org/book/).

# > Note: NLTK provides tools for tasks ranging from very simple (counting words in a text) to very complex (writing and training parsers, etc.). Many advanced tasks are beyond the scope of this course, but by the time we're done, you should understand Python and NLTK well enough to perform these tasks on your own!

# We will start by importing NLTK, setting a path to NLTK resources, and downloading some additional stuff.

# <codecell>
# inline images:
% matplotlib inline
# ability to clear output:
from IPython.display import clear_output 
import nltk # imports all the nltk basics
user_nltk_dir = "/home/researcher/nltk_data" # specify our data directory
if user_nltk_dir not in nltk.data.path: # make sure nltk can access this dir
    nltk.data.path.insert(0, user_nltk_dir)
    nltk.download("book", download_dir=user_nltk_dir) # download book materials to data directory
clear_output() # clear the large amount of text we just generated

# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,
# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,
# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,
# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,
# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,
# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,
# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,
# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,
# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,
# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,

# <codecell>
#,,,


# <markdowncell>
# ### Common relationals
#  |  Relational | Meaning |
#  |--------------:|:------------|
#  | <    |  less than |
#  | <=   |   less than or equal to |
#  | ==  |    equal to (note this is two "=" signs, not one) |
#  | !=   |   not equal to |
#  | \>   |   greater than |
#  | \>= |   greater than or equal to |

# <markdowncell>
# ### Common operators
#  | Operator  | Purpose  |
#  |--------------|------------|
#  | s.startswith(t) | test if s starts with t |
#  | s.endswith(t)  |  test if s ends with t | 
#  | t in s         |  test if t is a substring of s | 
#  | s.islower()    |  test if s contains cased characters and all are lowercase | 
#  | s.isupper()    |  test if s contains cased characters and all are uppercase | 
#  | s.isalpha()    |  test if s is non-empty and all characters in s are alphabetic | 
#  | s.isalnum()    |  test if s is non-empty and all characters in s are alphanumeric | 
#  | s.isdigit()    |  test if s is non-empty and all characters in s are digits | 
#  | s.istitle()    |  test if s contains cased characters and is titlecased (i.e. all words in s have initial capitals) | 

# <markdowncell>
# 