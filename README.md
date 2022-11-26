<h1 align=center>Chatbot mit Neural Network - Projektseite</h1>
<h3 align=center>von Jan Drewes (@LandingTheMoon) & Louis Lemberg (@MindOfUs)<h3>

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

Unsere Gruppe besteht aus Jan Drewes und Louis Lemberg. Wir gehen beide in das Physikprofil der 11. Klassen und haben uns als Aufgabe gesetzt dieses Halbjahr zusammen in Informatik zu arbeiten. Für uns war von Anfang an klar, dass wir zusammen arbeiten wollen. Da die Zusammenarbeit auch in anderen Projekten schon sehr gut funktioniert hat. Wir beiden sind schon mit Grundkenntnissen in der Programmmierung durch kleinere vorausgegangenen Projekte in dieses Projekt gestartet. So war uns klar, dass die Aufgabe auch gerne ein bisschen kniffeliger sein dürfte.
Bei uns gab es zu Beginn jedoch abgesehen von dem Projekt eine kleine extra Herausforderung, denn Louis war für die Zeit bis zu den Herbstferien wegen eines Schüleraustauschs in Frankreich. Dort hat er jedoch so gut wie es ging auch schon aus der Ferne angefangen an dem Projekt zu arbeiten. 

### 2. Die Idee <a name="idee"></a>

Bei der Ideenfindung haben wir uns am Anfang sehr schwer getan. Eigentlich hätten wir gerne ein Projekt mit einem Arduino gemacht, da für uns beide die Arbeit mit einem kleinen Computer sehr spannend schien. Diese Idee mussten wir jedoch durch die am Anfang bestehende Distanz zwischen uns abblasen. Dann haben wir uns relativ schnell darauf geeinigt ein rein programmierbares Projekt zu machen. Bei der folgenden Suche, was genau wir jetzt eigentlich Programmieren wollen, sind wir relativ schnell auf einen Chatbot gekommen. Um dies aber ein wenig spannender zu gestalten, haben wir uns als Ziel gesetzt, einen Chatbot mit einem Neural Network zu programmieren. Dies war für uns beide komplett neu, schien uns aber sehr spannend und wir waren direkt interessiert. Und von da an ging alles seinen Lauf, wir installierten uns die benötigten Programme, welche wir unter <a href="#programme">den verwendeten Programmen</a> vorstellen, und es ging ans Programmieren. Anfangs wollten wir eigentlich einen Chatbot programmieren, welcher mathematische Probleme löst, diese Idee wurde jedoch durch das Neural Network zu zeitaufwändig, dass wir uns darauf konzentriert haben, einen Chatbot zu programmieren, der ein normales Gespräch führen kann und dabei auf etliche Eingaben des Users reagieren kann.

## Die verwendeten Programme <a name="programme"></a>

### 1. Python (Programmiersprache) <a name="python"></a>

test

### 2. VisualStudio Code (Programmierumgebung) <a name="vscode"></a>

test

### 3. Anaconda (Distributionssoftware/Interpreter) <a name="anaconda"></a>

test

### 4. Pytorch (Neural Network) <a name="pytorch"></a>

test

### 5. NLTK (Natural Language Toolkit) <a name="nltk"></a>

test

### 6. tkinter (GUI) <a name="tk"></a>

test

## Der Chatbot <a name="chatbot"></a>

In der folgenden Sektion werden wir nun erklären, wie der eigentliche Chatbot funktioniert. Dafür benötigen wir die folgenden 6 Dateien: <a href="#data">data.json</a>, <a href="#nltk">nltk_utils.py</a>, <a href="#model">model.py</a>, <a href="#train">train.py</a>, <a href="#chat">chat.py</a> und <a href="#gui">gui_chatbot.py</a>. Alle Dateien bis auf die erste sind in <a href="#python">Python</a> geschrieben. Alle Dateien bis auf die Data und GUI Datei haben wir uns größtenteils von folgender Seite <a href="https://www.python-engineer.com/posts/chatbot-pytorch/">https://www.python-engineer.com/posts/chatbot-pytorch/</a> abgeguckt, da es sich dabei um die Programmierung des Neural Networks ging, und wir beide davon vorher noch keine Ahnung hatten. Wir haben uns jedoch jede dieser Zeilen Code angeguckt und auch nachvollzogen.

