# Help for instructors and in NLTK workshops

> In this document, explanations for tricky/problematic parts of the NLTK sessions are given, as well as some basic troubleshooting.

## Problem: Missing NLTK data

Sometimes, things required on NLTK aren't found on students' notebooks.

Depending on how much time you have, you may want to download *all* NLTK data, or just the relevant parts.

**Note**: nltk.download() starts a small, short interactive session.  iPython does not allow for this.  To use in iPython use the formats like: `nltk.download('all')` as listed below. If you run nltk.download() in Python in the shell, you will get the interactive session.

To download all NLTK data, run `nltk.download('all')`, this can take up to 15 minutes.

Other parts of NLTK that are used in the course can be downloaded as follows:

```python
nltk.download('punkt') # word tokeniser
nltk.download('wordnet') # lemmatisation
nltk.download('stopwords') # lists of stopwords
nltk.download('brown') # the Brown corpus
```

## Problem: Functions behaving badly

At many points in the course, variables and functions defined by the class need to be reused. If a student's function is different from the 'planned' function, issues may arise.

If you can diagnose and fix the problem by modifying the source of the problem, that's awesome! In that case, explain to the student where he/she went wrong, and catch them up on whatever they've missed.

If you can't locate the source of the problem, you can import key functions used in the course directly into the student's notebook. These functions live in the `resources/scripts.py` file.

If, for example, a correct version of the `parse_metadata()` function is needed, you can simply run:

```python
from resources.scripts import parse_metadata as parse_metadata
```

The functions currently in `resources/scripts.py` are:

* `searchtree(tree, query)`
* `quicktree(sentence)`
* `parse_metadata(text)`
* `structure_corpus(oldpath, newpath)`
* `plot('Title', results, fract_of = totals)`

## Adding to this document

If you encounter an issue that you think needs documentation, please feel free to add to this file!
