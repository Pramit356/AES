from nltk import pos_tag, wordnet as wn
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize

lemma = wn.WordNetLemmatizer()
print(lemma.lemmatize("is", pos = "v"))
print(lemma.lemmatize("am", pos = "v"))
print(lemma.lemmatize("are", pos = "v"))
print(lemma.lemmatize("been", pos = "v"))