import torch as to
import random
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import numpy as np
import json
import nltk
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize, stem

for x in range (0, 3):                                                  #Diese for-Loop führt das ganze Programm dreimal aus damit auf jedenfall die Tags unterscheiden kann
    data_json = 'Der Chatbot/Data.json'

    with open(data_json, 'r', encoding='utf-8') as file:                #Lädt die JSON-Datei
        data = json.loads(file.read())

    all_words = []
    tags = []
    xy = []
    for intent in data['intents']:                                      #Erstellt eine Liste mit den Tags aus Data.JSON
        tag = intent['tag']
        tags.append(tag)
        for pattern in intent['patterns']:                              #Erstellt eine Liste aus den patterns von Data.JSOn
            w = tokenize(pattern)
            all_words.extend(w)
            xy.append((w, tag))                                         #Eine liste aus den Wörtern und ihren tags
    ignore_words = ['?', '.', '!']                                      #Ignoriert Satzzeichen
    all_words = [stem(w) for w in all_words if w not in ignore_words]   #Stemmed alle Wörter
    all_words = sorted(set(all_words))                                  #Sortiert die Wörter
    tags = sorted(set(tags))                                            #Sortiert die Tags
    print("all_words", all_words)
    print("tags", tags)                                                 #Gibt alles wieder zu Überprüfung
    print("xy", xy)

    X_train = []
    y_train = []
    for (pattern_sentence, tag) in xy:                                  #Erstellt eine Liste aus allen Wörter und allen Patterns mit Hilfen der bag_of_words-Funktion
        bag = bag_of_words(pattern_sentence, all_words)                 #Und eine Liste aus allen Tags ebenfalls mit Hilfe der bag_of_words-Funktion
        X_train.append(bag)
        labels = tags.index(tag)
        y_train.append(labels)

    X_train = np.array(X_train)                                         #Konvertiert die Listen zu Arrays
    y_train = np.array(y_train)

    num_epochs = 1000
    batch_size = 8
    learning_rate = 0.001
    input_size = len(X_train[0])                                        #Definiert Variablen für das NeuralNetwork
    hidden_size = 8
    output_size = len(tags)

    class ChatDataset(Dataset):                                         #Erstellt eine Class, die die Data beinhaltet
        def __init__(self):
            self.n_samples = len(X_train)
            self.x_data = X_train
            self.y_data = y_train
        def __getitem__(self, index):
            return self.x_data[index], self.y_data[index]
        def __len__(self):
            return self.n_samples

    dataset = ChatDataset()
    train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True)     #Setzt eine Dataloader fest

    model = NeuralNet(input_size, hidden_size, output_size)             #Setzt das Model fest

    criterion = nn.CrossEntropyLoss()                                   #Criterion rechnet den Loss
    optimizer = to.optim.Adam(model.parameters(), lr=learning_rate)     #Ermöglicht den fortschritt beim lernen

    for epoch in range(num_epochs):                                     #Sagt dem NeuralNetwork wie es die Iterations machen soll und kalkuliert den Loss
        for (words, labels) in train_loader:
            words = words
            labels = labels
            print(labels.type())
            outputs = model(words)
            labels = labels.type(to.LongTensor)
            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        
        if (epoch+1) % 100 == 0:                                        #Gibt den Loss jeder Epoch wieder
            print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

    print(f'final loss: {loss.item():.4f}')

    data = {                                                            #Definiert die benutzten Variablen zur Verwendung in einem anderen Program
        "model_state": model.state_dict(),
        "input_size": input_size,
        "hidden_size": hidden_size,
        "output_size": output_size,
        "all_words": all_words,
        "tags": tags
    }

    FILE = "Der Chatbot/data.pth"                                       #Speichert das Ergebnis
    to.save(data, FILE)

    print(f'training complete. file saved to {FILE}')