from gensim.models import Word2Vec
import sys
print sys.path
import nltk
from urllib import urlopen # a library for working with urls
url = "https://raw.githubusercontent.com/resbaz/lessons/master/nltk/corpora/oz_politics/ozpol.txt" # define the url
raw = urlopen(url).read() # download and read the corpus into raw variable
raw = unicode(raw.lower(), 'utf-8') # make it lowercase and unicode
len(raw) # how many characters does it contain?
raw[:2000] # first 2000 characters
sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
sents = sent_tokenizer.tokenize(raw)
tokenized_sents = [nltk.word_tokenize(i) for i in sents]
model = Word2Vec(tokenized_sents)
model.most_similar('money', topn=5)