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

def form_sentences(essays):
    essay_mat = []
    for each_essay in essays:
        sentences = []
        temp = []
        ct = 0
        essay = convert_to_list(each_essay)
        for word in essay:
            if word in ['.', '?', '!']:
                if word != '!' or ( word=='!' and ct>=3):
                    sentences.append(temp)
                    temp = []
            else:
                temp.append(word)
                ct+=1
        essay_mat.append(sentences)
    return essay_mat


X = pd.read_csv('Dataset/training_set_rel3.tsv', sep='\t', encoding='ISO-8859-1')
df = pd.read_excel(r'Dataset\cleaned_dataset.xlsx')
y1 = df['domain1_score']
#print(df)
df = df.dropna(thresh = 12000, axis=1)
df = df.drop(columns=['rater1_domain1', 'rater2_domain1'])
#print(df.head())

minimum_scores = [-1, 2, 1, 0, 0, 0, 0, 0, 0]
maximum_scores = [-1, 12, 6, 3, 3, 4, 4, 30, 60]

#print(len(df['essay'].tolist()))
essays = df['essay'].tolist()
print(len(essays))


essays = df['essay'].tolist()
#print(len(essays))

sentence_mat = form_sentences(essays)

for el in sentence_mat:
    print(el)
print(len(sentence_mat))


# y = X['domain1_score']
# print(X)
# X = X.dropna(axis=1)
# X = X.drop(columns=['rater1_domain1', 'rater2_domain1'])
# print(X)
#print(X.head())
# print(y)
# print(y1)