
# <markdowncell>
# <br>
# <img style="float:left" src="http://ipython.org/_static/IPy_header.png" />
# <br>

# <headingcell level=1>
# Session 4: Getting the most out of what we've learned

# <markdowncell>
# So, now you know Python and NLTK! The main things we still have to do are:

# 1. Run through a workflow that addresses some of your specific questions
# 2. Manage resources and results
# 3. Brainstorm some other uses for NLTK
# 4. Integrate IPython into your existing workflow
# 5. Have an open discussion about what we've done
# 6. Summarise and say goodbye!

# <codecell>
import nltk
from IPython.display import (display, clear_output, Image, display_pretty, 
                 display_html, display_jpeg, display_png, display_svg, HTML)
%matplotlib inline

# <headingcell level=2>
# A toy workflow: Project Gutenberg

# <markdowncell>
# We're going to start the session today by mining [Project Gutenberg](https://www.gutenberg.org/wiki/Technology_%28Bookshelf%29)'s *Food Processing* books.

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

# <headingcell level=3>
# [Tags used in the Brown Corpus](http://en.wikipedia.org/wiki/Brown_Corpus#Part-of-speech_tags_used)

# <markdowncell>
# 
# 

# <codecell>
HTML('<iframe src=http://en.wikipedia.org/wiki/Brown_Corpus#Part-of-speech_tags_used width=700 height=350></iframe>')

# <headingcell level=2>
# Getting your data into Python/NLTK

# <headingcell level=3>
# Scenario 1: You have some old books.

# <markdowncell>
# * Are they machine readable?
# * OCR options&mdash;institutional or DIY?
# * Structure them in a meaningful way&mdash;by author, by year, by language ... 
# * Start querying!

# <headingcell level=3>
# Scenario 2: You're interested in an online community.

# <markdowncell>
# * Explore the site. Sign up for it, maybe.
# * Download it: *Wget*, *curl*, *crawlers, spiders* ...
# * Extract relevant data and metadata: Python's *Beautiful Soup* library.
# * **Structure your data!**
# * Annotate your data, save these annotations
# * Start querying!

# <headingcell level=3>
# Scenario 3: Something of interest breaks in the news

# <markdowncell>
# * It will start being discussed all over the web.
# * You can use the Twitter API to harvest tweets containing a term or hashtag of interest.
# * You can get a list of RSS feeds and mine news articles
# * You can use something like *WebBootCat* to harvest search engine results and make a plain text corpus
# * Process these into a manageable form
# * Structure them
# * *Start querying!


# <headingcell level=2>
# Wrap up


# <headingcell level=3>
# Managing resources and results

# <markdowncell>
# You generate huge amounts of code, data and findings. Often, it's hard to know what to do with it all. In this section, we'll provide some suggestions designed to keep your work:

# 1. Reproducible
# 2. Reusable
# 3. Comprehensible

# <headingcell level=3>
# Your code

# <markdowncell>

# 1. Most importantly, **write comments on your code**. You **will** forget what bits of code are supposed to do. Using others' code is much easier if it's commented up. 
# 2. A related point is to name your variables meaningfully: *variablexxy* does not tell us much about what it will contain. *For image in images:*  is a very comprehensible line.
# 3. Also, write docstrings for your functions. Help messages come in very handy for not only others, but yourself. Simply stating what
# 2. **Version control**. When editing your code, you may sometimes break it. [Here](https://drclimate.wordpress.com/2012/11/16/version-control/)'s a write-up about version control from Damien Irving.
# 3. **Share your code**. You are often doing novel things when you code, and sharing what you've done can save somebody else a lot of work. *GitHub* is free for open-source projects. GitHub provides version control, which is especially useful when you are working with a team.

# <headingcell level=3>
# Developing as a programmer

# <markdowncell>
# We've only scratched the surface of Python, to be honest. In fact, we've only been treating Python as a programming language. Many of its users, however, see it as more than just a programming language: it is an ideology and culture, as well. 

# You'll notice on Stack Overflow, people will remark that some solutions are more 'pythonic' than others. By this, they typically mean that the code is easy to read and broken into discrete functions. More broadly, *pythonic* refers to code that adheres to the *Zen of Python*:

# <codecell>
import this

# <markdowncell>
# So, as you explore Python more and more, you learn not only new ways to get tasks done, but also what ways are better to others. While at first you'll be content with making code that works, you'll later want to make sure your code is elegant as well. Fixing up your old code becomes a form of procrastination from thesis writing. Luckily, of all the kinds of procrastination, it's one of the better kinds.

# Another change you might notice is a switch toward *defensive programming*, where you write code to handle potential errors, and to provide useful messages when people do something wrong. This is a really awesome thing to do.

