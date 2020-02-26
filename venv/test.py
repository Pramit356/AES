import math

# def normalized_vector(vector):
#     den = math.sqrt(sum(map(lambda val : val * val, vector)))
#     return [eachel / den for eachel in vector]
#
# vec = [1,0,1,0,1,1]
# print(normalized_vector(vec))


from Preprocessing.preprocessing import pre_process
f = open("testinput", "r", encoding="utf8")
txt = f.read()
f.close()

print(pre_process(txt, 100))


#print(round(score/10))
#expenses = [[1, 1, 1, 'Chair', 1, 50, 'hosur', 'Timestamp(2017-01-01 00:00:00)'],
     #[2,1, 1, 'Table', 1, 50, 'hosur','Timestamp(2017-01-02 00:00:00)']]

# import openpyxl
#
# lst = [91,92,93,94,95,96,97,98,99]
# score=95
# wb = openpyxl.Workbook()
#
# sheet = wb.active
#
#
# p = 0
#
# for el in lst:
#     c1 = sheet.cell(row=p+1,column=1)
#     c1.value = el
#     p+=1
#
# wb.save("demo1.xlsx")


# import pandas as pd
# X = pd.read_csv('model/Dataset/training_set_rel3.tsv', sep='\t', encoding='ISO-8859-1')
# df = pd.read_excel(r'model\Dataset\cleaned_dataset.xlsx')
# y1 = df['domain1_score']
# #print(df)
# df = df.dropna(thresh = 12000, axis=1)
# df = df.drop(columns=['rater1_domain1', 'rater2_domain1'])
# print(df.head())
#
# minimum_scores = [-1, 2, 1, 0, 0, 0, 0, 0, 0]
# maximum_scores = [-1, 12, 6, 3, 3, 4, 4, 30, 60]
# essays = df['essay'].tolist()
# print(essays[0])



# y = X['domain1_score']
# print(X)
# X = X.dropna(axis=1)
# X = X.drop(columns=['rater1_domain1', 'rater2_domain1'])
# print(X)
#print(X.head())
# print(y)
# print(y1)