from nltk import wordnet as wn
import time
import pickle

def passive_voice_detection(sentence):
    lemma = wn.WordNetLemmatizer()
    isBEForm = False
    error = 0
    for word in sentence:
        if word[1][0] == 'V':
            check = lemma.lemmatize(word[0], pos="v")
            if  check == 'be':
                isBEForm = True
        if isBEForm:
            check = lemma.lemmatize(word[0], pos="v")
            if check == 'be':
                isBEForm = True
            else:
                if word[1][0] == 'V' and word[1]!='VBG':
                    error = 1
                    isBEForm = False
    return error


with open("Preprocessing/preliminary_results.txt", "rb") as myFile:
    contents = pickle.load(myFile)

start = time.time()
essay = contents[2]
print(contents[2])
passive_sentences = 0
temp = []
for eachword in essay:
    if eachword[0] == '.':
        passive_sentences+=passive_voice_detection(temp)
        temp = []
    else:
        temp.append(eachword)
print(passive_sentences)
end = time.time()
print(end-start)