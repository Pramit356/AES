import re
import pickle
import enchant
from Dictionary.usedictionary import in_trie, find_correct_words
import time

def is_number(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def splitter_on_single_quotes(essay):
    new_essay = []
    for word in essay:
        if "'" in word:
            if word.index("'") == 0:
                new_essay.append(word[0])
                new_essay.append(word[1:])
            elif word.index("'") == len(word)-1:
                new_essay.append(word[:len(word)-1])
                new_essay.append(word[len(word)-1])
            else:
                new_essay.append(word)
        else:
            new_essay.append(word)
    return new_essay


def spellcheck_and_correct(raw_essay, score):
    punctuations = ["'", '"', '.', ',', '?', '!']
    print(raw_essay)
    essay = re.findall(r"@?[\w']+|[.,!?;'\"]", raw_essay)
    #essay = re.findall(r"@?[\w+][\w']+|[.,!?;'\"]", raw_essay)
    essay = splitter_on_single_quotes(essay)
    #essay = re.findall(r"@?\w+", raw_essay)
    print(essay)
    with open("Dictionary/savedict.txt", "rb") as myFile:
        trie = pickle.load(myFile)
    misswords = []
    incorrect_index = []

    # converting to lower case
    #essay = [el.lower() for el in essay]

    # Checking for incorrect words
    for i in range(len(essay)):
        el = essay[i]
        if '@' not in el and is_number(el) == False and el not in punctuations:
            isthere = in_trie(trie, el.lower())
            if (isthere == False):
                misswords.append(el)
                incorrect_index.append(i)
    print('incorrect spelling')
    print(misswords)

    # Find correct replacement for words
    # to_use_dict = input("Enter the dictionary (US or UK): ")
    to_use_dict = "US"
    if to_use_dict.upper() == "US":
        dictionaryUS = enchant.Dict("en_US")
        corrected_words = find_correct_words(misswords, dictionaryUS)
    else:
        dictionaryUK = enchant.Dict("en_UK")
        corrected_words = find_correct_words((misswords, dictionaryUK))

    print('closest corrected words')
    print(corrected_words)

    incorrect = len(list(set(corrected_words)))
    for i in range(len(corrected_words)):
        if corrected_words[i] == misswords[i]:
            incorrect-=1

    # Deduct scores here
    if incorrect > 0 and incorrect <= 4:
        score -= incorrect
    elif (incorrect > 4 and incorrect <= 14):
        score -= 2 * (incorrect - 4) + 4
    elif incorrect > 14:
        score -= 20
    print(score)

    print()
    for i in range(len(corrected_words)):
        essay[incorrect_index[i]] = corrected_words[i]
    # Replacement done

    return essay, score
