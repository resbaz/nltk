
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
# clear output from download
from IPython.display import display, clear_output
# import: all the nltk basics
import nltk
user_nltk_dir = "/home/researcher/nltk_data" # specify our data directory
if user_nltk_dir not in nltk.data.path: # make sure nltk can access this dir
    nltk.data.path.insert(0, user_nltk_dir)
nltk.download("book", download_dir=user_nltk_dir) # download book materials to data directory
clear_output()

# <markdowncell>
# Oh, we've got to import some corpora used in the book as well...

# <codecell>
from nltk.book import *  # asterisk means 'everything'

# <markdowncell>
# Importing the book has assigned variable names to ten corpora. We can call these names easily: 

# <codecell>
#text1
text2
#text3

# <headingcell level=3>
# Exploring vocabulary

# <markdowncell>
# NLTK makes it really easy to get basic information about the size of a text and the complexity of its vocabulary.

# *len* gives the number of symbols or 'tokens' in your text. This is the total number of words and items of punctuation.

# *set* gives you a list of all the tokens in the text, without the duplicates.

# Hence, **len(set(text3))** will give you the total number unique tokens. Remember this still includes punctuation. 

#*sorted* places items in the list into alphabetical order, with punctuation symbols and capitalised words first.

# <codecell>
len(text3)

# <codecell>
len(set(text3))

# <codecell>
sorted(set(text3)) 

# <markdowncell>
# We can investigate the *lexical richness* of a text. For example, by dividing the total number of words by the number of unique words, we can see the average number of times each word is used. 
# We can also count the number of times a word is used and calculate what percentage of the text it represents.

# <codecell>

len(text3)/len(set(text3))

# <codecell>
text4.count("American")

# <markdowncell>
# **Challenge!** 

# How would you calculate the percentage of Text 4 that is taken up by the word "America"?

# <codecell>
100.0*text4.count("America")/len(text4) 

# <headingcell level=3>
# Exploring text - concordances, similar contexts, dispersion

# <markdowncell>
# 'Concordance' shows you a word in context and is useful if you want to be able to discuss the ways in which a word is used in a text. 
# 'Similar' will find words used in similar contexts; remember it is not looking for synonyms, 
# although the results may include synonyms

# <codecell>
text1.concordance("monstrous")

# <codecell>
text1.similar("monstrous")

# <codecell>
text2.similar("monstrous")

# <codecell>
text2.common_contexts(["monstrous", "very"])  # this function takes two arguments

# <markdowncell>
# Python also lets you create graphs to display data.
# To represent information about a text graphically, import the Python library *numpy*. We can then generate a dispersion plot that shows where given words occur in a text.

# <codecell>
import numpy
text1.dispersion_plot(["whale"])

# <markdowncell>
# **Challenge!**
# <br>
# Create a dispersion plot for the terms "citizens", "democracy", "freedom", "duties" and "America" in the innaugural address corpus.
# What do you think it tells you? 

# <codecell>
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"]) # plot five words longitudinally

# <headingcell level=2>
# How Python works

# <markdowncell>
# We've seen a bit now of how NLTK can help you to interrogate a text. Let's back up and talk about Python itself and the environment we're using.

# <codecell>
# A simple welcome message printer.
# Anything after a hash is ignored
# Run a cell with shift+enter

condition = True
if condition is True:
    print 'Welcome to Python and the IPython Notebook.'

# <markdowncell>
# Success! *And so it begins ... *

# <headingcell level=2>
# The IPython Notebook

# <markdowncell>
# Before we start coding, we should familiarise ourselves with the IPython Notebook interface. Click *Help* --\> *User interface tour* to begin.
# <br>
# Keyboard shortcuts come in very handy. Click *Help* --\> *Keyboard shortcuts* to get an overview. *The more you code, the less you'll want to use your mouse!*

# <headingcell level=2>
# Python: core concepts

# <markdowncell>
# If you're new to Python, there are a few core concepts that will help you understand how everything works. Here, we'll cover:

