import pickle
import jellyfish
from nltk import pos_tag
end_of_word = "emp"

def in_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
        else:
            return False
    if end_of_word in current_dict:
        return True
    else:
        return False

def find_correct_words(incorrect_words, dict_used):
    correct_words = []
    for word in incorrect_words:
        candidates = dict_used.suggest(word)
        metricval = 99
        considered_word = ""
        for eachword in candidates:
            val = jellyfish.damerau_levenshtein_distance(eachword, word)
            #val = jellyfish.levenshtein_distance(eachword, word)
            #val = jellyfish.jaro_distance(eachword, word)
            if val<metricval:
                metricval = val
                considered_word = eachword
        correct_words.append(considered_word)
    return correct_words
