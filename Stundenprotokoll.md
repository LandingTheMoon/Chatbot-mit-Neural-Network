# Stundenprotokoll

### 22.08.2022 Jan Drewes

Ich habe heute im Unterricht unsere Ideen für ein Projekt angeschaut und überlegt welches wir nehmen soll. Dabei waren in der Überlegung eine luftquaulitäts Messstation und ein Tic Tac Toe Spiel gegen einen Komputer. Am Ende der Stunde haben wir uns gegen die Messstation entscheiden, da wir keine geeigneten Sensoren für das Projekt haben. Das Tic Tac Toe Projekt haben wir auch rausgeschmissen, da wir fanden das es zu Komplitziert ist für uns. Wir haben beschlossen das wir nochmal überlegen und dann am 25.08.2022 entscheiden.

### 22.08.2022 Louis Lemberg

Ich habe heute, währenddessen Jan im Unterricht war und sich Gedanken zu unseren Ideen gemacht hat, über WhatsApp Rücksprache mit ihm gehalten. Dabei haben wir uns gegen unsere zwei vorher überlegten Ideen auf Grund von nicht vorhandenem Material und der Schwierigkeit entschieden. Wir haben uns dazu entschieden nochmal Rücksprache zu halten und uns dann am 25.08.2022 für ein Projekt final entscheiden.
Zudem habe ich mich angefangen mit GitHub und mit der Programmiersprache Markdown (md) auseinanderzusetzen.

### 25.08.2022 Jan Drewes

Ich habe heute weider im Unterricht überlegt welches Projekt wir angehen wollen. Wir haben uns zuhause überlegt ob wir nicht ein automatiesiertes Bewässerungssytem machen für eine Zimmerpflanze. Diese Idee haben wir erstmal nach hinten verschoben, weil wir uns überlegt haben das es einfacher wäre wenn wir etwas machen was nur programmiert wird, da Louis ja in Frankreich ist. Wir üpberlegen also noch mal weiter, aber plannen nächste Woche anzufangen.

### 26.08.2022 Louis Lemberg

Nachdem Jan und ich uns gestern nun schon zum zweiten Mal von unseren Ideen nach einigen Überlegungen abgewendet haben, habe ich mich weiter auf die Suche begeben nach Ideen was wir machen könnten. Dabei hab mich ausschließlich auf rein programmierbare Projekte beschränkt, da dies für uns durch den vorerst vorliegenden örtlichen Abstand beim Arbeiten einfach schien.
Weitergehend habe ich meine Einarbeitung in GitHub und Markdown vorerst beendet.

### 29.08.2022 Jan Drewes

Wir haben uns heute darauf geeinigt einen Chatbot zu programmieren, der in einer zukünftigen Version vielleicht auch mathematische/physikalische Probleme lösen kann. Um eine Übersicht zu behalten habe ich heute eine To-Do Liste auf der Projektseite erstellt. Dazu habe ich angefangen Resourcen zurecht zu suchen damit Louis und ich anfangen können das Programm zu schreiben.

### 31.08.2022 Louis Lemberg

Gestern haben Jan und ich uns wieder per WhatsApp verständigt und haben uns nun final dazu entschlossen einen Chatbot zu programmieren, der nach dem grundlegenden Erstellen in späteren Versionen in dem Sinne weiterentwickelt, dass dieser mathematische und auch physikalische Probleme lösen kann. Da wir uns dafür entschlossen diesen mit Python zu programmieren, habe ich damit angefangen meine bereits vorhandenen Vorkenntnisse in Python aufzufrischen.

### 05.09.2022 Jan Drewes
Ich habe heute vergebens versucht Anacondam mit pytorch und Visual Studio Code (VS Code) zum laufen zu bekommen auf meinem Computer. Dies hat leider nicht funktioniert. Ich werde mich zuhause damit weiter auseinander setzten, damit es bis Donnerstag funktioniert.

### 08.09.2022 Jan Drewes
Nach dem Ich zuhause VS Code mit Anaconda zum laufen gebracht habe, habe ich heute im Unterricht angefangen mich mit dem Program und der Sprache (Python) vertraut zu machen. Zum Beispiel habe ich heute das hier geschrieben:

<details>
    <summary>Erster Test Code</summary>
    
