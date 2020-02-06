from spellcorrector import spellcheck_and_correct
from stopword_removal import remove_stopwords
from lemmatization import lemmatize , lemmatize1
from checkstructures import sentence_proportion, check_punctuations_capitalization
from grammar3 import check_grammatical_errors
import time

start = time.time()
score = 100
f = open("Dictionary/input2.txt", "r")
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


print("Score after grammar checking: ", check_grammatical_errors(pos_list_punctuations, pos_list_grammar, score))

end = time.time()
print(end-start)


