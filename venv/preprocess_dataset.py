from Preprocessing.preprocessing import pre_process
import pandas as pd
import xlrd, openpyxl
import xlwt

df = pd.read_excel(r'model\Dataset\training_set_rel3.xlsx')
#print(df)
headings = df.columns.tolist()
#print(headings)
essays = df[headings[2]].tolist()
clean_essays = []
preliminary_scores = []
preliminary_scores.append("Score")
ind = 1
for each_essay in essays:
    cleaned, score =  pre_process(each_essay,100)
    print(ind)
    print(cleaned)
    print(score)
    clean_essays.append(cleaned)
    preliminary_scores.append(score)
    ind+=1

#print(preliminary_scores)
#print(len(cleaned))

df['essay'] = clean_essays
df.to_excel("model\Dataset\cleaned_dataset.xlsx", index=False)

wb = openpyxl.Workbook()

sheet = wb.active

ptr = 0

for el in preliminary_scores:
    cellVal = sheet.cell(row=ptr+1,column=1)
    cellVal.value = el
    ptr+=1

wb.save("model/dataset/Score.xlsx")



# f = open("testinput", "r", encoding="utf8")
# txt = f.read()
# f.close()
#
# print(pre_process(txt, 100))