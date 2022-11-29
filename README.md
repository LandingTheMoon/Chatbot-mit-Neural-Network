<h1 align=center>Chatbot mit Neural Network - Projektseite</h1>
<div align=center>
    <img src='logo.png', height="200", border="5"></img>
</div>
<h3 align=center>von Jan Drewes (@LandingTheMoon) & 
Louis Lemberg (@MindOfUs)</h3>


## Übersicht

<ol>
    <li>
        <a href="#einführung">Einführung</a>
        <ol>
            <li>
                <a href="#gruppe">Die Gruppe</a>
            </li>
            <li>
                <a href="#idee">Die Idee</a>
            </li>
        </ol>
    </li>
    <li>
        <a href="#programme">Die verwendeten Programme</a>
        <ol>
            <li>
                <a href="#python">Python (Programmiersprache)</a>
            </li>
            <li>
                <a href="#vscode">VisualStudio Code (Programmierumgebung)</a>
            </li>
            <li>
                <a href="#anaconda">Anaconda (Distributionssoftware/Interpreter)</a>
            </li>
            <li>
                <a href="#pytorch">Pytorch (Neural Network)</a>
            </li>
            <li>
                <a href="#nltk">NLTK (Natural Language Toolkit)</a>
            </li>
            <li>
                <a href="#tk">tkinter (GUI)</a>
            </li>
        </ol>
    </li>
    <li>
        <a href="#chatbot">Der Chatbot</a>
        <ol>
            <li>
                <a href="#data">data.json</a>
            </li>
            <li>
                <a href="#nltk">nltk_utils.py</a>
            </li>
            <li>
                <a href="#model">model.json</a>
            </li>
            <li>
                <a href="#train">train.py</a>
            </li>
            <li>
                <a href="#chat">chat.py</a>
            </li>
            <li>
                <a href="#gui">gui_chatbot.py</a>
            </li>
        </ol>
    </li>
    <li>
        <a href="Stundenprotokoll.md">Stundenprotokoll</a>
    </li>
    <li>
        <a href="#sources">Quellen</a>
    </li>
    <li>
        <a href="#eigen">Eigenständigkeitserklärung</a>
    </li>
</ol>

## Einführung <a name="einführung"></a>

Im ersten Abschnitt unserer Projektseite werden wir zuerst einmal unsere Gruppe, sowie unsere Projektidee erklären.

### 1. Die Gruppe <a name="gruppe"></a>

Unsere Gruppe besteht aus Jan Drewes und Louis Lemberg, wir gehen beide in das Physikprofil der 11. Klasse. Für uns war von Anfang an klar, dass wir zusammen arbeiten wollen, da die Zusammenarbeit in anderen Projekten schon sehr gut funktioniert hat. Wir beide sind schon mit Grundkenntnissen in der Programmmierung durch kleinere vorausgegangenen Projekte in dieses Projekt gestartet. Deswegen haben wir uns eine etwas kniffeligere Aufgabe ausgesucht.
Bei uns gab es zu Beginn jedoch abgesehen von dem Projekt eine kleine extra Herausforderung, denn Louis war für die Zeit bis zu den Herbstferien wegen eines Schüleraustauschs in Frankreich. Dort hat er angefangen an dem Projekt zu arbeiten. 

### 2. Die Idee <a name="idee"></a>

Bei der Ideenfindung haben wir uns am Anfang sehr schwer getan. Eigentlich hätten wir gerne ein Projekt mit einem Arduino gemacht, da für uns beide die Arbeit mit einem kleinen Computer sehr spannend schien. Diese Idee mussten wir jedoch durch die am Anfang bestehende Distanz zwischen uns verwerfen. Dann haben wir uns darauf geeinigt keine externen Geräte zuverwenden, sondern einen Chatbot zuprogramieren. Um diesen aber ein wenig spannender zu gestalten, haben wir uns als Ziel gesetzt, mit einem Neural Network zu arbeiten. Dies war für uns beide komplett neu, hat uns aber sofort begeistert und interessiert. Und von da an ging alles seinen Lauf, wir haben damit begonnen die benötigten Programme zu intsallieren, welche wir unter <a href="#programme">den verwendeten Programmen</a> vorstellen. Nachdem wir uns mit den Programmen vertraut gemacht haben, haben wir mit dem Chatbot losgelegt. Anfangs wollten wir eigentlich einen Chatbot programmieren, welcher mathematische Probleme löst, diese Idee wurde jedoch durch das Neural Network zu zeitaufwändig, somit haben wir uns darauf konzentriert, einen Chatbot zu entwickeln, der ein normales Gespräch führen und dabei auf umfangreiche Eingaben des Users reagieren kann.

## Die verwendeten Programme <a name="programme"></a>

