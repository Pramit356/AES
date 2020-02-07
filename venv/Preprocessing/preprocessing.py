from spellcorrector import spellcheck_and_correct
from stopword_removal import remove_stopwords
from lemmatization import lemmatize , lemmatize1
from checkstructures import sentence_proportion, check_punctuations_capitalization
from grammar3 import check_grammatical_errors
import time
import pickle

start = time.time()
score = 100
f = open("Dictionary/input2.txt", "r", encoding="utf8")
txt = f.read()
f.close()
essay, score = spellcheck_and_correct(txt, score)
print("Score after spell check: ",score)
print("Essay after spell checking and correction: ",essay)

cleaned_essay, pos_list_punctuations, pos_list_grammar = remove_stopwords(essay, txt)
print("Essay after stopword removal: ", cleaned_essay)

print(pos_list_punctuations)


cleaned_essay = lemmatize(cleaned_essay)
print("Essay after lemmatization: ", cleaned_essay)


score = sentence_proportion(essay, score)
print("Score after sentence proportions: ", score)

score = check_punctuations_capitalization(pos_list_punctuations, score)
print("Score after punctuations checker: ", score)

score = check_grammatical_errors(pos_list_punctuations, pos_list_grammar, score)
print("Score after grammar checking: ", score)

useful = [cleaned_essay, score, pos_list_grammar, pos_list_punctuations]
with open("preliminary_results.txt", "wb") as myFile:
    pickle.dump(useful, myFile)


end = time.time()
print(end-start)


