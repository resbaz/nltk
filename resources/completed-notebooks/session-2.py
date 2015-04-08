
# <markdowncell>
# <br>
# <img style="float:left" src="http://ipython.org/_static/IPy_header.png" />
# <br>

# <headingcell level=1>
# Session 2: Common NLTK tasks

# <markdowncell>
# <br>
# In this session we provide an quick introduction to the field of *corpus linguistics*. We then engage with common uses of NLTK within these areas, such as sentence segmentation, tokenisation and stemming. Often, NLTK has inbuilt methods for performing these tasks. As a learning exercise, however, we will sometimes build basic tools from scratch.

# <headingcell level=2>
# Corpus linguistics

# <markdowncell>
# Though corpus linguistics has been around since the 1950s, it is only in the last 20 years that its methods have been made available to individual researchers. GUIs including [Wordsmith Tools](http://www.lexically.net/wordsmith/) and [AntConc](http://www.laurenceanthony.net/software.html). 

# Alongside the development of GUIs, there has also been a shift from *general, balanced corpora* (corpora seeking to represent a language generally) toward *specialised corpora* (corpora containing texts of one specific type, from one speaker, etc.). More and more commonly, texts are taken from the Web.

# > **Note:** We'll discuss building corpora from online texts in a bit more detail tomorrow afternoon.

# After a long period of resistance, corpus linguistics has gained acceptence within a number of research areas. A few popular applications are within:

# * **Lexicography** (creating usage-based definitions of words and locating real examples)
# * **Language pedagogy** (advanced language learners can use a concordancing GUI or collocation tests to understand how certain words are used in the target language)
# * **Discourse analysis** (researching how meaning is made beyond the level of the clause/sentence)

# Notably, corpus linguistic methods have been embraced within the emerging paradigm of Digital Humanities, where it's sometimes called *distant reading*.

# <headingcell level=3>
# Corpora and discourse

# <markdowncell>
# As hardware, software and data become more and more available, people have started using corpus linguistic methods for discourse-analytic work. Paul Baker refers the combination of corpus linguistics and (critical) discourse analysis as a [*useful methodological synergy*](#ref:baker). Corpora bring objectivity and empiricism to a qualitative, interpretative tradition, while discourse-analytic methods provide corpus linguistics with a means of contextualising abstracted results.

# Within this area, researchers rely on corpora to varying extents. In *corpus-driven* discourse analysis, researchers interpret the corpus based on the findings of the corpus interrogation. In *corpus-assisted* discourse analysis, researchers may use corpora to provide evidence about the way a given person/idea/discourse is commonly represented by certain people/in certain publications etc.

# Our work here falls under the *corpus-driven* heading, as we are exploring the dataset without any major hypotheses in mind.

# > **Note:** Some linguists remain skeptical of corpus linguistics generally. In a well-known critique, Henry Widdowson ([2000, p. 6-7](#ref:widdowson)) said:
# >
# > Corpus linguistics \[...\] (there) is no doubt that this is an immensely important development in descriptive linguistics. That is not the issue here. The quantitative analysis of text by computer reveals facts about actual language behaviour which are not, or at least not immediately, accessible to intuition. There are frequencies of occurrence of words, and regular patterns of collocational co-occurrence, which users are unaware of, though they must be part of their competence in a procedural sense since they would not otherwise be attested. They are third person observed data ('When do they use the word X?') which are different from the first person data of introspection ('When do I use the word X?'), and the second person data of elicitation ('When do you use the word X?'). Corpus analysis reveals textual facts, fascinating profiles of produced language, and its concordances are always springing surprises. They do indeed reveal a reality about language usage which was hitherto not evident to its users.
# >
# > But this achievement of corpus analysis at the same time necessarily defines its limitations. For one thing, since what is revealed is contrary to intuition, then it cannot represent the reality of first person awareness. We get third person facts of what people do, but not the facts of what people know, nor what they think they do: they come from the perspective of the observer looking on, not the introspective of the insider. In ethnomethodogical terms, we do not get member categories of description. Furthermore, it can only be one aspect of what they do that is captured by such quantitative analysis. For, obviously enough, the computer can only cope with the material products ofwhat people do when they use language. It can only analyse the textual traces of the processes whereby meaning is achieved: it cannot account for the complex interplay of linguistic and contextual factors whereby discourse is enacted. It cannot produce ethnographic descriptions of language use. In reference to Hymes's components of communicative competence (Hymes 1972), we can say that corpus analysis deals with the textually attested, but not with the encoded possible, nor the contextually appropriate.
# > 
# > To point out these rather obvious limitations is not to undervalue corpus analysis but to define more clearly where its value lies. What it can do is reveal the properties of text, and that is impressive enough. But it is necessarily only a partial account of real language. For there are certain aspects of linguistic reality that it cannot reveal at all. In this respect, the linguistics of the attested is just as partial as the linguistics of the possible.

