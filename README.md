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

### 5. tkinter (GUI) <a name="tk"></a>

test

## Der Chatbot <a name="chatbot"></a>

test

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

test

### 3. model.py <a name="model"></a>

test

### 4. train.py <a name="train"></a>

test

### 5. chat.py <a name="chat"></a>

test

### 6. gui_chatbot.py <a name="gui"></a>

test

## Quellen <a name="sources"></a>

<ol>
    <li>
        <a href="https://www.python-engineer.com/posts/chatbot-pytorch/">https://www.python-engineer.com/posts/chatbot-pytorch/</a>
        <a href="https://short-funny.com/hilarious-jokes.php">https://short-funny.com/hilarious-jokes.php</a>
    </li>
</ol>

## Eigenständigkeitserklärung <a name="eigen"></a>

test
