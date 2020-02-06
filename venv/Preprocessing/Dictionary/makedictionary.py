import pickle

f1 = open("Dictionary/words_alpha.txt", "r")
end_of_word = 'emp'
word_list = f1.read().split()
root = dict()
for each_word in word_list:
    current_dict = root
    for each_letter in each_word:
        current_dict = current_dict.setdefault(each_letter, {})
    current_dict[end_of_word] = end_of_word

with open("Dictionary/savedict.txt", "wb") as myFile:
    pickle.dump(root, myFile)