# <headingcell level=2>
# Loading a corpus

# <markdowncell>
# First, we have to load a corpus. We'll use a text file containing posts to an Australian online forum for discussing politics. It's full of very interesting natural language data!

# <codecell>
from IPython.display import display
from IPython.display import HTML
HTML('<iframe src=http://www.ozpolitic.com/forum/YaBB.pl?board=global width=700 height=350></iframe>')

# <markdowncell>
# This file is available online, at the [ResBaz GitHub](https://github.com/resbaz). We can ask Python to get it for us. 

# > Later in the course, we'll discuss how to extract data from the Web and turn this data into a corpus.

# <codecell>
from urllib import urlopen # a library for working with urls
url = "https://raw.githubusercontent.com/resbaz/lessons/master/nltk/corpora/oz_politics/ozpol.txt" # define the url
raw = urlopen(url).read() # download and read the corpus into raw variable
raw = unicode(raw.lower(), 'utf-8') # make it lowercase and unicode
len(raw) # how many characters does it contain?
raw[:2000] # first 2000 characters

# <markdowncell>
# We actually already downloaded this file when we first cloned the ResBaz GitHub repository. It's in our *corpora* folder. We can access it like this:

# <codecell>
f = open('corpora/oz_politics/ozpol.txt')
raw = f.read()
raw = unicode(raw.lower(), 'utf-8') # make it lowercase and unicode
len(raw)
raw[:2000] 

# <headingcell level=2>
# Regular Expressions

# <markdowncell>
# Before we go any further, we need to talk about Regular Expressions. Regular Expressions (regexes) are ways of searching for complex patterns in strings. Regexes are standardised across many programming languages, and can also be used in GUI text editors and word processers.

# <codecell>
import nltk # just in case (you should only need to import a library once per session, 
    # but nothing bad will happen if you do it again)
import re # import this before using regexes!

# <markdowncell>
# If only using alphanumeric characters and spaces, regexes work like any normal search.

# <codecell>
# print only match
regex = re.compile(r"government")
re.findall(regex, raw)

# <markdowncell>
# Hmm ... not very useful.

# <codecell>
# print whole line
regex = re.compile(r'government')
for line in raw.splitlines():
    if regex.search(line) is not None:
        print line

# <markdowncell>
# ... but regex can be much more powerful than that. Certain characters have special meanings:

# * . (period): any character
# * \* (asterisk): any number of times
# * \b: word boundary
# * ^ (carat): start of a line
# * $ (dollar sign): end of a line
# * \+ (plus): one or more times
# * [xy]: either x or y
# * o{5}: five os in a row
# * o{5,}: at least five os in a row
# * o{,5}: max five os in a row
# * (any|of|these|words)

# <codecell>
# [a-z] means any letter
# the plus means ''one or more of the thing before''
regex = re.compile(r"[a-z]+ment")
# find all instances of regex in raw
results = re.findall(regex, raw)
sorted(set(results)) # sort and print only unique results