# * Significant whitespace
# * Input/output types
# * Commands and arguments
# * Defining functions
# * Importing libraries, functions, etc.

# <headingcell level=3>
# Significant Whitespace

# <markdowncell>
# One thing that makes Python unique is that whitespace at the start of the line (use four spaces for consistency!) is meaningful. 
# In many other languages, whitespace at the start of lines is simply a readability convention.

# <codecell>
# Fix this whitespace problem!

string = 'user'
if string == 'user':
print 'Phew, fixed.'

# <markdowncell>
# So, whitespace tells both Python and human readers where things start and stop.

# <headingcell level=3>
# Input/Output Types

# <markdowncell>
# * Python understands different *types* of input, including *string*, *unicode string*, *integer*, *item*, *tuple* and *dict*.
# * Different types of information behave in different ways, and the ways they are represented visually are different as well.
# * You need to always make sure your input types are correct, or Python won't know what to do with them.
# * For example, if you're trying to do maths, you'll want to be working with *integers*:

# <codecell>
1 + 2  # integer plus integer

# <codecell>
1 + '2'  # integer plus string

# <markdowncell>

# Note the error message. These will help you to understand what went wrong. 
# The first part looks like gobbledygook, but the rest is helpful. Line 3 of error tells us what command
# was executing when the error happened, which can assist in isolating a problem. The leading digit is the line number.
# Line 4 actually tells us what the error was - that's what we would have googled if we were looking for a solution.

# <markdowncell>
# You can determine the type of data stored in a variable with *type()*. Here are some of the most common types. Note how quotation marks, and brackets are used to distinguish between them when writing code.

# <codecell>
var = 'A string'
print type(var)
var = u'A unicode string'
print type(var)
var = 42
print type(var)
var = ['item']
print type(var)
var = ('item', 'another')
print type(var)
var = {'entry': 7}
print type(var)

# <markdowncell>
# Sometimes you can sometimes easily convert between types.

# <codecell>
num = '2'
1 + int(num)

# <markdowncell>
# ... and sometimes it's not so easy:

# <codecell>
adjectives = ['wicked', 'radical', 'awesome']
more_adjectives = str(adjectives) + 'overwhelmed'
print more_adjectives

# <headingcell level=3>
# Basic syntax

# <markdowncell>
# **Only do this section if we have time!!**

# Python has *variables* and *commands*. Commands may have *arguments* and *options*.

# > IPython highlights your code automatically, which can help you read it faster and spot problems.

# <codecell>
from math import sqrt  # importing math library and square root function
avariable = 50  # make a variable that is 50 as integer
answer = sqrt(avariable)  # figure out the answer by issuing a command with avariable as an argument
print answer  # tell us

# <codecell>
# This example has two arguments
from math import pow  # importing pow function (pow is short for 'power')
avariable = 50
answer = pow(avariable, 3)  # 50 to the power of 3
print answer

# <headingcell level=2>
# Advantages of IPython

# <markdowncell>
# So, we've been writing Python code in an IPython notebook. Why?

# 1. The main strength of IPython is that you can run bits of code individually, so you don't have to keep repeating things. For example, if you scroll up to the last function and replace the 50 with 2, you can re-run that code and get the new answer. 
# 2. IPython allows you to display images alongside code, and to save the input and output together.
# 3. IPython makes learning a bit easier, as mistakes are easier to find and do not break an entire workflow.

# You can get more information on IPython, including how to install it on your own machine, at the [IPython Homepage](http://ipython.org).

# <markdowncell>
# So, at this point, why don't you tell us what you make of it all. Can anyone see potential for Python in their own research? What are you working on, anyway? 

# Anything you're struggling with so far?

# At this point, we want to dive more deeply into general Python functionality. We want to define some functions, manipulate some lists, and understand better what variables are and what they do.

# <headingcell level=3>
# Defining a function

# <markdowncell>
# Next, we'll talk about *functions*. Here's an example:

# <codecell>
def welcomer(name):
    print 'Welcome, %s!' % name

# <markdowncell>
# Notice that it doesn't do anything by itself. It needs to actually be *called*, and given some data:

# <codecell>
welcomer('Kim')

# <markdowncell>
# You may wish to repeat an operation multiple times looking at different texts or different terms within a text. Instead of re-entering the formula every time, you can assign a name and set of actions to a particular task.

# Previously, we calculated the lexical diversity of a text. In NLTK, we can create a function called **lexical diversity** that runs a single line of code. We can then call this function to quickly determine the lexical density of a corpus or subcorpus.

# Advantages of functions:
# 1. Save you typing
# 2. You can be sure you're doing exactly the same operation every time
# <br>
# > **Note** Learn to love tab-completion! Typing the first one or two letters of a command you've used previously then hitting tab 
# will auto-complete that command, saving you typing (i.e. time and mistakes!). 
 
# <markdown cell>
# **Challenge!**

# Using a function, determine which of the nine texts in the NLTK Book has the highest lexical diversity score.

# <codecell>
def lexical_diversity(text):
    return len(text)/len(set(text))

# <codecell>
#After the function has been defined, we can run it:
lexical_diversity(text2)

# <markdowncell>
# The parentheses are important here as they sepatate the the task, that is the work of the function, from the data that the function is to be performed on. 

# The data in parentheses is called the argument of the function. When we use a function, we say that we 'call' it. 

# Other functions that we've used already include len() and sorted() - these were predefined. *lexical_diversity()* is one we set up ourselves; note that it's conventional to put a set of parentheses after a function, to make it clear what we're talking about.

# <headingcell level=3>
# Lists

# <markdowncell>
# Python treats a text as a long list of words. First, we'll make some lists of our own, to give you an idea of how a list behaves.

# <codecell>
sent1 = ['Call', 'me', 'Ishmael', '.']

# <codecell>
sent1

# <codecell>
len(sent1)

# <markdowncell>
# The opening sentences of each of our texts have been pre-defined for you. You can inspect them by typing in 'sent2' etc.

# You can add lists together, creating a new list containing all the items from both lists. You can do this by typing out the two lists or you can add two or more pre-defined lists. This is called concatenation.

# <codecell>
sent4 + sent1

# <markdowncell>
# We can also add an item to the end of a list by appending. When we append(), the list itself is updated. 

# <codecell>
sent1.append('Please')
sent1

# <markdowncell>
# There are some things we can do to make it easier to read the contents of a string. Note that we get some brackets and so on when we try to print the items in a list as a string.

# <codecell>
fruitsalad = []  # declare an empty list
fruitsalad.append('watermelon')  # add watermelon
fruitsalad.append('orange')  # add orange
print 'Our fruit salad contains: ' + str(fruitsalad)

# <markdowncell>
# If we want to print our ingredients in a nicer looking form, we might use a function like *join()*

# <codecell>
fruitsalad = []
fruitsalad.append('watermelon')
fruitsalad.append('orange')
listasastring = ''.join(fruitsalad)  # create a string with all the list items joined together
print 'Our fruit salad contains: ' + listasastring

# <markdowncell>
# ... whoops! Still ugly. We didn't put anything in between the '' to use as a delimiter.

# <codecell>
fruitsalad.append('canteloupe')
listasastring = ', '.join(fruitsalad)  # note the comma and space in quotation marks
print 'Our fruit salad contains: ' + listasastring

# <headingcell level=3>
#  Indexing Lists

# <markdowncell>
# We can navigate this list with the help of indexes. Just as we can find out the number of times a word occurs in a text, we can also find where a word first occurs. We can navigate to different points in a text without restriction, so long as we can describe where we want to be.

# <codecell>
print text4.index('awaken')

# <markdowncell>
# This works in reverse as well. We can ask Python to locate the 158th item in our list (note that we use square brackets here, not parentheses)

