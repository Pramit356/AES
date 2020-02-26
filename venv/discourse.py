import pickle, openpyxl
import math
import pandas as pd

def convert_to_list(each_essay):
    essay_list = []
    word=''
    start = False
    for letter in each_essay:
        if letter == "'":
            if start == False:
                start = True
            else:
                start = False
                essay_list.append(word)
                word = ''
        elif letter not in ['[', ']', ',', ' ', '']:
             word+=letter
    return essay_list

def form_sentences(essay):
    sentences = []
    temp = []
    ct = 0
    if type(essay) != list:
        essay = convert_to_list(essay)

    for word in essay:
        if word in ['.', '?', '!']:
            if word != '!' or ( word=='!' and ct>=2):
                if temp!=[]:
                    sentences.append(temp)
                    temp = []
        else:
            temp.append(word.lower())
            ct+=1
    if sentences == []:
        return temp
    return sentences


def normalized_vector(vector):
    den = math.sqrt(sum(map(lambda val : val * val, vector)))
    return [eachel / den for eachel in vector]

def get_vectors(sent1, sent2):
    l1_set = {w for w in sent1}
    l2_set = {w for w in sent2}
    vec1 = []
    vec2 = []
    rvector = l1_set.union(l2_set)
    for w in rvector:
        if w in l1_set:
            vec1.append(1)  # create a vector
        else:
            vec1.append(0)
        if w in l2_set:
            vec2.append(1)
        else:
            vec2.append(0)
    return rvector, vec1, vec2

def calculate_cosines_with_clusters(rvector, vec1, vec2):
    cval = 0
    for k in range(len(rvector)):
        cval += vec1[k] * vec2[k]
    return cval / float((sum(vec1) * sum(vec2)) ** 0.5)


def find_cosines_with_all(sent1, sent2):
    #print('sent1: ', sent1)
    #print('sent2: ', sent2)
    rvector, vec1, vec2 = get_vectors(sent1, sent2)
    vec1 = normalized_vector(vec1)
    vec2 = normalized_vector(vec2)
    return calculate_cosines_with_clusters(rvector, vec1, vec2)

#def discourse_parser(sentence_vec, threshold):
def discourse_parser(essay, threshold):
    #print(essay)
    discourse_list = []
    sentence_vec = form_sentences(essay)
    print('Sentence vec: ', sentence_vec)
    if type(sentence_vec[0]) != list:
        return 30
    discourse_list.append(sentence_vec[0])              #Assume first line is always introduction

    for i in range(1,len(sentence_vec)):
        cosines_with_all = []
        for j in range(len(discourse_list)):
            cosines_with_all.append(find_cosines_with_all(discourse_list[j], sentence_vec[i]))
        maxind = cosines_with_all.index(max(cosines_with_all))
        if cosines_with_all[maxind]>threshold:
            discourse_list[maxind] = discourse_list[maxind] + sentence_vec[i]
        else:
            discourse_list.append(sentence_vec[i])


    intro = discourse_list[0]
    conclusion = discourse_list[len(discourse_list)-1]
    body = []

    for i in range(1, len(discourse_list)-1):
        cosine = []
        cosine.append(find_cosines_with_all(intro, discourse_list[i]))
        if len(body) == 0:
            cosine.append(0)
        else:
            cosine.append(find_cosines_with_all(body, discourse_list[i]))
        #print(conclusion)
        cosine.append(find_cosines_with_all(conclusion, discourse_list[i]))
        maxind = cosine.index(max(cosine))
        if maxind == 0 and cosine[maxind]>=threshold:
            intro+=discourse_list[i]
        elif maxind == 2 and cosine[maxind]>=threshold:
            conclusion += discourse_list[i]
        else:
            body+=discourse_list[i]
    # print(intro)
    # print(body)
    # print(conclusion)
    tot = len(intro+body+conclusion)

    percent_intro = (len(intro)*100)/tot
    percent_body = (len(body)*100)/tot
    percent_conc = (len(conclusion)*100)/tot

    score = 0
    score += 15 if percent_intro>=15 else percent_intro
    score += 10 if percent_conc>=10 else percent_conc
    score += 75 if percent_body>=75 else percent_body

    #print("intro: ", percent_intro)
    #print("body: ", percent_body)
    #print("conclusion: ", percent_conc)
    #print(round(score))
    return round(score) if score>40 else 40

# with open("preliminary_results.txt", "rb") as myFile:
#     contents = pickle.load(myFile)
#
# threshold = 0.05        #Hyperparameter to qualify for merging
# cleaned_essay = contents[0]
# print(discourse_parser(cleaned_essay, threshold))

df = pd.read_excel(r'model/Dataset/cleaned_dataset.xlsx', sep='\t', encoding='ISO-8859-1')
scores = ['discourse score']
essays = df['essay'].tolist()
it=1
for essay in essays:
    print()
    print()
    print(it)
    score = discourse_parser(essay, 0.05)
    print(score)
    scores.append(score)
    it+=1


df1 = pd.read_excel(r'model/Dataset/Score.xlsx', sep='\t', encoding='ISO-8859-1')
previous = df1['Preliminary scores'].tolist()
previous.insert(0,'Preliminary scores')

wb = openpyxl.Workbook()
sheet = wb.active
ptr = 0
for i in range(len(scores)):
    cellVal = sheet.cell(row=ptr+1,column=1)
    cellVal.value = previous[i]
    cellVal = sheet.cell(row=ptr + 1, column=2)
    cellVal.value = scores[i]
    ptr+=1

wb.save("model/dataset/Score2.xlsx")