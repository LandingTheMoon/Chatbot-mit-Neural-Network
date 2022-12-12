import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):                     #Funktion um einen Satz in einzelne Wörter zu ändern
    return nltk.word_tokenize(sentence)

 
def stem(word):                             #Funktion um die Wörter auf den Wortursprung runter zu brechen
    return stemmer.stem(word.lower())       #Also z.B. Input = "walking" Stem = "walk"


def bag_of_words(tokenized_sentence, words):                        #Funktion um ein String mit allen stems zumachen 
    sentence_words = [stem(word) for word in tokenized_sentence]    #Alle Wörter stemmen
    bag = np.zeros(len(words), dtype=np.float32)                    #erstellt ein Array mit Nullen für jedes Wort
    for idx, w in enumerate(words):                                 #Stellt eine List aus Einsen und Nullen für die Wörter
        if w in sentence_words: 
            bag[idx] = 1

    return bag