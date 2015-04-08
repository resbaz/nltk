
# <markdowncell>
# <br>
# <img style="float:left" src="http://ipython.org/_static/IPy_header.png" />
# <br>


# <headingcell level=1>
# Session 3: Charting change in Fraser's speeches

# <markdowncell>
#
# In this lesson, we investigate a fully-parsed version of the Fraser Corpus. We do this using purpose-built tools.

# In the first part of the session, we will go through how to use each of the tools. Later, you'll be able to use the tools to navigate the data and visualise results in any way you like.

# The Fraser Speeches have been parsed for part of speech and grammatical structure by [*Stanford CoreNLP*](http://nlp.stanford.edu/software/corenlp.shtml), a parser that can be loaded within NLTK. We rely on [*Tregex*](http://nlp.stanford.edu/~manning/courses/ling289/Tregex.html) to interrogate the parse trees. Tregex allows very complex searching of parsed trees, in combination with [Java Regular Expressions](http://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html), which are very similar to the regexes we've been using thus far.

# If you plan to work more with parsed corpora later, it's definitely worthwhile to learn the Tregex syntax in detail. For now, though, we'll use simple queries, and explain the query construction syntax as we go.

# Before we get started, we have to install Java, as some of our tools rely on some Java code. You'll very likely have Java installed on your local machine, but we need it on the cloud. To make it work, you should run the following line of code in the cloud Terminal:

#      sudo yum install java

# <markdowncell>
# OK, that's out of the way. Next, let's import the functions we'll be using to investigate the corpus. These functions have been designed specifically for our investigation, but they will work with any parsed dataset.

# We'll take a look at the code used in this session a little later on, if there's time. Much of the code is derived from things we've learned here, combined with a lot of Google and Stack Overflow searching. All our code is on GitHub too, remember. It's open-source, so you can do whatever you like with it.

# Here's an overview of the functions we'll be using, and their purpose:

# | **Function name** | Purpose                            | |
# | ----------------- | ---------------------------------- | |
# | *searchtree()*  | find things in a parse tree         | |
# | *interrogator()*  | interrogate parsed corpora         | |
# | *plotter()*       | visualise *interrogator()* results | |
# | *quickview()*     | view *interrogator()* results      | |
# | *tally()*       | get total frequencies for *interrogator()* results      | |
# | *surgeon()*       | edit *interrogator()* results      | |
# | *merger()*       | merge *interrogator()* results      | |
# | *conc()*          | complex concordancing of subcopora | |

# We can import them using IPython Magic:

# <codecell>
import os # for joining paths
from IPython.display import display, clear_output # for clearing huge lists of output
# import functions to be used here:
%run corpling_tools/interrogator.ipy
%run corpling_tools/resbazplotter.ipy
%run corpling_tools/additional_tools.ipy

# <markdowncell>
# We also need to set the path to our corpus as a variable. If you were using this interface for your own corpora, you would change this to the path to your data.

# <codecell>
path = 'corpora/fraser-corpus-annotated' # path to corpora from our current working directory.

# <headingcell level=3>
# Interrogating the corpus

# <markdowncell>
# To interrogate the corpus, we need a crash course in parse labels and Tregex syntax. Let's define a tree (from the Fraser Corpus, 1956), and have a look at its visual representation.

#      Melbourne has been transformed over the let 18 months in preparation for the visitors.

# <codecell>
melbtree = (r'(ROOT (S (NP (NNP Melbourne)) (VP (VBZ has) (VP (VBN been) (VP (VBN transformed) '
           r'(PP (IN over) (NP (NP (DT the) (VBN let) (CD 18) (NNS months)) (PP (IN in) (NP (NP (NN preparation)) '
           r'(PP (IN for) (NP (DT the) (NNS visitors)))))))))) (. .)))')

# <markdowncell>
# Notice that an OCR error caused a parsing error. Oh well. Here's a visual representation, drawn with NLTK:

# <br>
# <img style="float:left" src="https://raw.githubusercontent.com/resbaz/lessons/master/nltk/images/melbtree.png" />
# <br>
# <markdowncell>
# The data is annotated at word, phrase and clause level. Embedded here is an elaboration of the meanings of tags *(ask Daniel if you need some clarification!)*:

# <codecell>
HTML('<iframe src=http://www.surdeanu.info/mihai/teaching/ista555-fall13/readings/PennTreebankConstituents.html width=700 height=350></iframe>')

# <markdowncell>
# Note that the tags are a little bit different from the last parser we were using:

# <codecell>
quicktree("Melbourne has been transformed over the let 18 months in preparation for the visitors")

# <markdowncell>
# Neither parse is perfect, but the one we just generated has a major flaw: *Melbourne* is parsed as an adverb! Stanford CoreNLP correctly identifies it as a proper noun, and also, did a better job of handling the 'let' mistake.

# <markdowncell>
# *searchtree()* is a tiny function that searches a syntax tree. We'll use the sample sentence and *searchtree()* to practice our Tregex queries. We can feed it either *tags* (S, NP, VBZ, DT, etc.) or *tokens* enclosed in forward slashes.

# <codecell>
# any plural noun
query = r'NNS'
searchtree(melbtree, query)

# <codecell>
# A token matching the regex *Melb.?\**
query = r'/Melb.?/'
searchtree(melbtree, query)

# <codecell>
query = r'NP'
searchtree(melbtree, query)

# <markdowncell>
# To make things more specific, we can create queries with multiple criteria to match, and specify the relationship between each criterion we want to match. Tregex will print everything matching **the leftmost criterion**.

# <codecell>
# NP with 18 as a descendent
query = r'NP << /18/'
searchtree(melbtree, query)

# <markdowncell>
# Using an exclamation mark negates the relationship. Try producing a query for a *noun phrase* (NP) without a *Melb* descendent:

# <codecell>
query = r'NP !<< /Melb.?/'
searchtree(melbtree, query)

# <markdowncell>
# The dollar specifies a sibling relationship between two parts of the tree---that is, two words or tags that are horizontally aligned.

# <codecell>
# NP with a sister VP
# This corresponds to 'subject' in many grammars
query = r'NP $ VP'
searchtree(melbtree, query)

# <markdowncell>
# Try changing the **more than** symbols to **less than**, and see how it affects the results.

# <codecell>
# Prepositional phrase in other prepositional phrases
query = r'PP >> PP'
searchtree(melbtree, query)

# <markdowncell>
# There is also a double underscore, which functions as a wildcard.

# <codecell>
# anything with any kind of noun tag
query = r'__ > /NN.?/'
searchtree(melbtree, query)

# <markdowncell>
# Using brackets, it's possible to create very verbose queries, though this goes well beyond our scope. Just know that it can be done!

# <codecell>
# particle verb in verb phrase with np sister headed by Melb.
# the particle verb must also be in a verb phrase with a child preposition phrase
# and this child preposition phrase must be headed by the preposition 'over'.
query = r'VBN >> (VP $ (NP <<# /Melb.?/)) > (VP < (PP <<# (IN < /over/)))'
searchtree(melbtree, query)

# <markdowncell>
# Here are two more trees for you to query, from 1969 and 1973.

#      We continue to place a high value on economic aid through the Colombo Plan, involving considerable aid to Asian students in Australia.

# <markdowncell>
# <br>
# <img style="float:left" src="https://raw.githubusercontent.com/resbaz/lessons/master/nltk/images/colombotree.png" />
# <br>

# <codecell>
colombotree = r'(ROOT (S (NP (PRP We)) (VP (VBP continue) (S (VP (TO to) (VP (VB place) (NP (NP (DT a) (JJ high) '
    r'(NN value)) (PP (IN on) (NP (JJ economic) (NN aid)))) (PP (IN through) (NP (DT the) (NNP Colombo) (NNP Plan))) '
    r'(, ,) (S (VP (VBG involving) (NP (JJ considerable) (NN aid)) (PP (TO to) (NP (NP (JJ Asian) (NNS students)) 
        r'(PP (IN in) (NP (NNP Australia))))))))))) (. .)))'

