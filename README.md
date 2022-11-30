<h1 align=center>Chatbot mit Neural Network - Projektseite</h1>
<div align=center>
    <img src='Der Chatbot/logo.png', height="200", border="5"></img>
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
        <a href="#ausführen">Wie führt man den Chatbot aus?</a>
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

In diesem letzten Programm haben wir das komplette Aussehen vom Chatbot designed. Mit allem was wir uns dazu gedacht haben, sprich mit dem Registrierung- und Loginsystems, der Scrollbar und alles was dazu gehört. Zudem haben wir auch noch einige letzten if-Statements für den Chatbot hinzugefügt.

Zunächst mussten natürlich erstmal wieder alle nötigen Librarys und Funktionen aus anderen Programmen importiert werden. Dann haben wir noch drei Variablen definiert, einmal 'url', welche wir für unsere Webbrowser-Funktion brauchen, die ich später erklären werde, und zum anderen drei Farben, welche wir den Labels, Buttons, etc. im weiteren Code zuordnen werden.

Im folgenden definieren wir nun einige seperate Funktionen. Angefangen haben wir mit der Funktion unseres Mainscreens, welche wir auch am Ende ausführen und der Startschuss für unser komplettes Programm ist. 

```
def mainscreen():
    w = 400
    h = 500
    chatgui = Tk()                                                  
    chatgui["background"] = bg_color1                               
    chatgui.title("Jeffrey.py")                                     
    chatgui.configure(width=w, height=h)                            
    chatgui.resizable(width=False, height=False)

    theme = Style()                                                 
    theme.theme_use('vista')

    stylegui = Style(chatgui)                                       
    stylegui.configure('.', font=("Avenir", 9))
    
    welcome = Label(chatgui, text="Welcome to our Chatbot!", font="Avenir 16", background = bg_color1 , foreground="#C14F00")
    welcome.place(x=80, y=80)                                       
    welcome.config()
```

Dies ist ein beispielhafter Ausschnitt aus dieser Funktion, in den ersten Zeilen Code wir überhaupt erstmal das Fenster erstellt. Es wird die Farbe, der Name und die Größe festgelegt. In den darauf folgenden Zeilen legen wir das Thema mithilfe von ttk fest (ttk ist eine Erweiterung zu tkinter, welche mehr Möglichkeiten zum Designen bietet). Dieses Thema hat ein festgelegtes Design für Buttons, Entrys, etc. Dann wird noch die Hauptschriftart definiert, die in unserem Fall "Avenir" ist, mit der Größe 9. Als Beispiel wie wir die Elemente auf unsere Seiten bringen, haben wir uns unser Welcome-Label ausgesucht, als erstes legen wir dabei fest, dass dieses Label auf diesm Fenster platziert werden soll, dann den Text des Labels, darauf die Schrift und deren Größe und zum Schluss die Hinter- und Vordergrundfarbe. Die Vordergrundfarbe ist hierbei die Schriftfarbe. Dann wird noch definiert wo dieses Label platziert werden soll und die 'config'-Funktion platziert es dann einfach Final. Dieses System wenden wir bei allen Elementen an. Bei Buttons fügen wir dann einfach noch einen Command hinzu, der zu einer weiter Funktion von diesem Programm führt.

Außerdem werden in dieser Funktion-'mainscreen' noch einige Variablen globalisiert, sodass man im gesamten Programm darauf zugreifen kann. Zudem werden noch zwei Styles für die Buttons und die Scrollbar definiert, in dem gleichen Sinne, wie bei der Schrift. Und es werden noch das Logo, der LogIn und Registrierungs Button und der Exit-Button auf der Seite platziert.

```
def quit():                                                         
    chatgui.destroy()
    print("window has been destroyed")
```

Diese Funktion wird beim Auslösen des Exit-Buttons oder der Tastenfolge shift+enter Ausgelöst und zerstört das Gesamte GUI, sprich das gesamte Programm.

```
def register():                                                     
    registerScreen = Toplevel(chatgui)                              
    registerScreen.geometry("300x250")
    registerScreen.title("Registration")
    registerScreen["background"] = bg_color1

    username = StringVar()                                          
    password = StringVar()

    Label(registerScreen, text="Username", background=bg_color1, foreground=txt_color).pack()       
    username_entry = Entry(registerScreen, textvariable=username)   
    username_entry.pack()                                           
    username_entry.focus()                                          
    Label(registerScreen, text="Password", background=bg_color1, foreground=txt_color).pack() 
    password_entry = Entry(registerScreen, textvariable=password, show="*")      
    password_entry.pack()                                               
    Button(registerScreen, text="Register", width="10", command=registerUser, style='log.TButton').pack()
```

