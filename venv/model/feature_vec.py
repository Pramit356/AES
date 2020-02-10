import numpy as np
import nltk
import re
from nltk.corpus import stopwords
#from gensim.models import Word2Vec

def essay_to_wordlist(essay_v, remove_stopwords):
    """Remove the tagged labels and word tokenize the sentence."""
    essay_v = re.sub("[^a-zA-Z]", " ", essay_v)
    words = essay_v.lower().split()
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
    return (words)

def essay_to_sentences(essay_v, remove_stopwords):
    """Sentence tokenize the essay and call essay_to_wordlist() for word tokenization."""
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    raw_sentences = tokenizer.tokenize(essay_v.strip())
    sentences = []
    for raw_sentence in raw_sentences:
        if len(raw_sentence) > 0:
            sentences.append(essay_to_wordlist(raw_sentence, remove_stopwords))
    return sentences


essay = "The use of computers is great for everyone. Using a computer can help you learn about different people from around the world. Also you can have the ability to talk to people. With a computer you can also learn about places all over the @LOCATION1 and the world. With a computer everyone can learn about people all over. If you were going on a vacation to somewhere in @LOCATION2 you could learn about what those people do. Also you can see what people your age do for a living. If you had to do a project for school about a place outside of the @LOCATION1 the computer would help a lot. You can search what thet wear and what holdays those people celebrate. Learning about people will help you make friends to. if a foreign exchange person comes to your school you can search about their culture and talk to than about it. While using a computer you can also talk to people. With the use of @CAPS1 or A.I.M you can talk to your friends easily. You can ask them what homework you had if you weren't in dschool. You can also become better well friends with people you didn't know that wll, by saying hello, or how was your day. You can also email. If you meet someone you made friends with on vacation you can email them. You can also go to websites where you can talk to people in other countris. If you have a webcam you can even video chat, and ask them questions about their country, or what they like. Also you can videochat with all yor friends to. Using a computer you can learn about places arounf the world. If you were going to a place ypu didn't know, you could look up the amazing resraurants, you could also look up fun things to do with the family. If you needed to do a projecct you can look up what the weather is like, and what the people do. if you wanted to help out a country that just had an earthquake or hurricane you could look up what you could do to help that country. Those three reasons are why compujters are essential to people. You can learn about different people, talk to your friends, and you can search and learn about different places arounf the world."
print(essay_to_sentences(essay, remove_stopwords = True))