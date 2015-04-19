# <markdowncell>
# <br>
# <img style="float:left" src="http://ipython.org/_static/IPy_header.png" />
# <br>

# <headingcell level=1>
# Session 4: The Fraser Speech Corpus

# <markdowncell>
# **Welcome back!**

# So, what did we learn yesterday? A brief recap:

# * The **IPython** Notebook
# * **Python**: syntax, variables, functions, etc.
# * **NLTK**: manipulating linguistic data
# * **Corpus linguistic tasks**: tokenisation, keywords, collocation, stemming, concordances

# Today's focus will be on **developing more advanced NLTK skills** and using these skills to **investigate the Fraser Speeches Corpus**. In the final session, we will discuss **how to use what you have learned here in your own research**.

# *Any questions or anything before we dive in?*

# <headingcell level=2>
# Malcolm Fraser and his speeches

# <markdowncell>
# So, for much of the next two sessions, we are going to be working with a corpus of speeches made by Malcolm Fraser. 

# <codecell>
# this code allows us to display images and webpages in our notebook
from IPython.display import display
from IPython.display import display_pretty, display_html, display_jpeg, display_png, display_svg
from IPython.display import Image
from IPython.display import HTML
import nltk

# <codecell>
Image(url='http://www.unimelb.edu.au/malcolmfraser/photographs/family/105~36fam6p9.jpg')

# <markdowncell>
# Because our project here is *corpus driven*, we don't necessarily need to know about Malcolm Fraser and his speeches in order to analyse the data: we may be happy to let things emerge from the data themselves. Even so, it's nice to know a bit about him.

# Malcolm Fraser was a member of Australian parliament between 1955 and 1983, holding the seat of Wannon in western Victoria. He held a number of ministries, including Education and Science, and Defence. 

# He became leader of the Liberal Party in March 1975 and Prime Minister of Australia in December 1975, following the dismissal of the Whitlam government in November 1975.

# He retired from parliament following the defeat of the Liberal party at the 1983 election and in 2009 resigned from the Liberal party after becoming increasingly critical of some of its policies.

# He can now be found on Twitter as **@MalcolmFraser12**

# <codecell>
HTML('<iframe src=http://en.wikipedia.org/wiki/Malcolm_Fraser width=700 height=350></iframe>')

# <markdowncell>
# In 2004, Malcolm Fraser made the University of Melbourne the official custodian of his personal papers. The collection consists of a large number of photographs, speeches and personal papers, including Neville Fraser's WWI diaries and materials relating to CARE Australia, which Mr Fraser helped to found in 1987. 

# <codecell>
HTML('<iframe src=http://www.unimelb.edu.au/malcolmfraser/ width=700 height=350></iframe>')

# <markdowncell>
# Every week, between 1954 until 1983, Malcolm Fraser made a talk to his electorate that was broadcast on Sunday evening on local radio.  

# The speeches were transcribed years ago. Optical Character Recognition (OCR) was used to digitise the transcripts. This means that the texts are not of perfect quality. 

# Some have been manually corrected, which has removed extraneous characters and mangled words, but even so there are still some quirks in the formatting. 

# For much of this session, we are going to manipulate the corpus data, and use the data to restructure the corpus. 

# <headingcell level=2>
# Cleaning the corpus

# <markdowncell>
# A common part of corpus building is corpus cleaning. Reasons for cleaning include:

# 1. Not break the code with unexpected input
# 2. Ensure that searches match as many examples as possible
# 3. Increasing readability, the accuracy of taggers, stemmers, parsers, etc.

# The level of kind of cleaning depends on your data and the aims of your project. In the case of very clean data (lucky you!), there may be little that needs to be done. With messy data, you may need to go as far as to correct variant spellings (online conversation, very old books).

# <headingcell level=3>
# Discussion

# <markdowncell>
# *What are the characteristics of clean and messy data? Any personal experiences? Discuss with your neighbours.* 

# It will be important to bear these characteristics in mind once you start building your own datasets and corpora.

# <headingcell level=3>
# OK, let's code!

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
# # Charting change in Fraser's speeches

# Before we get started, we have to install Java, as some of our tools rely on some Java code. You'll very likely have Java installed on your local machine, but we need it on the cloud. To make it work, you should run the following line of code in the cloud Terminal:

# <codecell>
! yum -y install java
# ! pip install corpkit 

# <headingcell level=3>
# Interrogating the corpus

# <markdowncell>
# To interrogate the corpus, we need a crash course in **syntax trees** and **Tregex queries**. Let's define a tree (from the Fraser Corpus, 1956), and have a look at its visual representation.

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

# <codecell>
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
# # Some linguistics...

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

# With this in mind, let's search the corpus for *interpersonal* and *experiential* change in Fraser's language.

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
# # Cheatsheet

# <br>
# <img style="float:left" src="https://raw.githubusercontent.com/resbaz/nltk/master/resources/images/options.png" />
# <br>
#
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