Dies ist ein Teil der 'register'-Funktion, welche ausgelöst wird, wenn der 'Register'-Button auf dem mainscreen gedrückt wird. Erst einmal wird natürlich erstmal wieder das Fenster erstellt. Besonders hierbei ist, dass dieses ein PopUp Fenster vom Mainscrenn sein wird. Dann legen wir mit 'username' und 'password' zwei Variablen für den Input fest. Dann fügen wir wieder Elemente zu unserem Fenster hinzu. In diesem Fall sind die beiden 'entry'-Felder besonders. Dessen Input wird nämlich direkt in den eben erwähnten Variablen gespeichert und bei dem 'password'-Entry haben wir die Besonderheit, dass man nicht den richtigen Text sieht sondern anstelle von diesm nur Sternchen.

Weitergehen, was in diesem Beispielcode nicht zu sehen ist, werden einige Platzhalter-Labels erstellt und es werden wieder einige Variablen globalisiert.

```
def registerUser():                                                
    if username.get() == "" or password.get() == "":               
        tkinter.messagebox.showinfo(title="Info", message="No input recognized!")   
    else: 
        username_info = username.get()                              
        password_info = password.get()

        file = open(username_info, "w")                             
        file.write(username_info+"\n")                              
        file.write(password_info)                                   
        file.close()                                                

        username_entry.delete(0, END)                               
        password_entry.delete(0, END)

        tkinter.messagebox.showinfo(title="Info", message="Registration succesful!")        
        registerScreen.destroy()  
```

Diese Funktion wird vom Button 'Register' auf dem eben erklärten PopUp-Fenster für die Registrierung aufgerufen. Sie registriert den User. Dafür wird erstmal überprüft, ob es überhaupt einen Input gab. Wenn nämlich nicht, sagt das Programm dies dem User durch eine tkinter-Messagebox. 
Falls beide Eingabefelder Input enthalten, holt sich die Funktion die beiden Inputs. Dann erstellt das Programm eine Textatei im aktuellen Path mit dem Namen des Usernames, dann schreibt das Programm in die erste Zeile der Datei den Username und die Nächste das Passwort. Dann schließt das Programm die Datei und speichert sie. 
Darauf werden beide Eingabefelder zerstört, eine Messagbox geschickt, dass die Registrierung erfolgreich war, und final wird dann das Pop-Up Fenster für die Registrierung zerstört. Man landet dann wieder auf dem Mainscreen.

```
def login():                                                        
    loginScreen = Toplevel(chatgui)                                 
    loginScreen.title("Login")
    loginScreen.geometry("300x250")
    loginScreen["background"] = bg_color1
```

Die Login-Funktion wird durch den Login-Button auf dem Mainscreen ausgelöst und erstellt wieder ein PopUp-Fenster. Diese sieht genauso aus wie jenes von der Registrierung. Es wurden nur einige Texte geändert.

```
def loginUser():                                                    
    list_of_files = os.listdir()                                    
    if username_input in list_of_files:                             
        file1 = open(username_input, "r")                           
        verify = file1.read().splitlines()                          
        if password_input in verify:                                
            tkinter.messagebox.showinfo(title="Info", message="Login succesful!")       
            therealusername = username_input                        
            loginScreen.destroy()                                   
            userselection()                                         
        else:
            tkinter.messagebox.showinfo(title="Info", message="Password is wrong!")         
            password_entry1.delete(0, END)                          
    else:
        tkinter.messagebox.showinfo(title="Info", message="Username is wrong!")         
        username_entry1.delete(0, END)                              
        password_entry1.delete(0, END)
```

Diese Funktion wird durch den Login-Button auf dem Login-PopUp-Fenster ausgeführt. Sie ist dazu zuständig den Login-Vorgang durchzuführen. Zuerst werden, was jetzt nicht in diesem Codebeispiel gezeigt ist, es werden wieder die Inputs von den Entry-Feldern auf dem Login-PopUp Fenster in eine Variable verpackt. 
Dann wird eine Liste mit dem Namen von alles Files im aktuellen Path erstellt. Darauf folgt eine if-Abfrage ob der Username vom Login-Entry in den Files wiederzufinden ist. Wenn dies nicht der Fall ist, wird eine Messagebox geschickt, dass der Username falsch ist und die beiden Entry-Felder werden geleert. Falls dies aber der Fall ist, wird diese Datei mit dem Username geöffnet und die beiden Zeilen werden getrennt gelesen. Falls nun das Passwort vom 'password'-Entry auch noch in dieser Datei ist, kriegt der User eine Messagebox, dass der Login erfolgreich war und der username wird in eine globale Variable gapackt. Zudem wird noch das Login-PopUp Fenster zerstört und die Funktion 'userselection', welche den eigentlichen Chatbot startet, ausgeführt. Im Falle, dass das Passwort nicht übereinstimmt, bekommt der User dazu eine Messagebox und es wird nur das Passwort-Entry geleert.