# <codecell>
# word at start of line that ends in ion:
regex = re.compile(r"^[a-z]+ion\b")
# find all instances of regex in raw
results = re.findall(regex, raw)
sorted(set(results)) # sort and print only unique results

# <markdowncell>
# Sometimes, we want match the special characters:

# <codecell>
string = 'What!? :) U fink im flirtin wit *u*!? LOL'
# define a regex:
regex = re.compile(r':)')
re.findall(regex, string)

# <markdowncell>
# What happened? Well, if you want to search for any special character, it must be 'escaped' by a backslash:

# <codecell>
string = 'What!? :) U fink im flirtin wit *u*!? LOL'
# define a regex:
regex = re.compile(r':\)')
re.findall(regex, string)

# <markdowncell>
# Regular expressions take a while to master, but have great benefits for searching large texts for very specific things. Here are some additional regex resources:

# * [Regex Info](http://www.regular-expressions.info/): tutorials etc.
# * [Regexr](http://www.regexr.com/): a place to build and test out your regex
# * [Regex crosswords](http://regexcrossword.com/): exactly what you think it is!

# <markdowncell>
# The code below will get any word over *minlength* alphabetic characters by passing an integer into a regex.

# <codecell>
minlength = 5  # minimum number of letters as integer 
# gets passed into the building of the regex
sentence = 'We, the democratically-elected leaders of our people, hereby declare Kosovo to be an independent and sovereign state'

# any letter, minlength times:
pattern = re.compile(r'[A-Za-z]{' + str(minlength) + ',}') 
# What happens if you add a hyphen after 'a-z' inside the square brackets above?
re.findall(pattern, sentence)

# <headingcell level=2>
# Sentence segmentation

# <markdowncell>
# So, with a basic understanding of regex, we can now start to turn our corpus into a structured resource. At present, we have 'raw', a very, very long string of text.

#  We should break the string into segments. First, we'll split the corpus into sentences. This task is a pretty boring one, and it's tough for us to improve on existing resources. We'll try, though.

# Let's define a sentence as any string ending with (one or more) newline, full stop, question mark, or exclamation mark. A regex can be written to find these, and the split() function can  be used to break the string into a list of strings.

# <codecell>
import re
sentences = re.split("(\n|\.|\?|!)+", raw)
print 'Sentence: ' + '\nSentence: '.join(sentences[:10]) # print the first ten sentences

# <markdowncell>
# Well, it worked, sort of. What problems do we have?

# 1. sh.thole was split
# 2. Empty matches/punctuation only matches

# So, to fix our first problem, we have to make an intpretative decision. Is *sh.thole* a word? We could:

# 1. Clean the corpus and remove this false positive
# 2. Define sentence differently

# We'll go with the second option, for better or worse. The regex in the code below makes sure that any sentence final character must not be followed by a letter.

# <codecell>
sentences = re.split("(?:\n|\.|\?|!)+([^a-zA-Z]|$)", raw)
print 'Sentence: ' + '\nSentence: '.join(sentences[:10])

# <markdowncell>
# Problem 1 is solved: *sh.thole* is now a single token. To fix Problem 2, we will remove list items not containing a letter, as any sentence must contain at least one by definition.

# <codecell>
regex = re.compile('[a-zA-Z]')
no_blanklines = [sentence for sentence in sentences if regex.match(sentence)]
# or, an alternative approach using filter function:
# no_blanklines = filter(regex.match, sentences)
print 'Sentence: ' + '\nSentence: '.join(no_blanklines[:20]) # this should be better!

# <markdowncell>
# The code below turns out sentence segmenter into a function.

# <codecell>
def sent_seg(string):
    allmatches = re.split("(?:\n|\.|\?|!)+([^a-zA-Z]|$)", string)
    regex = re.compile('[a-zA-Z]')
    sentences = [sentence for sentence in allmatches if regex.match(sentence)]
    length = len(sentences)
    return sentences

