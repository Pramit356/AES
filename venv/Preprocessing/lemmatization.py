from nltk import pos_tag, wordnet as wn
from Dictionary.usedictionary import in_trie, find_correct_words
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''

def lemmatize(essay):
    lemma = wn.WordNetLemmatizer()
    lemma_word = []
    for word in essay:
        if '@' not in word:
            word1 = lemma.lemmatize(word, pos = "n")
            word2 = lemma.lemmatize(word1, pos = "v")
            word3 = lemma.lemmatize(word2, pos = "a")
            lemma_word.append(word3)

    print()
    # print('lemmatization')
    # print(lemma_word)
    return lemma_word

def lemmatize1(essay):
    lemma = wn.WordNetLemmatizer()
    pos_list = pos_tag(essay)
    cleaned_essay = []
    for tag in pos_list:
        if '@' not in tag[0]:
            cleaned_essay.append(lemma.lemmatize(tag[0], get_wordnet_pos(tag[1])))
        # if word[1]!='NNP' or word[0][0]!="@":
        #     essay.remove(essay[ind])
    return cleaned_essay


