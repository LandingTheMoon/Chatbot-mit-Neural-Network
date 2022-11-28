import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

data_json = 'Data.json'

with open(data_json, 'r', encoding='utf-8') as file:                #Lädt Data.JSON
    intents = json.loads(file.read())

FILE = "data.pth"
data = torch.load(FILE)                                             #Lädt das Ergebnis von Train.py

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]                                   #Holt sich die Parameter und Variabeln aus Train.py
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)                                  #Lädt das model
model.eval()

bot_name = "Jeffrey"                                                #Gibt dem Bot seinen Namen

def get_response(msg):                                              #Diese Funktion erzeugt einen Response anhand des Inputs

    sentence = tokenize(msg)                                        #Tokenizes den Input
    X = bag_of_words(sentence, all_words)                           #Erstellt eine Liste
    X = X.reshape(1, X.shape[0])                                    #Formt die Liste um
    X = torch.from_numpy(X)                                         #Erstellt einen Tensor (Das Array von Torch)

    output = model(X)                                               #Läst die Liste durch das Model laufen
    _, predicted = torch.max(output, dim=1)                         #Setzt die Prediction vom Input fest

    tag = tags[predicted.item()]                                    #Holt sich denTag von der Prediction

    probs = torch.softmax(output, dim=1)                            #Setzt eine Wahrscheinlichkeit für die richtige Prediction fest
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:                                          #Schaut ob die Wahrscheinlichkeit größer als 0.75 ist
        for intent in intents['intents']:                           #Untersucht alle Tags
            if tag == intent["tag"]:                                #Erzeugt eine zufällige Antwort von dem vorhergesagtem Tag
                return random.choice(intent['responses'])
    else:
        return "I do not understand. \nDo you want me to search that?"           #Antortet falls kein Tag gefunden worden ist

def get_tag(msg):                                                   #Macht das gleiche wie get_response nur das es den vorhergesagten Tag weider gibt

    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return tag
    else:
        return ""