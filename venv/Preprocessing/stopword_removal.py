from nltk import pos_tag, wordnet as wn
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize

def remove_punctuations(essay, pos_list):
    punctuations = ["'", '"', ',', '?', '!']
    cleaned_essay = []
    pos_list1 = []
    for word, pos_tag in zip(essay, pos_list):
        if word in punctuations or "'" in word:
            continue
        cleaned_essay.append(word)
        pos_list1.append(pos_tag)
    return cleaned_essay, pos_list1

def remove_stopwords(essay, txt):
    useful_tag_initials = ['R', 'N', 'V', 'J']
    pos_list = pos_tag(essay)

    essay, pos_list1 = remove_punctuations(essay, pos_list)

    #These LOC fail in remote cases
    # print()
    # # set of stop words
    # stop_words = set(stopwords.words('english'))
    #
    # # tokens of words
    # word_tokens = word_tokenize(txt)
    # print(word_tokens)
    #
    # filtered_sentence = []
    #
    # for w in word_tokens:
    #     if w not in stop_words:
    #         filtered_sentence.append(w)
    #
    # print("len1: ", len(filtered_sentence))
    #
    # print("\n\nOriginal Sentence \n\n")
    # print(" ".join(word_tokens))
    #
    # print("\n\nFiltered Sentence \n\n")
    # print(" ".join(filtered_sentence))

    print('len1: ', len(essay))
    for word in pos_list1:
        ind = essay.index(word[0])
        if word[1][0] not in useful_tag_initials and word[1]!='RP':
            essay.remove(word[0])
    print('len2: ', len(essay))
    print(essay)

    return essay, pos_list, pos_list1