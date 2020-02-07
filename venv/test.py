from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from Preprocessing.lemmatization import lemmatize

f = open("testinput", "r")
txt = f.read()
print(txt)
f.close()
lst = []
word = ""
temp = []
for letter in txt:
    if letter in [' ', ',', "'", '"']:
        if word!="":
            temp.append(word)
        word = ""
    else:
        word+=letter
    if letter == '.':
        lst.append(temp)
        temp = []

print(lst)
sw = stopwords.words('english')
for i in range(len(lst)-1):
    l1_list = lemmatize(lst[i])
    l2_list = lemmatize(lst[i+1])
    vec1 = []
    vec2 = []

    l1_set = {w for w in l1_list if not w in sw}
    l2_set = {w for w in l2_list if not w in sw}

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
    c = 0

    print(vec1)
    print(vec2)
    # cosine formula
    for i in range(len(rvector)):
        c += vec1[i] * vec2[i]
    cosine = c / float((sum(vec1) * sum(vec2)) ** 0.5)
    print("similarity: ", cosine)