# <codecell>
# Call the segmenter on our raw text here. Store it in a variable called 'sents'

# <markdowncell>
# It's all academic, anyway: NLTK actually has a sentence segmenter built in that works better than ours (we didn't deal with quotation marks, or brackets, for example).

# <codecell>
sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
sents = sent_tokenizer.tokenize(raw)
sents[101:111]

# <markdowncell>
# Alright, we have sentences. Now what?

# <headingcell level=2>
# Tokenisation

# <markdowncell>
# Tokenisation is simply the process of breaking texts down into words. We already did a little bit of this in Session 1. We won't build our own tokenizer, because it's not much fun. NLTK has one we can rely on.

# Keep in mind that definitions of tokens are not standardised, especially for languages other than English. Serious problems arise when comparing two corpora that have been tokenised differently.

# > **Note:** It is also possible to use NLTK to break tokens into morphemes, syllables, or phonemes. We're not going to go down those roads, though.

# <codecell>
tokenized_sents = [nltk.word_tokenize(i) for i in sents]
print tokenized_sents[:10]
# another view:
# tokenized_sents[:10]

# <headingcell level=2>
# Stemming

# <markdowncell>
# Stemming is the task of finding the stem of a word. So, *cats --> cat*, or *taking --> take*. It is an important task when counting words, as often the counting each inflection seperately is not particuarly helpful: forms of the verb 'to be' might seem under-represented if we could *is, are, were, was, am, be, being, been* separately. 

# NLTK has pre-programmed stemmers, but we can build our own using some of the skills we've already learned.

# A stemmer is the kind of thing that would make a good function, so let's do that.

# <codecell>
def stem(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']: # list of suffixes
        if word.endswith(suffix):
            return word[:-len(suffix)] # delete the suffix
    return word

# <markdowncell>
# Let's run it over some text and see how it performs.

# <codecell>
# empty list for our output
stemmed_sents = []
for sent in tokenized_sents:
    # empty list for stemmed sentence:
    stemmed = []
    for word in sent:
        # append the stem of every word
        stemmed.append(stem(word))
    # append the stemmed sentence to the list of sentences
    stemmed_sents.append(stemmed)
# pretty print the output
stemmed_sents[:10]

# <markdowncell>
# Looking at the output, we can see that the stemmer works: *wingers* becomes *winger*, and *tearing* becomes *tear*. But, sometimes it does things we don't want: *Nothing* becomes *noth*, and *mate* becomes *mat*. Even so, for the learns, let's rewrite our function with a regex:

# <codecell>
def stem(word):
    import re
    # define a regex to get word, and common suffixes
    regex = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regex, word)[0]
    return stem

# <markdowncell>
# Because we just redefined the *stem()* function, we can run the previous code and get different results.


# <markdowncell>
# Here's a very quick implementation of our stemmer on our raw tokens:

# <codecell>
tokens = nltk.word_tokenize(raw)
stemmed = [stem(t) for t in tokens]
print stemmed[:50]

# <markdowncell>
# We can see that this approach has obvious limitations. So, let's rely on a purpose-built stemmer. These rely in part on dictionaries. Note the subtle differences between the two possible stemmers:

# <codecell>
# define stemmers
lancaster = nltk.LancasterStemmer()
porter = nltk.PorterStemmer()
# stem each word in tokens
stems = [lancaster.stem(t) for t in tokens]  # replace lancaster with porter here
print stems[:100]

# <markdowncell>
# Notice that both stemmers handle some things rather poorly. The main reason for this is that they are not aware of the *word class* of any particular word: *nothing* is a noun, and nouns ending in *ing* should not have *ing* removed by the stemmer (swing, bling, ring...). Later in the course, we'll start annotating corpora with grammatical information. This improves the accuracy of stemmers a lot.

# > Note: stemming is not *always* the best thing to do: though *thing* is the stem of *things*, things has a unique meaning, as in *things will improve*. If we are interested in vague language, we may not want to collapse things --> thing.

