In diesem Program legen wir drei Funktionen fest, die für die Verarbeitung von Eingaben (User und Data.json) wichtig sind. Dafür benutzen wie im Namen vom Program schon beschrieben NLTK.

'''
def tokenize(sentence):
    return nltk.word_tokenize(sentence)
'''

Die 'tokenize'-Funktion zerlegt die Eingabe vom User (Satz) in die einzelnen Worte, z.B. wird aus "How are you?", ["How", "are", "you", "?"].

'''
def stem(word):
    return stemmer.stem(word.lower())
'''

Die 'stem' bzw. 'stemmer'-Funktion bringt jedes Wort vom Input in die Grundform, so erkennt der Chatbot zum Beispiel in "plays", "playing" und "played", den immer wieder kehrenden Part "play".

'''
def bag_of_words(tokenized_sentence, words):
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag
'''

Die letzte Funktion in nltk_utils.py konvertiert die Eingabe vom User (Satz) in Zahlen, denn nur so kann Train.py den Input verarbeiten. Der Output der vorherigen Funktionen wird als Input verendet. Die Funktion zählt die Anzahl der Worte und wie oft sie vorkommen. Diese Information speichert in Form eines Arrays. Dies könnte z.B. so aussehen:

<div align=center>
    <img src=https://miro.medium.com/max/1400/1*3IACMnNpwVlCl8kSTJocPA.webp, height="200", border="5"></img>
</div>
