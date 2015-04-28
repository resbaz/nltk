# <markdowncell>
# <br>
# <img style="float:left" src="http://ipython.org/_static/IPy_header.png" />
# <br>

# <headingcell level=1>
# Downloading and analysing text with Python and NLTK

# <markdowncell>
# Welcome to *Python* and the *IPython Notebook*! Today, we're demonstrating **Python**, a programming language, and **NLTK**, a Python library for working with language.

# <markdowncell>
# Whatever your area of study, Python can speed up repetitive tasks and ensure that whatever you do can quickly be redone, by anyone.

# <codecell>
subjects = ['Environmental Law', 'Family Law', 'Mergers & Acquisitions']

for subject in subjects:
    print "You're taking %s!? How interesting!" % subject

# <headingcell level=1>
# Downloading a lot of text

# <markdowncell>
# You can use Python to automatically download a bunch of text from the web.

# <headingcell level=2>
# Import HTML parser, define and read a URL

# <codecell>
from bs4 import BeautifulSoup
from urllib import urlopen

# <codecell>
url = 'http://www.lawyersweekly.com.au'
raw = urlopen(url).read()
print raw[:2000]
soup = BeautifulSoup(raw)

# <headingcell level=2>
# Get a list of all links in that URL

# <codecell>
links = []
for link in soup.find_all('a'):
    link = link.get('href')
    if link and '/news/' in link and 'disqus' not in link:
        links.append(url + link)

# remove duplicates
links = sorted(set(links))

# <headingcell level=2>
# Our URLs

# <codecell>
for link in links:
    print link

# <headingcell level=2>
# Get article text from each URL

# <codecell>
texts = []
for link in links:
    raw = urlopen(link).read()
    soup = BeautifulSoup(raw)
    paras = soup.find_all('p')
    text = '\n'.join([para.text for para in paras if not para.text.startswith('Lawyers Weekly')])
    texts.append(text)

# <headingcell level=2>
# What did we get?

# <codecell>
print 'We have %d stories!\n' % len(texts)

# <codecell>
print texts[2]

# <headingcell level=1>
# Analysing these texts

# <markdowncell>
# Let's turn our texts into a single item:

# <codecell>
text = '\n'.join(texts)
print text[:500]

# <markdowncell>
# Then, we turn our text into a list of words with NLTK

# <codecell>
import nltk
words = nltk.word_tokenize(text)
print words[:50]

# <markdowncell>
# With a list of words, we can then search for interesting patterns.

# <headingcell level=2>
# Concordancing

# <codecell>
searchable_text = nltk.Text(words)  # formats our tokens for concordancing
searchable_text.concordance("Australia")

# <headingcell level=2>
# Keywording

# <codecell>
import corpkit
from corpkit import keywords
encoded_text = text.encode('utf-8', errors = 'ignore')
keywords, ngrams = keywords(encoded_text, dictionary = 'bnc.p')

# <markdowncell>
# Results?

# <codecell>
for key in keywords[:25]:
    print key

# <codecell>
for ngram in ngrams[:25]:
    print ngram

# <headingcell level=2>
# Other ideas ...

# <markdowncell>
# Using Python and/or NLTK, you can automatically:

# * Group texts into topics
# * Analyse sentiment
# * Annotate the text for grammatical features, for more advanced searching
# * Quantify the tone of texts
# * Sort texts by the likelihood of their containing what you want
# * Archive texts cleanly

# <headingcell level=2>
# Use this Notebook and code!

# <markdowncell>
# **Head to [github.com/resbaz/nltk](https://www.github.com/resbaz/nltk) to access these materials and more.**

# <markdowncell>
#