# <headingcell level=2>
# Keywording: 'the aboutness of a text'

# <markdowncell>
# Keywording is the process of generating a list of words that are unusually frequent in the corpus of interest. To do it, you need a *reference corpus*, or at least a *reference wordlist* to which your *target corpus* can be compared. Often, *reference corpora* take the form of very large collections of language drawn from a variety of spoken and written sources.

# Keywording is what generates word-clouds beside online news stories, blog posts, and the like. In combination with speech-to-text, it's used in Oxford University's [Spindle Project](http://openspires.oucs.ox.ac.uk/spindle/) to automatically archive recorded lectures with useful tags.

# In fact, the keywording part of the Spindle Project is written in Python, and in open source.

# Spindle has sensible defaults for keyword calculation. Let's download their code and use it to generate keywords from our corpus.

# <codecell>
import sys
 # download spindle from github
!wget https://github.com/sgrau/spindle-code/archive/master.zip
!unzip master.zip # unzip it
!rm master.zip # remove the zip file
# put the keyworder directory in python's path, so we can call it easily
sys.path.insert(0, 'spindle-code-master/keywords')
# import the function
from keywords import keywords_and_ngrams # import keywords function

# <codecell>
# this tool works with raw text, not tokens!
keywords_and_ngrams(raw.encode("UTF-8"), nBigrams = 0)

# <markdowncell>
# Success! We have keywords.

# > Keep in mind, the BNC reference corpus was created before ISIS and ISIL existed. *Moslem/moslems* is a dispreferred spelling of Muslim, used more frequently in anti-Islamic discourse. Also, it's unlikely that a transcriber of the spoken BNC would choose the Moslem spelling. *Having an inappropriate reference corpus is a common methodological problem in discourse analytic work*.

# Our keywords would perhaps be better if they were stemmed. That shouldn't be too hard for us:

# <codecell>
keywords_and_ngrams(stems, nBigrams = 0) # this will use our corpus of stems, as defined earlier.

# <markdowncell>
# Rats! Keywording with stems actually revealed a list of incorrect stems.

# What re really need to do is improve our stemmer, and then come back and try again.

# <headingcell level=2>
# A return to stemming

# <markdowncell>
# Keywords and ngram searches actually work by comparing a corpus to a reference corpus. In our case, we have been using a dictionary of words in the 100 million word *British National Corpus*. We could use this same dictionary to make sure our stemmer does not create non-words when it stems.

# First, let's get a list of common words in the BNC from the *pickle* provided by SPINDLE (*pickle* is a kind of list compression).

# <codecell>
import pickle
import os
# unpack the pickled list
bncwordlist = pickle.load(open('spindle-code-master/keywords/bnc.p', 'rb')) 
bnc_commonwords = [] # empty list
for word in bncwordlist:
    getval = bncwordlist[word] # find out number of occurrences of word
    if getval > 20: # if more than 20
        bnc_commonwords.append(word) # add to common word list
print bnc_commonwords[:200] # what are our results?

# <markdowncell>
# So, this gives us a list of any word appearing more than twenty times in the BNC. We could build this function into our stemmer:

# <codecell>
# Now, let's use this as the dict for our stemmer
# The third variable sets a default threshold, but also allows us to enter one.
def newstemmer(words, stemmer, threshold = 20):
    """A stemmer that uses Lancaster/porter stemmer plus a dictionary."""
    import pickle
    import os
    import nltk
    bncwordlist = pickle.load(open('spindle-code-master/keywords/bnc.p', 'rb'))
    bnc_commonwords = {k for (k,v) in bncwordlist.iteritems() if v > threshold}
    # if words is a raw string, tokenise it
    if type(words) == unicode or type(words) == string:
        tokens = nltk.word_tokenize(words)
    # or, if list of tokens, duplicate the list
    else:
        tokens = words
        # define stemmer based on the argument we passed in
    if stemmer == 'Lancaster':
        stemmertouse = nltk.LancasterStemmer()
    if stemmer == 'Porter':
        stemmertouse = nltk.PorterStemmer()
    # empty list of stems
    stems = []
    for w in tokens:
        # stem each word
        stem = stemmertouse.stem(w)
        # if the stem is in the bnc list
        if stem in bnc_commonwords:
            # add the stem
            stems.append(stem)
        else:
            # or else, just add the word as it was
            stems.append(w)
    return stems