# <markdowncell>
#      As a result, wool industry and the research bodies are in a state of wonder and doubt about the future.

# <markdowncell>
# <br>
# <img style="float:left" src="https://raw.githubusercontent.com/resbaz/lessons/master/nltk/images/wooltree.png" />
# <br>

# <codecell>
wooltree = r'(ROOT (S (PP (IN As) (NP (DT a) (NN result))) (, ,) (NP (NP (NN wool) (NN industry)) (CC and) '
                 r'(NP (DT the) (NN research) (NNS bodies))) (VP (VBP are) (PP (IN in) (NP (NP (DT a) (NN state)) '
                    r'(PP (IN of) (NP (NN wonder) (CC and) (NN doubt))))) (PP (IN about) (NP (DT the) (NN future)))) (. .)))'

# <markdowncell>
# Try a few queries in the cells below.

# > If you need help constructing a Tregex query, ask Daniel. He writes them all day long for fun.

# <codecell>
query = '?'
searchtree(colombotree, query)

# <codecell>
# 

# <codecell>
#

# <codecell>
#

# <markdowncell>
# So, now we understand the basics of a Tregex query (don't worry---many queries have already been written for you. We can start our investigation of the Fraser Corpus by generating some general information about it. First, let's define a query to find every word in the corpus. Run the cell below to define the *allwords_query* as the Tregex query.

# > *When writing Tregex queries or Regular Expressions, remember to always use **r'...'** quotes!*

# <codecell>
# any token containing letters or numbers (i.e. no punctuation):
# we specify here that it cannot have any descendants,
# just to be sure we only get tokens, not tags.
allwords_query = r'/[A-Za-z0-9]/ !< __' 

# <markdowncell>
# Next, we perform interrogations with *interrogator()*. Its most important arguments are:
#
# 1. **path to corpus** (the *path* variable)
#
# 2. Tregex **options**:
#   * **'-t'**: return only words
#   * **'-C'**: return a count of matches
#
# 3. the **Tregex query**

# We only need to count tokens, so we can use the **-C** option (it's often faster than getting lists of matching tokens). The cell below will run *interrogator()* over each annual subcorpus and count the number of matches for the query.

# <codecell>
allwords = interrogator(path, '-C', allwords_query) 

# <markdowncell>
# When the interrogation has finished, we can view the total counts by getting the *totals* branch of the *allwords* interrogation:

# <codecell>
# from the allwords results, print the totals
print allwords.totals

# <markdowncell>
# If you want to see the query and options that created the results, you can print the *query* branch.

# <codecell>
print allwords.query

# <headingcell level=3>
# Plotting results

# <markdowncell>
# Lists of years and totals are pretty dry. Luckily, we can use the *plotter()* function to visualise our results. At minimum, *plotter()* needs two arguments:

# 1. a title (in quotation marks)
# 2. a list of results to plot

# <codecell>
plotter('Word counts in each subcorpus', allwords.totals)

# <markdowncell>
# Great! So, we can see that the number of words per year varies quite a lot. That's worth keeping in mind.

# Next, let's plot something more specific, using the **-t** option.

# <codecell>
query = r'/(?i)\baustral.?/' # australia, australian, australians, etc.
aust = interrogator(path, '-t', query) # -t option to get matching words, not just count

# <markdowncell>
# We now have a list of words matching the query stores in the *aust* variable's *results* branch:

# <codecell>
aust.results[:3] # just the first few entries

# <markdowncell>
# *Your turn!* Try this exercise again with a different term. 

# <markdowncell>
# We can use a *fract_of* argument to plot our results as a percentage of something else. This helps us deal with the issue of different amounts of data per year.

# <codecell>
# as a percentage of all aust* words:
plotter('Austral*', aust.results, fract_of = aust.totals)
# as a percentage of all words (using our previous interrogation)
plotter('Austral*', aust.results, fract_of = allwords.totals)

