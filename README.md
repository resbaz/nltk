# Data Carpentry with NLTK and IPython

<img style="float:left" src="http://ipython.org/_static/IPy_header.png" />
<br>

[![Join the chat at https://gitter.im/resbaz/resbaz](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/resbaz/resbaz?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This is the repository for teaching materials and additional resources used by Research Platforms Services to teach *Python*, *IPython* and the *Natural Language Toolkit* (*NLTK*).

All the materials used in NLTK workshops are in this repository. In fact, cloning this repository will be our first activity together as a group. To do that, just open your terminal and type/paste:

```shell
git clone https://github.com/resbaz/nltk.git
```

Though we'll be working with blank notebooks in our training sessions, everthing we cover lives as a complete notebook in the `resources/completed-notebooks` directory. These notebooks are useful for remembering or extending what you learned in during training. Alternatively, they may be useful for those who cannot attend our sessions face-to-face.

Below is a basic overview of the four-session lesson plan. You can click the headings to view complete versions of the IPython Notebooks we'll be using in each sessions. The materials are always evolving, and pull requests are always welcome.

## [Session 1: Orientation](http://nbviewer.ipython.org/github/resbaz/nltk/blob/master/resources/completed-notebooks/session-1.ipynb)

In this session, you will learn how to use IPython Notebooks, as well as how to complete basic tasks with Python/NLTK. 

* Getting up and running
* What exactly are *Python*, *IPython* and *NLTK*?
* Introductions to *IPython Notebook*
* Overview of basic Python concepts: *significant whitespace*, *input/output types*, *commands and arguments*, etc.
* Introduction to NLTK
* Quickstart: *US Inaugural Addresses Corpus*
* Plot key terms in the inaugural addresses longitudinally
* Discussion: *Why might we want to use NLTK? What are its limitations?*

## [Session 2: Functions, lists and variables](http://nbviewer.ipython.org/github/resbaz/nltk/blob/master/resources/completed-notebooks/session-2.ipynb)

In this session, we devote more time to the fundamentals of Python, learning how to create and manipulate different kinds of data. In the first half of the session, we discuss:

* Working with variables
* Writing functions
* Creating frequency distributions

In the second half of the session, we put our existing skills to work in order to investigate the corpora that come bundled with NLTK. The major kinds of analysis we cover are:

* Sentence splitting
* Tokenisation
* Keywords
* n-grams
* Collocates
* Concordancing

## [Session 3: The Fraser Corpus](http://nbviewer.ipython.org/github/resbaz/nltk/blob/master/resources/completed-notebooks/session-3.ipynb)

By this point, we're familiar with what NLTK is and how to use it. It's time to put it to work on a novel dataset. We've chosen a [corpus of Malcolm Fraser's speeches](http://www.unimelb.edu.au/malcolmfraser/speeches/electorate/). In this session, we begin by:

* Introducing the corpus
* Exploring corpus metadata
* Data structuring by metadata feature
* Getting keywords, n-grams, and collocates
* Part-of-speech tagging and parsing the data

Next, we'll use some purpose-built tools called [`corpkit`](https://www.github.com/interrogator/corpkit) to look for longitudinal changes in the language of Malcolm Fraser's speeches. These tools help us with:

* Searching syntax trees
* Interrogating each subcorpus
* Visualising results
* Viewing and editing results

We'll leave some time at the end of this session for exploring the Fraser Corpus, and for discussing what we found.

## [Session 4: Getting the most out of what we've learned](http://nbviewer.ipython.org/github/resbaz/nltk/blob/master/resources/completed-notebooks/session-4.ipynb)

So, we've learned some great skills! But, we need to know how to put these skills into practice within our own work. In this final session, we discuss:

* What kind(s) of data we're all working with
* Storing your data and results
* Using what you've learned here
* Developing your skills further
* Summarising and saying goodbye

# Adding to this repository

You're more than welcome to submit a pull request with changes

The `.ipynb` files used by both students and instructors are generated using plain `.py` files with IPython's `nbconvert` utility. Accordingly, the best way to modify our course materials is to update the `.py` file, rather than the `.ipynb` file. These live in `resources/notebook-source-files`.



Longer functions may be archived in `resources/scripts.py`, so that they may be imported by instructors/helpers on students' notebooks if need be.