Im folgenden werden alle verwendeten Programme und Erweiterungen die maßgeblich zu unserem Projekt beigetragen haben vorgestellt.

### 1. Python (Programmiersprache) <a name="python"></a>

Als Programmiersprache haben wir uns Python ausgesucht, da es häufig in der Wirtschaft und Wissenschaft für Datenanalyse verwendet wird. Python eignet sich für die Programmierung eines Chatbots sehr gut, weil man die Eingabedaten analysieren muss, um die richtigen Antworten zu erzeugen.

### 2. VisualStudio Code (Programmierumgebung) <a name="vscode"></a>

Für die Programmierumgebung haben wir uns für VisualStudio Code (VSC) entschieden, da wir beide schon sehr gute Erfahrungen damit gemacht haben. VSC ist sehr übersichtlich, man kann zahlreiche individuelle Erweiterungen installieren, u.a. werden einem direkt eventuelle Tipp- bzw. Zeichenfehler angezeigt. Ein weiterer entscheidener Faktor für uns war, dass VSC mit GitHub kompatibel ist und man so gemeinsam an einem Projekt direkt zusammen arbeiten kann.

### 3. Anaconda (Distributionssoftware/Interpreter) <a name="anaconda"></a>

Als Python-Intepreter haben wir uns für Anaconda entschieden. Der Hauptgrund war, dass es mit Pytorch kompatibel ist, und wir auf Pytorch angewiesen waren. Zusätzlich hat Anaconda eine große Palette an Liberies, die man installieren und verwenden kann.
Anaconda ist allgemein für die Entwicklung von Anwendungen mit großen Datenmengen, wozu unser Projekt gehört, ausgelegt.

### 4. Pytorch (Neural Network) <a name="pytorch"></a>

Pytorch ist ein Framework, welches für Machine Learning genutzt wird. Es arbeitet dabei sehr schnell und hat allgemein eine sehr benutzerfreundliche Oberfläche. Was uns dazu verleitet hat, Pytorch zu verwenden. 
Pytorch ist auch allgemein bei großen Unternehmen sehr beliebt und wird dort vor allem für die Entwicklung künstlicher Intelligenzen, für Datenwissenschaften und für Forschung genutzt.

### 5. NLTK (Natural Language Toolkit) <a name="nltk"></a>

NLTK ist ein Tool zur Verarbeitung von natürlicher Sprache in Computersprache. NLTK verarbeitet also in unserem Fall unsere Data, die wir dem Chatbot zum lernen geben, in gewisse Algorithmen, womit das Programm dann arbeiten kann. 

### 6. tkinter (GUI) <a name="tk"></a>

Tkinter ist eine Python-Erweiterung, welche wir dafür benutzt haben die GUI von unserem Chatbot zu designen. Trotz anderer Moöglichkeiten haben wir und für tkinter entschieden, da es am häufigsten verwendet wird und somit die meisten Tutorials und Dokumentation hat.

## Der Chatbot <a name="chatbot"></a>

In der folgenden Sektion werden wir erklären, wie der Chatbot funktioniert. Dafür benötigen wir die folgenden 6 Dateien: <a href="#data">Data.json</a>, <a href="#nltk">nltk_utils.py</a>, <a href="#model">model.py</a>, <a href="#train">train.py</a>, <a href="#chat">chat.py</a> und <a href="#gui">gui_chatbot.py</a>. Alle Dateien bis auf Data.json sind in <a href="#python">Python</a> geschrieben. Für alle Dateien bis auf die Data.json und gui_chatbot.py haben wir uns größtenteils an folgender Seite <a href="https://www.python-engineer.com/posts/chatbot-pytorch/">https://www.python-engineer.com/posts/chatbot-pytorch/</a> orientiert, da es sich dabei um die Programmierung des Neural Networks ging, und wir beide vorher noch keine Erfahrung hatten. Wir haben uns den Code angesehen, verstanden und haben ihn deshalb auch ein wenig erweitert.

### 1. Data.json <a name="data"></a>

In der Datei Data.json haben wir die Daten hinterlegt, mit welcher der Chatbot trainiert wird. Dafür haben wir Listen nach folgendem Muster programmiert:

```
"intents": [
    {
        "tag": "",
        "patterns": [""],
        "responses": [""]
    }
]
```

Mit dem "tag" bestimmen wir den Namen von dieser Gruppe von "patterns" und "responses". Diesen haben wir immer so gewählt, dass er beschreibt was danach definiert wird. In "patterns" geben wir dem Chatbot durch Keywords, anhand welcher der Bot später erkennt, dass der User auf diesen "tag" zugreifen will. In der Liste-"responses" sagen wir dem Bot, was er antworten soll, wenn er einen von den davor definierten "patterns" erkennt. Dies sieht dann zum Beispiel anhand des "tags": "test" so aus:

```
"intents": [
    {
        "tag": "test",
        "patterns": ["test", "1,2,3"],
        "responses": ["Test succesful!"]
    }
]
```

### 2. nltk_utils.py <a name="nltk"></a>

In diesem Program legen wir drei Funktionen fest, die für die Verarbeitung von Eingaben (User und Data.json) wichtig sind. Dafür benutzen wie im Namen vom Program schon beschrieben <a href="#nltk">NLTK</a>.

```
def tokenize(sentence):
    return nltk.word_tokenize(sentence)
```
Die 'tokenize'-Funktion zerlegt die Eingabe vom User (Satz) in die einzelnen Worte, z.B. wird aus "How are you?", ["How", "are", "you", "?"].

```
def stem(word):
    return stemmer.stem(word.lower())
```
Die 'stem' bzw. 'stemmer'-Funktion bringt jedes Wort vom Input in die Grundform, so erkennt der Chatbot zum Beispiel in "plays", "playing" und "played", den immer wieder kehrenden Part "play".
```
def bag_of_words(tokenized_sentence, words):
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag
```
Die letzte Funktion in nltk_utils.py konvertiert die Eingabe vom User (Satz) in Zahlen, denn nur so kann Train.py den Input verarbeiten. Der Output der vorherigen Funktionen wird als Input verendet. Die Funktion zählt die Anzahl der Worte und wie oft sie vorkommen. Diese Information speichert in Form eines Arrays. Dies könnte z.B. so aussehen:

<img src="https://miro.medium.com/max/700/1*3IACMnNpwVlCl8kSTJocPA.png"></img>

### 3. model.py <a name="model"></a>

Mit diesem Programm wird nun das 'Model' bzw. das Neural Network mit Hilfe von <a href="#pytorch">pytorch</a> erstellt. Dafür haben wir eine class mit folgenden zwei Funktionen drin:

```
def __init__(self, input_size, hidden_size, num_classes):  
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
```
Diese erste Funktion tut nichts anderes als das Neural Network aufzubauen bzw. erst einmal zu erschaffen.
```
def forward(self, x:                                          
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        return out
```
Diese zweite Funktion schickt die ganzen Daten durch jedes einzelne Layer des Neural Networks durch.
### 4. train.py <a name="train"></a>

In diesem Programm bringen wir nun alles was wir vorher in den anderen Programmen bereits festgelegt haben zusammen, und lassen den Chatbot lernen. Dafür importieren wir zunächst alle möglichen Librarys, welche wir für die Umsetzung brauchen, und die Funktionen, welche wir in <a href="#model">model.py</a> und <a href="#nltk">nltk_utils.py</a> definiert haben.

```
data_json = 'Data.json'

with open(data_json, 'r', encoding='utf-8') as file:                    
    data = json.loads(file.read())

all_words = []
tags = []
xy = []
for intent in data['intents']:                                      
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:                              
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))                                         
ignore_words = ['?', '.', '!']                                      
all_words = [stem(w) for w in all_words if w not in ignore_words]   
all_words = sorted(set(all_words))                                  
tags = sorted(set(tags))
```

Zunächst öffnet das Programm unsere <a href="#data">Data.json</a> und liest dessen Inhalt. Dann erstellen wir drei Listen aus der Data.json, eine mit den 'tags', eine mit den 'patterns' und die letzte mit den Wörtern aus 'patterns' und den dazugehörigen 'tags'. Dann nutzen wir die 'stem'-Funktion, um diese dann allen Wörtern auszuführen. Darauf sortiert das Programm alle Wörter, sowie 'tags'. Diesen lassen wir uns dann zur Kontrolle noch einmal in die Konsole printen.

```
X_train = []
y_train = []
for (pattern_sentence, tag) in xy:                                      
    bag = bag_of_words(pattern_sentence, all_words)                  
    X_train.append(bag)
    labels = tags.index(tag)
    y_train.append(labels)

X_train = np.array(X_train)                                         
y_train = np.array(y_train)
```

Dann erstellt es drei weitere Listen, jedoch diesmal mit Hilfe der bag_of_words-Funktion aus <a href="#nltk">nltk_utils.py</a>, zudem konvertiert das Programm darauf die Listen zu arrays. Diese beiden Aktionen sind notwendig, denn nur mit diesen Daten kann der Chatbot tatsächlich trainieren.

Zunächst werden einige Variablen festgelegt, welche für das Neural Network gelten. Zudem wird eine Klasse definiert und erstellt, in welcher die ganze Trainingsdata gespeichert wird.