# <markdowncell>
# Great! So, we now have a basic understanding of the *interrogator()* and *plotter()* functions.

# <headingcell level=3>
# Customising visualisations

# <markdowncell>
# By default, *plotter()* plots the absolute frequency of the seven most frequent results.

#  We can use other *plotter()* arguments to customise what our chart shows. *plotter()*'s possible arguments are:

#  | plotter() argument | Mandatory/default?       |  Use          | Type  |
#  | :------|:------- |:-------------|:-----|
#  | *title* | **mandatory**      | A title for your plot | string |
#  | *results* | **mandatory**      | the results you want to plot | *interrogator()* total |
#  | *fract_of* | None      | results for plotting relative frequencies/ratios etc. | list (interrogator(-C) form) |
#  | *num_to_plot* | 7     | number of top results to display     |   integer |
#  | *multiplier* | 100     | result * multiplier / total: use 1 for ratios | integer |
#  | *x_label* | False    | custom label for the x-axis     |  string |
#  | *y_label* | False    | custom label for the y-axis     |  string |
#  | *yearspan* | False    | plot a span of years |  a list of two int years |
#  | *justyears* | False    | plot specific years |  a list of int years |
#  | *csvmake* | False    | make csvmake the title of csv output file    |  string |

# You can easily use these to get different kinds of output. Try changing some parameters below:

# <codecell>
# maybe we want to get rid of all those non-words?
plotter('Austral*', aust.results, fract_of = allwords.totals, num_to_plot = 3, y_label = 'Percentage of all words')

# <codecell>
# or see only the 1960s?
plotter('Austral*', aust.results, fract_of = allwords.totals, num_to_plot = 3, yearspan = [1960,1969])

# <markdowncell>
# **Your Turn**: mess with these variables, and see what you can plot. Try using some really infrequent results, if you like!

# <codecell>
#

# <codecell>
#

# <headingcell level=3>
# Viewing and editing results

# <markdowncell>
# Aside from *interrogator()* and *plotter()*, there are also a few simple functions for viewing and editing results.

# <headingcell level=4>
# quickview()

# <markdowncell>
# *quickview()* is a function that quickly shows the n most frequent items in a list. Its arguments are:
#
# 1. an *interrogator()* result
# 2. number of results to show (default = 50)
#
# We can see the full glory of bad OCR here:

# <codecell>
quickview(aust.results, n = 20)

# <markdowncell>
# The number shown next to the item is its index. You can use this number to refer to an entry when editing results.

# <headingcell level=4>
# tally()

# <markdowncell>
# *tally()* displays the total occurrences of results. Its first argument is the list you want tallies from. For its second argument, you can use:

# * a list of indices for results you want to tally
# * a single integer, which will be interpreted as the index of the item you want
# * a string, 'all', which will tally every result. This could be very many results, so it may be worth limiting the number of items you pass to it with [:n],

# <codecell>
tally(aust.results, [0, 3])

# <markdowncell> 
# **Your turn**: Use 'all' to tally the result for the first 11 items in aust.results

# <codecell>
tally(aust.results[:10], 'all')


# <headingcell level=4>
# surgeon()

# <markdowncell>
# Results lists can be edited quickly with *surgeon()*. *surgeon()*'s arguments are:

# 1. an *interrogator()* results list
# 2. *criteria*: either a regex or a list of indices.
# 3. *remove = True/False*

# By default, *surgeon()* removes anything matching the regex/indices criteria, but this can be inverted with a *remove = False* argument. Because you are duplicating the original list, you don't have to worry about deleting *interrogator()* results.

# We can use it to remove some obvious non-words.

# <codecell>
non_words_removed = surgeon(aust.results, [5, 9], remove = True)
plotter('Some non-words removed', non_words_removed, fract_of = allwords.totals)

# <markdowncell>
# Note that you do not access surgeon lists with *aust.non_words_removed* syntax, but simply with *non_words_removed*.

