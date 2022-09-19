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

###19.09.2022 Jan Drewes
Heute habe ich angefangen pytorch zulernen, also Nueral Networks. Dies habe ich getan, dürch die offiziele pytorch Seite (https://pytorch.org/tutorials/index.html). Ich habe angegfangen mir die basics von pytorch anzuschauen, um mich langsam drauf hin zuarbeiten das ich den Chatbot anfangen kann. Angefangen habe ich mit tensors und dann habe ich mir Nueral Networks angeschaut und wie sie funktionieren.