# <codecell>
print text4[158]

# <markdowncell>
# As well as pulling out individual items from a list, indexes can be used to pull out selections of text from a large corpus to inspect. We call this slicing

# <codecell>
print text5[16715:16735]

# <markdowncell>
# If we're asking for the beginning or end of a text, we can leave out the first or second number. For instance, [:5] will give us the first five items in a list while [8:] will give us all the elements from the eighth to the end. 

# <codecell>
print text2[:10]
print text4[145700:]

# <markdowncell>
# To help you understand how indexes work, let's create one.

# We start by defining the name of our index and then add the items. You probably won't do this in your own work, but you may want to manipulate an index in other ways. Pay attention to the quote marks and commas when you create your test sentence.

# <codecell>
sent = ['The', 'quick', 'brown', 'fox']
sent[0]
print sent[2]

# <markdowncell>
# Note that the first element in the list is zero. This is because we are telling Python to go zero steps forward in the list. If we use an index that is too large (that is, we ask for something that doesn't exist), we'll get an error.

# We can modify elements in a list by assigning new data to one of its index values. We can also replace a slice with new material.

# <codecell>
sent[2] = 'furry'
sent[3] = 'child'
print sent

# <headingcell level=3>
#  Defining variables

# <markdowncell>
# In Python, we give the items we're working with names, a process called assignment. For instance, in the NLTK corpus, 'Sense and Sensibility' has been assigned the name 'text2', which is much easier to work with. 
# We also assigend the name 'sent' to the sentence that we created in the previous exercise, so that we could then instruct Python to do various things with it. Assigning a variable in python looks like this:  
# variable = expression   
# You can call your variables (almost) anything you like, but it's a good idea to pick names that will be meaningful and easy to type. You can't use words that already have a meaning in Python, such as import, def, or not. If you try to use a word that is reserved, you'll get a syntax error.

# <markdowncell>
# *Challenge*
#1. Create a list called 'opening' that consists of the phrase "It was a dark and stormy night; the rain fell in torrents"
#2. Create a variable called 'clause' that contains the contents of 'opening', up to the semi-colon
#3. Create a variable called 'alphabetised' that contains the contents of 'clause' sorted alphabetically
#4. Print 'alphabetised' 

# <codecell>
opening = ['It', 'was', 'a', 'dark', 'and', 'stormy', 'night', ';', 'the', 'rain', 'fell', 'in', 'torrents']
clause = opening[0:7]
alphabetised = sorted(clause)

# <markdowncell>
# Note that assigning a variable just causes Python to remember that information without generating any output. 

# If you want Python to show you the result, you have to ask for it (this is a good thing when you assign a variable to a very long list!).

# <codecell>
print clause

# <codecell>
print alphabetised

# <headingcell level=3>
# Frequency distributions

# <markdowncell>
# We can use Python's ability to perform statistical analysis of data to do further exploration of vocabulary. For instance, we might want to be able to find the most common or least common words in a text. We'll start by looking at frequency distribution.

# <codecell>
fdist1 = FreqDist(text1)

# <codecell>
fdist1.most_common(50)

# <codecell>
fdist1['whale']

# <codecell>
fdist1.plot(50, cumulative = True)

# <markdowncell>
# *Challenge!*

# Create a function called "Common_Words" and use it to compare the 15 most common words of four of the texts in the NLTK book. 
# Discuss what you found with your neighbour.

# <markdowncell>
# As well as counting individual words, we can count other features of vocabulary, such as how often words of different lengths occur. We do this by putting together a number of the commands we've already learned.

# We could start like this: 

#      [len(w) for w in text1]

# ... but this would print the length of every word in the whole book, so let's skip that bit!

# <codecell>
fdist2= FreqDist(len(w) for w in text1)

# <codecell>
fdist2.max()

# <codecell>
fdist2.freq(3)