# <markdowncell>
# Now, we can fiddle with the stemmer and BNC frequency to get different keyword lists.

# <codecell>
# try raising the threshold if there are still bad spellings!
stemmed = newstemmer(raw, 'Lancaster', 10)

# <codecell>
keys = keywords_and_ngrams(stemmed)
keys[0] # only keywords
keys[1] # only n-grams

# <headingcell level=2>
# Collocation

# <markdowncell>
# > *You shall know a word by the company it keeps.* - J.R. Firth, 1957

# Collocation is a very common area of interest in corpus linguistics. Words pattern together in both expected and unexpected ways. In some contexts, *drug* and *medication* are synonymous, but it would be very rare to hear about *illicit* or *street medication*. Similarly, doctors are unlikely to prescribe the *correct* or *appropriate drug*.

# This kind of information may be useful to lexicographers, discourse analysts, or advanced language learners.

# In NLTK, collocation works from ordered lists of tokens. Let's put out tokenised sents into a single, huge list of tokens:

# <codecell>
allwords = []
# for each sentence,
for sent in tokenized_sents:
    # for each word,
    for word in sent:
        # make a list of all words
        allwords.append(word)
print allwords[:20]
# small challenge: can you think of any other ways to do this?

# <markdowncell>
# Now, let's feed these to an NLTK function for measuring collocations:

# <codecell>
# get all the functions needed for collocation work
from nltk.collocations import *
# define statistical tests for bigrams
bigram_measures = nltk.collocations.BigramAssocMeasures()
# go and find bigrams
finder = BigramCollocationFinder.from_words(allwords)
# measure which bigrams are important and print the top 30
sorted(finder.nbest(bigram_measures.raw_freq, 30))

# <markdowncell>
# So, that tells us a little: we can see that terrorists, Muslims and the Middle East are commonly collocating in the text. At present, we are only looking for immediately adjacent words. So, let's expand out search to a window of *five words either side*

# ''window size'' specifies the distance at which 
# two tokens can still be considered collocates
finder = BigramCollocationFinder.from_words(allwords, window_size=5)
sorted(finder.nbest(bigram_measures.raw_freq, 30))

# <markdowncell>
# Now we have the appearance of very common words! Let's use NLTK's stopwords list to remove entries containing these:

# <codecell>
finder = BigramCollocationFinder.from_words(allwords, window_size=5)
# get a list of stopwords from nltk
ignored_words = nltk.corpus.stopwords.words('english')
# make sure no part of the bigram is in stopwords
finder.apply_word_filter(lambda w: len(w) < 2 or w.lower() in ignored_words)
finder.apply_freq_filter(2)
#print the sorted collocations
sorted(finder.nbest(bigram_measures.raw_freq, 30))

# <markdowncell>
# There! Now we have some interesting collocates. Finally, let's remove punctuation-only entries, or entries that are *n't*, as this is caused by different tokenisers:

# <codecell>
finder = BigramCollocationFinder.from_words(allwords, window_size=5)
ignored_words = nltk.corpus.stopwords.words('english')
# anything containing letter or number
regex = r'[A-Za-z0-9]'
# the n't token
nonot = r'n\'t'
# lots of conditions!
finder.apply_word_filter(lambda w: len(w) < 2 or w.lower() in ignored_words or not re.match(regex, w) or re.match(nonot, w))
finder.apply_freq_filter(2)
sorted(finder.nbest(bigram_measures.raw_freq, 30))

# <markdowncell>
# You can get a lot more info on collocation at the [NLTK homepage](http://www.nltk.org/howto/collocations.html).