# <headingcell level=4>
# merger()

# <markdowncell>
# *merger()* is for merging items in a list. Like *surgeon()*, it duplicates the old list. Its arguments are:

# 1. the list you want to modify
# 2. the indices of results you want to merge, or a regex to match
# 3. newname = *str/int/False*: 
#   * if string, the string becomes the merged item name.
#   * if integer, the merged entry takes the name of the item indexed with the integer.
#   * if not specified/False, the most most frequent item in the list becomes the name.

# In our case, we might want to collapse *Australian* and *Australians*, because the latter is simply the plural of the former.

# <codecell>
# before:
plotter('Before merging Australian and Australians', aust.results, num_to_plot = 3)
# after:
merged = merger(aust.results, [1, 2],  newname = 'australian(s)')
plotter('After merging Australian and Australians', merged, num_to_plot = 2)

# <headingcell level=4>
# conc()

# <markdowncell>
# The final function is *conc()*, which produces concordances of a subcorpus based on a Tregex query. Its main arguments are:

# 1. A subcorpus to search *(remember to put it in quotation marks!)*
# 2. A Tregex query

# <codecell>
# here, we use a subcorpus of politics articles,
# rather than the total annual editions.
conc(os.path.join(path,'1966'), r'/(?i)\baustral.?/') # adj containing a risk word

# <markdowncell>
# You can set *conc()* to print *n* random concordances with the *random = n* parameter. You can also store the output to a variable for further searching.

# <codecell>
randoms = conc(os.path.join(path,'1963'), r'/(?i)\baustral.?/', random = 5)
randoms

# <markdowncell>
# *conc()* takes another argument, window, which alters the amount of co-text appearing either side of the match.

# <codecell>
conc(os.path.join(path,'1981'), r'/(?i)\baustral.?/', random = 5, window = 50)

# <markdowncell>
# *conc()* also allows you to view parse trees. By default, it's false:

# <codecell>
conc(os.path.join(path,'1954'), r'/(?i)\baustral.?/', random = 5, window = 30, trees = True)

# Now you're familiar with the corpus and functions, it's time to explore the corpus in a more structured way. To do this, we need a little bit of linguistic knowledge, however.

# <headingcell level=3>
# Some linguistics...

# <markdowncell>
# *Functional linguistics* is a research area concerned with how *realised language* (lexis and grammar) work to achieve meaningful social functions.

# One functional linguistic theory is *Systemic Functional Linguistics*, developed by Michael Halliday (Prof. Emeritus at University of Sydney).

# Central to the theory is a division between **experiential meanings** and **interpersonal meanings**.

# * Experiential meanings communicate what happened to whom, under what circumstances.
# * Interpersonal meanings negotiate identities and role relationships between speakers 

# Halliday argues that these two kinds of meaning are realised **simultaneously** through different parts of English grammar.

# * Experiential meanings are made through **transitivity choices**.
# * Interpersonal meanings are made through **mood choices**

# Here's one visualisation of it. We're concerned with the two left-hand columns. Each level is an abstraction of the one below it.

# <br>
# <img style="float:left" src="https://raw.githubusercontent.com/interrogator/sfl_corpling/master/cmc-2014/images/egginsfixed.jpg" />
# <br>

# Transitivity choices include fitting together configurations of:

# * Participants (*a man, green bikes*)
# * Processes (*sleep, has always been, is considering*)
# * Circumstances (*on the weekend*, *in Australia*)

# Mood features of a language include:

# * Mood types (*declarative, interrogative, imperative*)
# * Modality (*would, can, might*)
# * Lexical density---the number of words per clause, the number of content to non-content words, etc.

# Lexical density is usually a good indicator of the general tone of texts. The language of academia, for example, often has a huge number of nouns to verbs. We can approximate an academic tone simply by making nominally dense clauses: 

#       The consideration of interest is the potential for a participant of a certain demographic to be in Group A or Group B*.