```
mainscreen()           
```

Diese letzte Zeile Code ist die Wichtigste, denn diese führt die Funktion 'mainscreen' aus und startet somit das komplette Programme.

### def userselection()

Diese Funktion ist die Verknüpfung zwischen der chat.py Datei und dieser GUI Datei und wird durch ein erfolgreiches Login ausgeführt. Innerhalb dieser Funktion gibt es nochmal zwei weitere Funktionen. Vor diesen anderen beiden Funktionen, wird erst einmal der Username vom erfolgreichen Login in eine Variable gepackt. Dann wird der Mainscreen in den Chatbotscreen umgewandelt. Die Login und Registrierungs-Buttons werden entfernt, und die Scrollbar, das Entry-Feld und das Chatdisplay werden hinzugefügt. Zudem wird noch ein Enter-Button zum Abschicken und eine Label für die Erklärung zum Nachrichten schicken und für den Exit hinzugefügt. Außerdem wird der Input vom User in eine Variable gepackt.

```
def callback():                                                 
    inp = input.get()                                           
    if inp == "":                                               
        return
    else:
        print(f"Input has been confirmed and send as: {inp}")
        chatdisplay.configure(state=NORMAL)                     
        chatdisplay.insert(END, f'{user}: {inp} \n')            
        chatdisplay.configure(cursor="arrow", state=DISABLED)   
        inputentry.delete(0, END)                               
        res = get_response(inp)                                 
        print(f"Response: {res}")
        restag = get_tag(inp)                                    
        print(f"Tag: {restag}")
```

Dies ist der erste Teil von der ersten Funktion in 'userselection'. Das Programm holt sich zuerst den Input und packt ihn in eine Variable. Dann guckt es, ob dieser Input leer ist wenn ja, tut das Programm nichts. Wenn jedoch etwas erkannt wird, wird der Input mit dem Username zusammen im Chatdisplay angeziegt. Dann wird das Entry-Feld geleert und das Programm holt sich mit Hilfe der 'get_response'-Funktion aus <a href="#chat">chat.py</a> eine Antwort. Diese zeigt es dann auch im Chatdisplay an.

```
if restag == "datetime":                                
    time = datetime.now()                               
    timenow = time.strftime("%H:%M")                    
    datenow = time.strftime("%d/%m/%Y")                 
    chatdisplay.configure(state=NORMAL)                 
    chatdisplay.insert(END, f'{bot_name}: The time is {timenow} and the date is \n{datenow} \n')        
    chatdisplay.yview(END)                              
    chatdisplay.configure(cursor="arrow", state=DISABLED) 
elif restag == "":                                      
    global web_input                                    
    web_input = inp
    print(f'web_input: {web_input}')
    chatdisplay.configure(state=NORMAL)                 
    chatdisplay.insert(END, f'{bot_name}: {res} \n')    
    chatdisplay.yview(END)                              
    chatdisplay.configure(cursor="arrow", state=DISABLED) 
elif restag == "yes":                                   
    webbrowser.open(url + web_input)                    
    print(f'web_input: {web_input}')
    chatdisplay.configure(state=NORMAL)                 
    chatdisplay.insert(END, f'{bot_name}: Please wait a moment! \n')        
    chatdisplay.yview(END)                              
    chatdisplay.configure(cursor="arrow", state=DISABLED)
elif restag == "no":    	                            
    chatdisplay.configure(state=NORMAL)                 
    chatdisplay.insert(END, f'{bot_name}: Ok, Please type something else. \n')      
    chatdisplay.yview(END)                              
    chatdisplay.configure(cursor="arrow", state=DISABLED)       
else:
    chatdisplay.configure(state=NORMAL)                 
    chatdisplay.insert(END, f'{bot_name}: {res} \n')    
    chatdisplay.yview(END)                              
    chatdisplay.configure(cursor="arrow", state=DISABLED)
    if restag == "goodbye" or restag == "thanks":       
        chatgui.after(1500, delay)
```