``` 
    import torch
    import numpy as np
    import numpy.random as npr

    H = ""
    msg4 = "Hello"
    msg5 = "Please say something else"
    while (H != msg4):
        H = input("Type anything")
        if (H == msg4):
            print(msg4)
        else:
            print(msg5) 
```
</details>

Dieses kliene Program fordert jemanden auf etwas zuschreiben und überprüft dann ob die Person "Hello" geschrieben hat. Wenn nicht dann fordert das Program einen auf etwas anderes zuschreiben. Wenn die Person "Hello" schreibt dannn antwort das Programm mit "Hello" und das Program ist zu ende.

### 09.09.2022 Louis Lemberg
Ich habe in der vergangen Woche meine Pythonkenntnisse aufgefrischt und habe mir meine Programmierumgebung eingerichtet. Ich habe mich dazu entschieden in VisualStudio Code zu programmieren, da ich mit diesem Programm schon vertraut bin. Zudem habe ich mir auf Rat von Jan Anaconda und pytorch installiert.

### 12.09.2022 Jan Drewes
Ich habe heute im Unterricht das Program vom letzten mal verbessert und erweitert, sodass es jetzt eine zweite Ebene von "How are you?".

<details>
    <summary>Erweiteter Test Code</summary>
    
```
    import torch
    import numpy as np
    import numpy.random as npr


    H = input("Hello! ")
    while (H != ""):
        if (H == "Hello") or (H == "Hi"):
            H = input("How are you? ")
        elif (H == "Good"):
            print("Great! Me too.")
            break
        elif (H == "Bad"):
            print("I'm sorry to hear that.")
            break
        elif (H == "Fuck you" or H == "F U"):
            H = input("Please do not swear. ")
        elif (H == "Shut up" or H == "Shut it"):
            print("Alright")
            break
        elif (H == "exit"):
            break
        else:
            H = input("I do not understand. ")
```
</details>

Als nächstestes werde ich mir wahrscheinlich mal anschauen wie man eine Oberfläche machen kann damit das Program nicht im Terminal laufen muss.

### 13.09.2022 Louis Lemberg
Am Wochenende habe ich mich theoretisch darum informiert wie man einen Chatbot beispielsweise programmieren könnte und meine Pythonkenntnisse in diesem Bereich dann auch verbessert.
Heute habe ich dann angefangen einen ersten kleinen Chatbot zu programmieren, der auf ganz einfache Fragen und Antworten antwortet. Dies sollen Fragen sein, wie zum Beispiel "Wie geht es dir?".