# Notice how not only are there many nouns (*consideration*, *interest*, *potential*, etc.), but that the verbs are very simple (*is*, *to be*).

# In comparison, informal speech is characterised by smaller clauses, and thus more verbs.

#       A: Did you feel like dropping by?
#       B: I thought I did, but now I don't think I want to

# Here, we have only a few, simple nouns (*you*, *I*), with more expressive verbs (*feel*, *dropping by*, *think*, *want*)

# > **Note**: SFL argues that through *grammatical metaphor*, one linguistic feature can stand in for another. *Would you please shut the door?* is an interrogative, but it functions as a command. *invitation* is a nominalisation of a process, *invite*. We don't have time to deal with these kinds of realisations, unfortunately.

# <headingcell level=3>
# Fraser's speeches and linguistic theory

# <markdowncell>
# So, from an SFL perspective, when Malcolm Fraser gives a speech, he is simultaneously making meaning about events in the real world (through transitivity choices) and about his role and identity (through mood and modality choices).

# With this basic theory of language, we can create two research questions:

# 1. **How does Malcolm Fraser's tone change over time?**
# 2. **What are the major things being spoken about in Fraser's speeches, and how do they change?**

# As our corpus is well-structured and parsed, we can create queries to answer these questions, and then visualise the results.

# <headingcell level=4>
# Interpersonal features

# <markdowncell>
# We'll start with interpersonal features of language in the corpus. First, we can devise a couple of simple metrics that can teach us about the interpersonal tone of Fraser's speeches over time. We don't have time to run all of these queries right now, but there should be some time later to explore the parts of this material that interest

# <codecell>
# number of content words per clause
openwords = r'/\b(JJ|NN|VB|RB)+.?\b/'
clauses = r'S < __'
opencount = interrogator(path, '-C', openwords)
clausecount = interrogator(path, '-C', clauses)

# <codecell>
plotter('Lexical density', opencount.totals, 
        fract_of = clausecount.totals, y_label = 'Lexical Density Score', multiplier = 1)

# <markdowncell>
# We can also look at the use of modals auxiliaries (*would could, may, etc.*) over time. This can be interesting, as modality is responsible for communicating certainty, probability, obligation, etc.

# Modals are very easily and accurately located, as there are only a few possible words, and they occur in predicable places within clauses.

# Most grammars tag them with 'MD'.

# If modality interests you, later, it could be a good set of results to manipulate and plot.

# <codecell>
query = r'MD < __'
modals = interrogator(path, '-t', query)
plotter('Modals', modals.results, fract_of = modals.totals)

# <codecell>
# percentage of tokens that are I/me
query = r'/PRP.?/ < /(?i)^(i|me|my)$/'
firstperson = interrogator(path, '-C', query)

# <codecell>
plotter('First person', firstperson.totals, fract_of = allwords.totals)

# <codecell>
# percentage of questions
query = r'ROOT <<- /.?\?.?/'
questions = interrogator(path, '-C', query)

# <codecell>
plotter('Questions/all clauses', questions.totals, fract_of = clausecount.totals)

# <codecell>
# ratio of open/closed class words
closedwords = r'/\b(DT|IN|CC|EX|W|MD|TO|PRP)+.?\b/'
closedcount = interrogator(path, '-C', closedwords)

# <codecell>
plotter('Open/closed word classes', opencount.totals, 
        fract_of = closedcount.totals, y_label = 'Open/closed ratio', multiplier = 1)

# <codecell>
# ratio of nouns/verbs
nouns = r'/NN.?/ < __'
verbs = r'/VB.?/ < __'
nouncount = interrogator(path, '-C', nouns)
verbcount = interrogator(path, '-C', verbs)

# <codecell>
plotter('Noun/verb ratio', nouncount.totals, fract_of = verbcount.totals, multiplier = 1)

# <headingcell level=4>
# Experiential features of Fraser's speech

# <markdowncell>
# We now turn our attention to what is being spoken about in the corpus. First, we can get the heads of grammatical participants:

# <codecell>
# heads of participants (heads of NPS not in prepositional phrases)
query = r'/NN.?/ >># (NP !> PP)'
participants = interrogator(path, '-t', query, lemmatise = True)

# <codecell>
plotter('Participants', participants.results, fract_of = allwords.totals)

# <markdowncell>
# Next, we can get the most common processes. That is, the rightmost verb in a verbal group (take a look at the visualised tree!)

# > *Be careful not to confuse grammatical labels (predicator, verb), with semantic labels (participant, process) ... *

# <codecell>
# most common processes
query = r'/VB.?/ >># VP >+(VP) VP'
processes = interrogator(path, '-t', query, lemmatise = True)

# <codecell>
plotter('Processes', processes.results[2:], fract_of = processes.totals)

# <markdowncell>
# It seems that the verb *believe* is a common process in 1973. Try to run *conc()* in the cell below to look at the way the word behaves.

# <codecell>
# write a call to conc() that gets concordances for r'/VB.?/ < /believe/ in 1973
# conc('fraser-corpus-annotated/1973', r'/VB.?/ < /believe/)
#

# <markdowncell>
# For discussion: what events are being discussed when *believe* is the process? Why use *believe* here?
# <br>

# Next, let's chart noun phrases headed by a proper noun (*the Prime Minister*, *Sydney*, *John Howard*, etc.). We can define them like this:

# <codecell>
# any noun phrase headed by a proper noun
pn_query = r'NP <# NNP'

# <markdowncell>
# To make for more accurate results the *interrogator()* function has an option, *titlefilter*, which uses a regular expression to strip determiners (*a*, *an*, *the*, etc.), titles (*Mr*, *Mrs*, *Dr*, etc.) and first names from the results. This will ensure that the results for *Prime Minister* also include *the Prime Minister*, and *Fraser* results will include the *Malcolm* variety. The option is turned on in the cell below:

# <codecell>
# Proper noun groups
propernouns = interrogator(path, '-t', pn_query, titlefilter = True)

# <codecell>
plotter('Proper noun groups', propernouns.results, fract_of = propernouns.totals, num_to_plot = 15)

# <markdowncell>
# Proper nouns are a really good category to investigate further, as it is through proper nouns that we can track discussion of particular people, places or things. So, let's look at the top 100 results:

# <codecell>
quickview(propernouns.results, n = 100)

# <markdowncell>
#  You can now use the *merger()* and *surgeon()* options to make new lists to plot. Here's one example: we'll use *merger()* to merge places in Victoria, and then *surgeon()* to create a list of places in Australia.

# <codecell>
merged = merger(propernouns.results, [9, 13, 27, 36, 78, 93], newname = 'places in victoria')
quickview(merged, n = 100)

ausparts = surgeon(merged, [7, 9, 23, 25, 33, 41, 49], remove = False)
plotter('Places in Australia', ausparts, fract_of = propernouns.totals)

# <markdowncell>
# Neat, eh? Well, that concludes the structured part of the lesson. You now have a bit of time to explore the corpus, using the tools provided. Below, for your convenience, is a table of the functions and their arguments.

# Particularly rewarding can be playing more with the proper nouns section, as in the cells above. Shout out if you find something interesting!

# <markdowncell>
# <br>
# <img style="float:left" src="https://raw.githubusercontent.com/resbaz/lessons/master/nltk/images/options.png" />
# <br>

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

# <markdowncell>
# By the way, here's the code behind some of the functions we've been using. With all your training, you can probably understand quite a bit of it!

# <codecell>
%load corpling_tools/additional_tools.ipy

# <markdowncell>
# That's it for this lesson, and for our interrogation of the Fraser Corpus. Remember that this is the first time anybody has conducted a sustained corpus linguistic investigation of this corpus. Everything we found here is a new discovery about the way language changes over time! (feel free to write it up and publish it!)

# The final session will look to the future: we hope to have a conversation about what you can do with the kind of skills you've learned here.

# *See you soon!*