```
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True)     

model = NeuralNet(input_size, hidden_size, output_size)             

criterion = nn.CrossEntropyLoss()                                   
optimizer = to.optim.Adam(model.parameters(), lr=learning_rate)
```

Nun werden einige weitere Dinge definiert. Zunächst einen Dataloader, welcher wie der Name schon sagt die ganze Data liest und in der Variable train_loader speichert. Dann legen wir das Neural Network anhand der vorher definierten Variablen fest und speichern dies wiederum alles in einer Variable model. 
Dann legen wir noch criterion und optimizer fest, ersteres bestimmt den 'Loss' beim Training und letzteres stellt schlussendlich sicher, dass der Chatbot lernt.

```
for epoch in range(num_epochs):                                     
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
    
    if (epoch+1) % 100 == 0:                                        
        print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')
```

Jetzt lassen wir den Chatbot schließlich trainieren. Dabei geht er die komplette Data durch und rechnet den Loss für jeden 'epoch' aus.
Nachdem er fertig ist, gibt er noch den kompletten 'Loss' aus.

```
data = {                                                            
    "model_state": model.state_dict(),
    "input_size": input_size,
    "hidden_size": hidden_size,
    "output_size": output_size,
    "all_words": all_words,
    "tags": tags
}
```

Dann definieren wir die benutzen Variablen nochmal neu, um sie dann später in einem anderen Programm nochmal zu verwenden.

```
FILE = "data.pth"                                                   
to.save(data, FILE)
```

Am Ende wird nun die gesamte Trainingsdata in der Datei data.pth im aktuellen path gespeichert.

### 5. chat.py <a name="chat"></a>

Diese Datei ist für die eigentliche Technik hinter dem eigentlichen Chatvorgang mit dem Chatbot am Ende notwendig.
Zuerst müssen wir auch hier alle nötigen Librarys importen. Dann öffnen und lesen wir wieder die <a href="#data">Data.json</a>-Datei, nun öffnen und lesen wir aber noch zusätzlich die 'data.pth'-Datei, welche ja unsere Trainingsdata enthält. Zudem holt sich das Programm die Variablen und die dazugehörigen Parameter, welche wir am Ende von <a href="#train">train.py</a> definiert haben.

```
model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)                                 
model.eval()
```

Dann laden wir so ähnlich wie in <a href="#train">train.py</a> auch schon das Model bzw. den Chatbot anhand den vorher festegelegten Variablen.

```
bot_name = "Jeffrey" 
```

Nun legen wir den Namen von unserem Chatbot fest. Wir haben ihn auf den Namen "Jeffrey" getauft.

```
def get_response(msg):                                              
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
                return random.choice(intent['responses'])
    else:
        return "I do not understand. \nDo you want me to search that?" 
```

Diese Funktion gibt eine Response auf die Eingabe vom User aus. Dafür wird zuerst die Eingabe 'tokenized'. Damit wird dann eine Liste erstellt, die im folgenden noch durch die 'reshape'-Funktion umgeformt wird. Daraus wiederum wird ein Tensor erstellt, welches in pytorch wie ein normaler Array ist.
Dann lässt das Programm diesen Tensor durch das Model laufen und definiert daraufhin die Predicition vom Input. Danach holt das Programm sich den Tag aus dieser Predicition und rechnet die Wahrscheinlichkeit aus, dass dies die richtige Prediction ist. 
Nun guckt das Programm, ob die Wahrscheinlichkeit größer als 0,75 ist, und falls dies der Fall ist, sucht er alle 'tags' ab, und guckt, ob der 'tag' von der Prediction in <a href="#data">Data.json</a>, falls dies der Fall ist, gibt er eine zufällige 'response' aus.
Falls die Wahrscheinlichkeit kleiner als 0,75 ist, gibt er die Nachricht "I do not understand. Do you want me to search that?" aus.

Dann haben wir noch eine weiter Funktion get_tag in chat.py, welche exakt das gleiche gemacht, wie die vorher genannte Funktion, jedoch gibt diese am Ende den 'tag' aus statt einer 'response'.

### 6. gui_chatbot.py <a name="gui"></a>

test

## Quellen <a name="sources"></a>

<ol>
    <li>
        <a href="https://www.python-engineer.com/posts/chatbot-pytorch/">https://www.python-engineer.com/posts/chatbot-pytorch/</a>
    </li>
    <li>
        <a href="https://short-funny.com/hilarious-jokes.php">https://short-funny.com/hilarious-jokes.php</a>
    </li>
</ol>

## Eigenständigkeitserklärung <a name="eigen"></a>

Wir bestätigen hiermit, dass unser Ergebnis, ein von uns eigens erschaffenes Produkt ist, und wir uns bei der Umsetzung einzig durch die angegebenen Quellen geholfen haben.
