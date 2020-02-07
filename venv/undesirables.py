from nltk import wordnet as wn
import time
import pickle

def passive_voice_detection(sentence):
    lemma = wn.WordNetLemmatizer()
    error = 0
    for i in range(len(sentence)-1):
        if sentence[i][1][0] == 'V':
            check = lemma.lemmatize(sentence[i][0], pos="v")
            if check == 'be' and sentence[i+1][1][0] == 'V' and sentence[i+1][1]!='VBG':
                error = 1
                break
    return error

def indirect_speech_detection(sentence):
    error = 0
    for eachword in sentence:
        if eachword[0] in ['say', 'says', 'told', 'tells']:
            if '"' or "'" not in sentence:
                error = 1
                break
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

essay = contents[3]
indirect_speech = 0
temp = []
for eachword in essay:
    if eachword[0] == '.':
        indirect_speech+=indirect_speech_detection(temp)
        temp = []
    else:
        temp.append(eachword)
print(indirect_speech)

print(end-start)