# Some code authors also try to use *test-driven development*. From [the Wikipedia article](http://en.wikipedia.org/wiki/Test-driven_development):

# > First the developer writes an (initially failing) automated test case that defines a desired improvement or new function, then produces the minimum amount of code to pass that test, and finally refactors the new code to acceptable standards.

# This helps stop feature-creep, builds your confidence, and encourages the division of long code into well-defined functions.

# Oh, and you'll probably start dreaming in code. *Not* a joke.

# <headingcell level=3>
# Your data

# <markdowncell>
# It should now be clear to you that you have data!
# Think about how you structure it. Without necessarily becoming an archivist, do think about your metadata. It will help you to manage your data later.
# *Cloud computing* offers you access to more storage and compute-power than you might want to own. Plus you're unlikely to spill coffee on it.

# <headingcell level=3>
# Your findings

# <markdowncell>
# [*Figshare*](http://www.figshare.com) is a site for storing tables and figures. It's particularly useful for working with large datasets, as we often generate far more raw tables and statistics than we can possibly publish.

# It's becoming more and more common to link journal publications to additional online resources such as GitHub code or Figshares. It's also more and more common to cite GitHub and Figshare&mdash;always nice to bump up your citation count!

# <headingcell level=2>
# Integrating IPython into your workflow

# <markdowncell>
# What you've learned here isn't much good unless you can pull things out of it and put them into your own research workflow.

# It's important to remember that IPython code may be a little different from vanilla Python, as it can contain Magics, shell commands, and the like.

# Perhaps the coolest thing about programming is you are simultaneously researching and developing. The functions that you write can be uploaded to the web and used by others who encounter the problem that necessitated your writing the function in the first place.

# In reality, NLTK is nothing more than a lot of Python functions, coupled with some datasets (corpora, stopword lists, etc.). You can even visit NLTK on GitHub, fork their repository, and start playing around with the code! If you find bugs in the code, or if you think documentation is lacking, you can either write directly to the people who maintain the code, or fix the problem yourself and request that they review your fix and integrate it into NLTK.

# <headingcell level=3>
# Using IPython locally

# <markdowncell>
# We've done everything on the cloud so far, and it's been pretty good to us. You may also want to use IPython locally. To do this, you need to install it. There are many ways to install it, and these vary depending on your OS and what you already have installed. See the [IPython website](http://ipython.org/ipython-doc/2/install/install.html#installnotebook) for detailed instructions.

# > *[Anaconda](http://continuum.io/downloads)* is a large package of Python-based tools (including IPython and Matplotlib) that is easy to install. 

# Once you have IPython installed, it's very easy to start using it. All you need to do is open up Terminal, navigate to the notebook directory and type:

#      ipython notebook filename.ipynb

# This will open up a blank notebook, exactly the same as the kind of notebook we've been using on the cloud. The only difference will be that if you enter:

#      os.listdir('.')

# you'll get a list of files in the directory of your notebook file, rather than a directory of your part of the cloud.

# <headingcell level=2>
# Next steps - keep going!

# <codecell>
Image(url='http://starecat.com/content/wp-content/uploads/two-states-of-every-programmer-i-am-god-i-have-no-idea-what-im-doing.jpg')

# <markdowncell>
# We hope you've learned enough in these two days to be excited about what NLTK can add to your work and you're feeling confident to start working on your own.
# Code breaks. Often. Be patient and try not to get discouraged.
# The good thing about code breaking so often is that you can find help. Try:
# * Coming back to these notebooks and refreshing your memory
# * Checking the NLTK book
# * Googling your error messages. This will often lead you to Stack Overflow, the major online community for sharing coding questions.
# * NLTK also has a Google group where people share their experiences and ask for help
# * Keep in touch! Your community is a wonderful resource.

# <headingcell level=2>
# Summaries and goodbye

# <markdowncell>
# Before we go, we should summarise what we've learned. Add all this to your CV!

# * Navigating the IPython notebook
# * Python commands - defining a variable; building a function
# * Using Python to perform basic quantitative analysis of text
# * Tagging and parsing to perform more sophisticated analysis of language
# * A crash course in corpus linguistics!
# * An appreciation of clean vs messy data and data structure
# * Data management practices

# <headingcell level=2>
# Bragging rights 

# <markdowncell>
# You have learned a lot of stuff in under a week:

# * IPython
# * Python
# * NLTK
# * Linguistic theory

# Put it all on your resume. Be proud. And if you feel like writing up your findings, do it!

# <headingcell level=2>
# Thanks!

# <markdowncell>
# That's the end of of course. Thank you to everybody for your participation.

# Please let us know how you found the course.

# Come along to *Hacky Hour* (Tsubu, Thursdays at 3pm).

# Also, [submit a pull request](https://github.com/resbaz/nltk) and improve our teaching materials! 

# <markdowncell>
# 