# <markdowncell>
# These last two commands tell us that the most common word length is 3, and that these 3 letter words account for about 20% of the book. 
# We can see this just by visually inspecting the list produced by *fdist2.most_common()*, but if this list were too long to inspect readily, or we didn't want to print it, there are other ways to explore it.  

# <markdowncell> 
# It is possible to select the longest words in a text, which may tell you something about its vocabulary and style

# <codecell>
v = set(text4)
long_words = [word for word in v if len(word) > 15]
sorted(long_words)

# <markdowncell>
# We can fine-tune our selection even further by adding other conditions. For instance, we might want to find long words that occur frequently (or rarely).  

# **Challenge!**

# Can you find all the words in a text that are more than seven letters long and occur more than seven times?

# <codecell>
fdist3 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)

# <markdowncell>
# There are a number of functions defined for NLTK's frequency distributions:
#
#  | Function | Purpose  |
#  |--------------|------------|
#  | fdist = FreqDist(samples) | create a frequency distribution containing the given samples |
#  | fdist[sample] += 1 | increment the count for this sample |
#  | fdist['monstrous']  | count of the number of times a given sample occurred |
#  | fdist.freq('monstrous') | frequency of a given sample |
#  | fdist.N()  |  total number of samples |
#  | fdist.most_common(n)   |  the n most common samples and their frequencies |
#  | for sample in fdist:   |  iterate over the items in fdist, when in the loop, we refer to each item as sample |
#  | fdist.max() | sample with the greatest count |
#  | fdist.tabulate()   |  tabulate the frequency distribution |
#  | fdist.plot()  |   graphical plot of the frequency distribution |
#  | fdist.plot(cumulative=True) | cumulative plot of the frequency distribution |
#  | fdist1 < fdist2 | test if samples in fdist1 occur less frequently than in fdist2 |

# <markdowncell>
# We can also find words that typically occur together, which tend to be very specific to a text or genre of texts. We'll talk more about these features and how to use them later.

# <codecell>
text4.collocations()

# <markdowncell>
# We can also use numerical operators to refine the types of searches we ask Python to run. We can use the following relational operators:
#
#
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
# *Challenge!*
# Using one of the pre-defined sentences in the NLTK corpus, use the relational operators above to find:

# <markdowncell>
# 1. Words longer than four characters
# 2. Words of four or more characters
# 3. Words of exactly four characters

# <codecell>
# Words longer than four characters:
#

# <codecell>
# Words of four or more characters:
#

# <codecell>
# Words of exactly four characters:
#
# <markdowncell>
# ### Common operators
#
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

# <codecell>
sorted(w for w in set(text1) if w.endswith('ableness'))

# <codecell>
sorted(n for n in sent7 if n.isdigit())

# <markdowncell>
# Have a play around with some of these operators in the cells below.

# <codecell>
#

# <codecell>
#

# <codecell>
# You can insert more cells via the menu bar if you need to!

# <markdowncell>
# **Bonus!**

# You'll remember right at the beginning we started looking at the size of the vocabulary of a text, but there were two problems with the results we got from using:

#      len(set(text1)).

# This count includes items of punctuation and treats capitalised and non-capitalised words as different things (*This* vs *this*). We can now fix these problems. We start by getting rid of capitalised words, then we get rid of the punctuation and numbers.

# <codecell>
len(set(word.lower() for word in text1))

# <codecell>
len(set(word.lower() for word in text1 if word.isalpha()))

# <markdowncell>
# <img style="float:left" src="http://images.catsolonline.com/cache/custom/CEN/CE651-250x250.jpg" />
# <br>

# <markdowncell>
# You've completed the introduction to Python Natural Language Toolkit! To summarise, here's what you've learned so far:

# * How to navigate the iPython notebook
# * How Python uses whitespace 
# * Why functions are useful and how to define one
# * How to use basic Python commands to start exploring features of a text
#
# We'll practice all these commands in the following lessons ... so don't panic!

# It's a lot to take in and it will probably take a while before you feel really comfortable.

# <markdowncell>
# 