Dieser zweiter Teil der 'callback'-Funktion gehört in die elfe-Clause vom ersten Teil. Hier werden einige Sonderfälle definiert, wo der Chatbot besonders drauf antworten soll.
Der erste Sonderfall ist wenn der 'tag' vom Userinput gleich 'datetime' ist, denn dann wird eine Variable mit der aktuellen Uhrzeit und dem aktuellen Datum erstellt. Dafür nutzen wir das PlugIn 'datetime'. Dann bringen wir die Zeit und das Datum in das von uns gewünschte Format und lassen es auf dem Chatdisplay anzeigen.
Der zweite Sonderfall bzw. eigentlich die nächsten drei Sonderfälle hängen alle miteinander zusammen, denn sie ermöglichen die Websuche. Denn wenn der Input vom User keinem 'tag' zugeordnet werden konnte, wird der Input in eine globale Variable gepackt, damit wir gleich wieder drauf zu greifen können. Und es wird die normale Response-Funktion ausgeführt, bei dieser kommt aber, da der 'tag' unbekannt ist, am Ende die Frage raus, ob der Chatbot den Input vom User in Google suchen soll. Wenn er dies mit "ja" beantwortet (dies ist gleichzeitig der 3. Sonderfall), wird der Standardbrowser geöffnet und mit Google der Input gesucht. Der Chatbot gibt dann nur einmal im Chatdisplay aus, dass er User ein wenig Geduld haben soll, denn bei manchen Rechner dauert dies einen kurzen Moment länger. Falls der User mit "no" antwortet (4. Sonderfall), wird dieser einfach aufgefordert etwas anderes zu schreiben.
Falls keiner von diesen Sonderfällen zu trifft, wird die normale Prozessur angewandt. Der Chatbot zeigt die Response, welche er aus <a href="#chat">chat.py</a> erhalten, an. Falls dabei festgestellt wird, dass er 'tag' vom Input 'goodbye' oder 'thanks' ist. Wird die Funktion 'delay' ausgeführt, welche das komplette Programm schließt. Vorher schreibt noch eine kurze Verabschiedungsnachricht.

```
def delay():                                                    
        chatdisplay.configure(state=NORMAL)                         
        chatdisplay.insert(END, f"This window will now be destroyed. \nPlease do not press anything. \n")       
        chatdisplay.yview(END)                                      
        chatdisplay.configure(cursor="arrow", state=DISABLED)       
        chatgui.after(2500, quit)
```

Dies ist die eben genannte Funktion, welche damit auch die zweite Funktion in der großen 'userselection'-Funktion ist.

## Wie führt man den Chatbot aus? <a name="ausführen"></a>

Um unseren Chatbot zum Laufen zu bekommen, muss man sich zunächst alle Dateien importieren. Zusätzlich braucht man Anaconda und dessen Erweiterungen (pytorch, tkinter, tkk und datetime) Dann führt man zuerst <a href="#train">train.py</a> aus, damit der Chatbot erst einmal von der Data lernt. Daraufhin muss man dann nur noch <a href="#gui">gui_chatbot.py</a> ausführen, und der Chatbot sollte starten und funktionieren. Natürlich muss man sich dann zunächst eine Konto erstellen, aber nach erfolgreicher Registrierung und LogIn sollte man dann mit dem Chatbot reden können.

## Quellen <a name="sources"></a>

<ol>
    <li>
        <a href="https://www.python-engineer.com/posts/chatbot-pytorch/">https://www.python-engineer.com/posts/chatbot-pytorch/</a>
    </li>
    <li>
        <a href="https://short-funny.com/hilarious-jokes.php">https://short-funny.com/hilarious-jokes.php</a>
    </li>
    <li>
        <a href="https://www.alexanderthamm.com/de/data-science-glossar/pytorch/">https://www.alexanderthamm.com/de/data-science-glossar/pytorch/</a>
    </li>
    <li>
        <a href="https://www.python-lernen.de/webbrowser-mit-python-nutzen.htm">https://www.python-lernen.de/webbrowser-mit-python-nutzen.htm</a>
    </li>
    <li>
        <a href="https://www.youtube.com/watch?v=Xt6SqWuMSA8&list=WL&index=2">https://www.youtube.com/watch?v=Xt6SqWuMSA8&list=WL&index=2</a>
    </li>
</ol>

Alle Links wurden zuletzt erfolgreich am 01.12.2022 um --.-- Uhr geöffnet.

## Eigenständigkeitserklärung <a name="eigen"></a>

Wir bestätigen hiermit, dass unser Ergebnis, ein von uns eigens erschaffenes Produkt ist, und wir uns bei der Umsetzung einzig durch die angegebenen Quellen geholfen haben.