### 1. data.json <a name="data"></a>

In der Datei data.json haben wir die ganzen Daten vorgeschrieben mit welcher der Chatbot am Ende trainiert. Dafür haben wir Listen nach folgendem Muster programmiert:

```
"intents": [
    {
        "tag": "",
        "patterns": [""],
        "responses": [""]
    }
]
```

Mit dem "tag" bestimmen wir einfach den Namen von dieser Gruppe von "patterns" und "responses". Diesen haben wir immer so gewählt, dass er beschreibt was danach definiert wird. In "patterns" geben wir dem Chatbot durch Keywords, anhand welcher der Bot später erkennt, dass der User auf diesen "tag" zugreifen will. In der Liste-"responses" sagen wir der Bot, wie er antworten soll, wenn er einen von den davor definierten "patterns" erkennt. Dies sieht dann zum Beispiel anhand des "tags": "greetings" so aus:

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

In dieser Datei legen wir drei Funktionen fest, welche am Ende auschlaggebend für das Neural Network sein werden. Dafür benutzen wie im Namen der Datei schon beschrieben <a href="#nltk">NLTK</a>.

```
def tokenize(sentence):
    return nltk.word_tokenize(sentence)
```
Diese 'tokenize'-Funktion zerlegt den Input vom User, welchen der Chatbot in einem string bekommt, in ganz viele einzelne kleine Teile. Zum Beispiel wird aus "How are you?", ["How", "are", "you", "?"].

```
def stem(word):
    return stemmer.stem(word.lower())
```
Diese 'stem' bzw. 'stemmer'-Funktion bringt jedes Wort vom Input in die simpelste Form, so erkennt der Chatbot zum Beispiel in "plays", "playing" und "played", den immer wieder kehrenden Part "play".
```
def bag_of_words(tokenized_sentence, words):
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag
```
Diese letzte Funktion in nltk_utils.py konvertiert den Input vom User, welcher der Chatbot in strings bekommt, in Zahlen, denn nur so kann der Chatbot mit dem Input arbeiten. Dafür benutzt er zunächst beide vorher genannten Funktionen und packt den Input dann in eine Zahl konvertiert in die Variable 'bag'. Dann gleicht er den Input mit allen Wörtern, die er durch die data.json-File kennt, ab, und packt an jede Stelle an welcher er ein Wort vom Input in der data.json File findet, eine 1, und ansonsten immer eine 0. Falls er ein Wort mehrmals Mal erkennt gibt er ne die komplette Anzahl aus. Dies könnte dann zum Beispiel so aussehen:

<img src="https://miro.medium.com/max/700/1*3IACMnNpwVlCl8kSTJocPA.png"></img>

Im finalen Ablauf wird immer zuerst die 'tokenize'-Funktion angewendet, dann die 'stem', darauf werden Satzzeichen entfernt und zum Beispiel wird dieser bag_of_words erstellt, wie im Bild dargestellt.

### 3. model.py <a name="model"></a>

Mit dieser Datei erstellen wir nun das 'Model' bzw. den Chatbot mit Hilfe von <a href="#pytorch">pytorch</a>. Dafür erstellen wir dessen zweischichtiges Neural Network.

### 4. train.py <a name="train"></a>

In dieser Datei bringen wir nun alles was wir vorher in den anderen Dateien bereits festgelegt haben zusammen, und lassen den Chatbot endlich trainieren. 

### 5. chat.py <a name="chat"></a>

test

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
