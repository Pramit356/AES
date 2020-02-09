# import csv
#
# def listToString(s):
#     str1 = " "
#     return (str1.join(s))
#
# lst = ['word1', 'word2', 'word3']
# str1 = listToString(lst)
# print(str1)
#
# with open("testing.csv", "w", newline="") as f:
#     writer = csv.writer(f, quoting=csv.QUOTE_ALL)
#     writer.writerow([str1])

# from Preprocessing.preprocessing import pre_process
# f = open("testinput", "r", encoding="utf8")
# txt = f.read()
# f.close()
#
# print(pre_process(txt, 100))


#print(round(score/10))
#expenses = [[1, 1, 1, 'Chair', 1, 50, 'hosur', 'Timestamp(2017-01-01 00:00:00)'],
     #[2,1, 1, 'Table', 1, 50, 'hosur','Timestamp(2017-01-02 00:00:00)']]

import openpyxl

lst = [91,92,93,94,95,96,97,98,99]
score=95
wb = openpyxl.Workbook()

sheet = wb.active

p = 0

for el in lst:
    c1 = sheet.cell(row=p+1,column=1)
    c1.value = el
    p+=1

wb.save("model/Dataset/demo1.xlsx")