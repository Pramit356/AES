import pickle

with open("Preprocessing/preliminary_results.txt", "rb") as myFile:
    contents = pickle.load(myFile)
print(contents[0])
cleaned_essay = contents[0]
temp = []
sentence_vec = []
discourse_list = []
essay_size = 0
for word in cleaned_essay:
    if word == ".":
        sentence_vec.append(temp)
        temp = []
    else:
        temp.append(word.lower())
        essay_size+=1

print(sentence_vec)

discourse_list.append(sentence_vec[0])

for i in range(1,len(sentence_vec)):
    cosines_with_all = []
    for j in range(len(discourse_list)):
        l1_set = {w for w in discourse_list[j]}
        l2_set = {w for w in sentence_vec[i]}
        vec1 =[]
        vec2 =[]
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
        cval = 0
        for k in range(len(rvector)):
            cval += vec1[k] * vec2[k]
        cosine = cval / float((sum(vec1) * sum(vec2)) ** 0.5)
        cosines_with_all.append(cosine)
        #print("similarity: ", cosine)
    maxind = cosines_with_all.index(max(cosines_with_all))
    print("len: ", len(discourse_list))
    print(maxind)
    print("Maxval: ", cosines_with_all[maxind])
    if cosines_with_all[maxind]>0.1:
        discourse_list[maxind] = discourse_list[maxind] + sentence_vec[i]
    else:
        discourse_list.append(sentence_vec[i])

# for el in discourse_list:
#     print(len(el))
discourse_list_len = []
if len(discourse_list)>3:
    discourse_list_len.append(len(discourse_list[0]))
    sum = 0
    for i in range(1,len(discourse_list)-1):
        sum += len(discourse_list[i])
    discourse_list_len.append(sum)
    discourse_list_len.append(len(discourse_list[i+1]))
else:
    for i in range(len(discourse_list)):
        discourse_list_len.append(len(discourse_list[i]))
print("Number of words in each section: ", discourse_list_len)
print("Size of essay: ", essay_size)
for i in range(len(discourse_list_len)):
    discourse_list_len[i]/=essay_size
print(discourse_list_len)