# <headingcell level=2>
# Clustering/n-grams

# <markdowncell>
# Clustering is the task of finding words that are commonly **immediately** adjacent (as opposed to collocates, which may just be nearby). This is also often called n-grams: bigrams are two tokens that appear together, trigrams are three, etc.

# Clusters/n-grams have a spooky ability to tell us what a text is about.

# We can use *Spindle* for bigram searching as well:

# <codecell>
# an argument here to stop keywords from being produced.
keywords_and_ngrams(raw.encode("UTF-8"), nKeywords=0)

# <markdowncell>
# There's also a method for n-gram production in NLTK. We can use this to understand how n-gramming works.

# Below, we get lists of any ten adjacent tokens:

# <codecell>
from nltk.util import ngrams
# define a sentence
sentence = 'give a man a fish and you feed him for a day; teach a man to fish and you feed him for a lifetime'
# length of ngram
n = 10
# use builtin tokeniser (but we could use a different one)
tengrams = ngrams(sentence.split(), n)
for gram in tengrams:
  print gram

# <markdowncell>
# So, there are plenty of tengrams in there! What we're interested in, however, is duplicated n-grams:

# <codecell>
# arguments: a text, ngram size, and minimum occurrences
def ngrammer(text, gramsize, threshold = 4):
    """Get any repeating ngram containing gramsize tokens"""
    # we need to import this in order to find the duplicates:
    from collections import defaultdict
    from nltk.util import ngrams
    # a subdefinition to get duplicate lists in a list
    def list_duplicates(seq):
        tally = defaultdict(list)
        for i,item in enumerate(seq):
            tally[item].append(i)
            # return to us the index and the ngram itself:
        return ((len(locs),key) for key,locs in tally.items() 
               if len(locs) > threshold)
    # get ngrams of gramsize    
    raw_grams = ngrams(text.split(), gramsize)
    # use our duplication detector to find duplicates
    dupes = list_duplicates(raw_grams)
    # return them, sorted by most frequent
    return sorted(dupes, reverse = True)

# <markdowncell>
# Now that it's defined, let's run it, looking for trigrams

# <codecell>
ngrammer(raw, 3)

# <markdowncell>
# Too many results? Let's set a higher threshold than the default.

# <codecell>
ngrammer(raw, 3, threshold = 10)

# <headingcell level=2>
# Concordancing with regular expressions

# <markdowncell>
# We've already done a bit of concordancing. In discourse-analytic research, concordancing is often used to perform thematic categorisation.

# <codecell>
text = nltk.Text(tokens)  # formats our tokens for concordancing
text.concordance("muslims")

# <markdowncell>
# We could even our stemmed corpus here:
text = nltk.Text(stemmed)
text.concordance("muslims")

# <markdowncell>
# You get no matches in the latter case, because all instances of *muslims* were stemmed to *muslim*.

# A problem with the NLTK concordancer is that it only works with individual tokens. What if we want to find words that end with **ment*, or words beginning with *poli**?

# We already searched text with Regular Expressions. It's not much more work to build regex functionality into our own concordancer.

# From running the code below, you can see that bracketting sections of our regex causes results to split into lists:

# <codecell>
# define a regex for different aussie words
aussie = r'(aussie|australia)'
searchpattern = re.compile(r"(.*)" + aussie + r"(.*)")
search = re.findall(searchpattern, raw)
search[:5]

# <markdowncell>
# Well, it's ugly, but it works. We can see five bracketted results, each containing three strings. The first and third strings are the left-context and right-context. The second of the three strings is the search term.

# These three sections are, with a bit of tweaking, the same as the output given by a concordancer.

# Let's go ahead and turn our regex seacher into a concordancer:

# <codecell>
def concordancer(text, regex):
    """Concordance using regular expressions"""
    import re
    # limit context to 30 characters max
    searchpattern = re.compile(r"(.{,30})(\b" + regex + r"\b)(.{,30})")
    # find all instances of our regex
    search = re.findall(searchpattern, raw)
    for result in search:
        #join each result with a tab, and print
        print("\t".join(result).expandtabs(20))
        # expand tabs helps align results

# <codecell>
concordancer(raw, r'aus.*?')

# <markdowncell>
# Great! With six lines of code, we've officially created a function that improves on the one provided by NLTK! And think how easy it would be to add more functionality: an argument dictating the size of the window (currently 30 characters), or printing line numbers beside matches, would be pretty easy to add, as well.

# > Adding too much functionality is known as *feature creep*. It's often best to keep your functions simple and more varied. An old adage in programming is to *make each program do one thing well*.

# <markdowncell>
# In the cells below, try concordancing a few things. Also try creating variables with concordance results, and then manipulate the lists. If you encounter problems with the way the concordancer runs, alter the function and redefine it. If you want, try implementing the window size variable!

# > **Tip:** If you wanted to get really creative, you could try stemming concordance or n-gram results!

# <codecell>
#
# <codecell>
#
# <codecell>
#
# <codecell>
#
# <codecell>
#

# <headingcell level=2>
# Summary

# <markdowncell>
# That's the end of session three! Great work.

# So, some of these tasks are a little dry---seeing results as lists of words and scores isn't always a lot of fun. But ultimately, they're pretty important things to know if you want to avoid the 'black box approach', where you simply dump words into a machine and analyse what the machine spits out.

# Remember that almost every task in corpus linguistics/distance reading depends on how we segment our data into sentences, clauses, words, etc.

# Building a stemmer from scratch taught us how to use regular expressions, and their power. But, we also saw that they weren't perfect for the task. In later lessons, we'll use more advanced methods to normalise our data. 

# *See you tomorrow!*

# <headingcell level=1>
# Bibliography

# <markdowncell>
# <a id="ref:baker"></a>
# Baker, P., Gabrielatos, C., Khosravinik, M., Krzyzanowski, M., McEnery, T., & Wodak, R. (2008). A useful methodological synergy? Combining critical discourse analysis and corpus linguistics to examine discourses of refugees and asylum seekers in the UK press. Discourse & Society, 19(3), 273-306.
#
# <a id="firth"></a>
# Firth, J. (1957).  *A Synopsis of Linguistic Theory 1930-1955*. In: Studies in Linguistic Analysis, Philological Society, Oxford; reprinted in Palmer, F. (ed.) 1968 Selected Papers of J. R. Firth, Longman, Harlow.
#
# <a id="ref:hymes"></a>
# Hymes, D. (1972). On communicative competence. In J. Pride & J. Holmes (Eds.), Sociolinguistics (pp. 269-293). Harmondsworth: Penguin Books. Retrieved from [http://humanidades.uprrp.edu/smjeg/reserva/Estudios%20Hispanicos/espa3246/Prof%20Sunny%20Cabrera/ESPA%203246%20-%20On%20Communicative%20Competence%20p%2053-73.pdf](http://humanidades.uprrp.edu/smjeg/reserva/Estudios%20Hispanicos/espa3246/Prof%20Sunny%20Cabrera/ESPA%203246%20-%20On%20Communicative%20Competence%20p%2053-73.pdf)
#
# <a id="ref:widdowson"></a>
# Widdowson, H. G. (2000). On the limitations of linguistics applied. Applied Linguistics, 21(1), 3. Available at [http://applij.oxfordjournals.org/content/21/1/3.short](http://applij.oxfordjournals.org/content/21/1/3.short).

# <headingcell level=3>
# Workspace

# <markdowncell>
# Here are a few blank cells, in case you need them for anything:

# <codecell>
# 
# <codecell>
#
# <codecell>
#
# <codecell>
#
# <codecell>
#
# <codecell>
#
# <codecell>
#
# <codecell>
#
# <codecell>
#
# <codecell>
#
# <codecell>
# 