### 19.09.2022 Jan Drewes
Heute habe ich angefangen pytorch zulernen, also Nueral Networks. Dies habe ich getan, dürch die offiziele pytorch Seite (https://pytorch.org/tutorials/index.html). Ich habe angegfangen mir die basics von pytorch anzuschauen, um mich langsam drauf hin zuarbeiten das ich den Chatbot anfangen kann. Angefangen habe ich mit tensors und dann habe ich mir Nueral Networks angeschaut und wie sie funktionieren.

### 20.09.2022 Louis Lemberg
In der vergangenen Woche habe ich leider etwas schleppend, da ich ziemlich viel für die Schule in Frankreich zu tun hatte, den ersten kleinen Chatbot programmier. Dies ist der dazugehörige Programmcode:

<details>
    <summary>Erster kleiner Chatbot</summary>
    
``` 
print("Hello my friend, I'm Simon, you're Chatbot!")
print("-------------------------------------------")

while True:
    print("> How can I help you?")
    userinput = input()
    if userinput == "Hello":
        userinput = input("> Hi, how are you? ")
        if userinput == "Good":
            print("> That's good! Is there anything else I can do for you?")
            userinput = input()
            if userinput == "No":
                print("> Ok, goodbye, see you soon!")
                break
        else:
            print("> I'm sorry for you! Is there anything I can for you?")
            userinput = input()
            if userinput == "No":
                print("> Ok, goodbye, see you soon!")
                break
    elif userinput == "exit":
        break
    else:
        print("> I'm sorry, I think I can't help you... I'm still in progress! Have a nice day!")
        break
```
</details>

Dieser kann in der ersten Version auf die Nachricht "Hallo" von dem User antworten und fragt dann wie es dem User geht, und interagiert dann mit jeweiligen Antwort wieder. Als nächstes möchte ich diesen Chatbot noch ein bisschen komplexer gestalten.

### 22.09.2022 Jan Drewes
Ich habe heute im Unterricht damit angefangen eine Datei zu machen wo Dataen hinterlegt sind. Dies soll später der Ort sein wo die trainings Daten sind vom A.I. Hier für habe ich das Dateiformar .json verwendet. Ich habe dann in einem Program versucht auf diese Daten zuzugreifen. Dies hat funktioniert und ich habe mich daran gesetzt ein weg zu finden um wörter in Zahlen zu machen die für den Komputer verständich sind.

<details>
    <summary>Code um Buchstaben in Zahlen auszudrücken</summary>
    
``` 
    import torch
    import math
    import numpy as np
    import json

    with open("Data.json") as file:
        data = json.load(file)
    data2 = []
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            data3 = pattern
            data2.extend(data3)
            data4 = [ord(x) for x in data2]
    print(data4)
```
</details>
        
Dieser Code holt sich aus der .json datei eine Reihe an einzelnen Buchstaben die zusammen ein Wort ergeben. Das Program drückt sie dann als Zahlen aus. Ich plane durch einen Algorytmus diese Zahlen zu Listen machen wo eine Liste ein Wort ergibt. Dies kann ich machen, weil das Program die Buchstaben nach dem ASCII (American Standard Code for Information Interchange) convertiert.

### 25.09.2022 Louis Lemberg
Ich habe mich jetzt erstmal dazu entschieden mir anzugucken, wie man mit tkinter in Python Programme schön designen kann. Dafür habe ich erstmal um die Anordnung von Elementen zu üben, ein TicTacToe Feld mit 9 Buttons erstellt. Als nächstes möchte ich dann ein erstes mögliches Desgin für einen Chatbot programmieren.

<details>
    <summary>TicTacToe Layout</summary>
    
``` 
from tkinter import *

window = Tk()
window.title("TicTacToe Layout")

button1 = Button(window, height=5, width=10, text="O")
button2 = Button(window, height=5, width=10, text="X")
button3 = Button(window, height=5, width=10, text="O")
button4 = Button(window, height=5, width=10, text="X")
button5 = Button(window, height=5, width=10, text="X")
button6 = Button(window, height=5, width=10, text="O")
button7 = Button(window, height=5, width=10, text="X")
button8 = Button(window, height=5, width=10, text="O")
button9 = Button(window, height=5, width=10, text="X")

exit_button = Button(window, text="Exit", command=window.quit)

button1.grid(row = 1, column = 1)
button2.grid(row = 1, column = 2)
button3.grid(row = 1, column = 3)
button4.grid(row = 2, column = 1)
button5.grid(row = 2, column = 2)
button6.grid(row = 2, column = 3)
button7.grid(row = 3, column = 1)
button8.grid(row = 3, column = 2)
button9.grid(row = 3, column = 3)

exit_button.grid(row = 3, column = 4)

window.mainloop()
```
</details>

### 26.09.2022 Jan Drewes
Heute in der Stunde habe ich versucht die Liste von Zahlen nach Wörtern zu sortieren. Hierzu habe ich, den ASCII verwendet und ganz viele If-Statments. Dies hat dur mäßig funktioniert und ich werde daran noch zuhause arbeiten um es zum laufen zu kriegen.

### 02.10.2022 Louis Lemberg
In der vergangenen Woche habe ich mich mit dem möglichen Design für einen Chatbot programmiert. Dafür habe ich ein großes Textfeld, ein Eingabefeld und ein "Send"-Button in das window eingefügt. Als nächstes will ich dieses Design mit meinem Chatbot verbinden, den ich vor einigen Wochen programmiert hatte.

<details>
    <summary>TicTacToe Layout</summary>
    
``` 
from tkinter import *

window = Tk()
window.title("Chatbot")

background_color = "#17202A"
background_color2 = "#98bee3"
text_color = "#EAECEE"
font = "Lastica 14"

textfield = Text(window, bg=background_color, fg=text_color, font=font, width=60) 
entrybox = Entry(window, bg="#2C3E50", fg=text_color, font=font, width=55)
send_button = Button(window, text="Send", font=font, bg=background_color2, command=chat)

textfield.grid(row=1, column=0, columnspan=2)
entrybox.grid(row=2, column=0)
send_button.grid(row=2, column=1)
 
window.mainloop()
```
</details>

### 06.10.2022 Jan Drewes
Nach dem ich letzte Woche auf diese Schwiegrigkeit gestoßen, habe ich mich in der Zeit zwischen den stunden daran gesetzt das Problem zu lösen. Ich habe es auch geschaft das Problem zu lösen. Da diese Lösen etwa komplitzierter ist und etwas länger ist werde ich sie hier nicht einfügen. Ich habe das gemacht um zuverstehen wie abkürzungen das machen. Im weiteren habe ich dann in der Stunde angefangen mir verschiedene möglichkeiten einen Chatbot zu programieren angeschaut. Um dann zu überlegen welche wir benutzten sollten.

### 12.10.2022 Louis Lemberg
In der letzten Woche habe ich den Code für meinen Chatbot nochmal überarbeitet. Ich habe einige neue Elemente (Fragen und Aufforderungen) eingebunden und natürlich danach alles mit dem Design zusammengeführt.

<details>
    <summary>TicTacToe Layout</summary>
    
``` 
from tkinter import *

def chat():
    user_input = entrybox.get()

    message = "You -> " + entrybox.get()
    textfield.insert(END, "\n" + message)
 
    if user_input == "hello" or user_input == "hi" or user_input == "hey":
        textfield.insert(END, "\n" + "Bot -> Hello my friend, how can I help?")
 
    elif user_input == "how are you":
        textfield.insert(END, "\n" + "Bot -> I'm fine and you?")
 
    elif user_input == "fine" or user_input == "i am good" or user_input == "i am fine":
        textfield.insert(END, "\n" + "Bot -> That's nice! Is there anything else I can do for you?")

    elif user_input == "how is the weather today?":
        textfield.insert(END, "\n" + "Bot -> I'm not able to answer to this question but you could go to a window and look by yourself.")

    elif user_input == "tell me a joke":
        textfield.insert(END, "\n" + "Bot -> Did you hear about the guy who invented the knock-knock joke?" + "\n" + "Bot -> He won the “no-bell” prize.")
 
    elif user_input == "goodbye" or user_input == "bye":
        textfield.insert(END, "\n" + "Bot -> See you, have a nice day!")
 
    else:
        textfield.insert(END, "\n" + "Bot -> I'm sorry, I think I can't help you... I'm still in progress! Have a nice day!")
 
    entrybox.delete(0, END)

window = Tk()
window.title("Chatbot")

background_color = "#17202A"
background_color2 = "#98bee3"
text_color = "#EAECEE"
font = "Lastica 14"

textfield = Text(window, bg=background_color, fg=text_color, font=font, width=60) 
entrybox = Entry(window, bg="#2C3E50", fg=text_color, font=font, width=55)
send_button = Button(window, text="Send", font=font, bg=background_color2, command=chat)

textfield.grid(row=1, column=0, columnspan=2)
entrybox.grid(row=2, column=0)
send_button.grid(row=2, column=1)
 
window.mainloop()
```
</details>

Ich muss leider als kleines Fazit von meiner Zeit in Frankreich, in welcher Jan und ich getrennt arbeiten mussten, sagen, dass ich nicht wirklich zufrieden bin. Durch die vielen Aktivitäten und die sehr langgehende Schule in Frankreich, habe ich nicht immer regelmäßig Zeit gefunden und war leider nie so richtig im Arbeitsflow. Ich werde jetzt dafür natürlich nach Absprache mit Jan alles nachzuholen, was nachzuholen ist und mich versuchen umso mehr einzubringen.

### 03.11.2022
Heute war die erste Stunde in der wir beide zusammen an unserem Projekt gearbeitet haben. Wir standen direkt vor der Entscheidung, ob wir unseren Chatbot mit einem Movie Script oder anhand einer selbst geschriebenen Liste von möglichen Inputs und Responses trainieren wollen. Wir fanden beides sehr spannend, haben uns dann jedoch final für die zweite Variante mit der selbstgeschriebenen Liste entschieden. Damit haben wir dann angefangen den Bot für das "Training" vorzubereiten. Sodass wir vorraussichtlich in der nächsten Stunde einen ersten Test machen können.
