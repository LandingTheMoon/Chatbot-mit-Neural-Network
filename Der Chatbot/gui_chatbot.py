from tkinter import *
import tkinter.messagebox
from tkinter.scrolledtext import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import numpy as np
from chat import get_response, get_tag, bot_name
from datetime import datetime
import os
import webbrowser

url = "https://www.google.com/search?q="                            #Webadresse definiert

bg_color1 = "#17202A"
bg_color2 = "#98bee3"                                               #Farben definiert für das GUI
txt_color = "#EAECEE"

def mainscreen():                                                   #Erstellung der Funktion vom Haupt-Screen
    global chatgui
    global loginButton
    global registerButton                                           #Hier werden Variablen erstellt die von allen Funktionen benutzt werden können  
    global exit1
    global w
    global h

    w = 400
    h = 500
    chatgui = Tk()                                                  #Hier wird der Haupt-Screen erstellt
    chatgui["background"] = bg_color1                               #Farbe des Interfaces wird festgelegt
    chatgui.title("Jeffrey.py")                                     #Titel
    chatgui.configure(width=w, height=h)                            #Größe des Interfaces festgelegt durch die Variablen w und h
    chatgui.resizable(width=False, height=False)                    #Diese Zeile legt fest, dass der User nicht die Größe vom Fenster verändern kann
    
    theme = Style()                                                 #Theme setzt das theme von allen Sachen, wie z.B. von Buttons
    theme.theme_use('vista')

    stylegui = Style(chatgui)                                       #Stylegui setzt alle Schrift auf Avenir 9
    stylegui.configure('.', font=("Avenir", 9))

    stylescrollbar = Style(chatgui)                                 #Stylescrollbar erstellt eine Scrollbar die keine Pfeile hat
    stylescrollbar.layout('arrowless.Vertical.TScrollbar', [('Vertical.Scrollbar.trough', {'children': [('Vertical.Scrollbar.thumb', {'expand': '1', 'sticky': 'nswe'})], 'sticky': 'ns'})])

    global stylebutton                                              #Aus stylebutton wird eine globale Variable, die Hintergrundfarbe und Größe der Knöpfe ändert
    stylebutton = Style(chatgui)
    stylebutton.configure('log.TButton', background=bg_color2, height="2")

    logoimage = Image.open("Bilder/logo.png")                              #Hier wird das Logo geöffnet
    logoimageresize = logoimage.resize((125,90), Image.ANTIALIAS)   #In dieser Zeile wird die Größe vom Logo verändert
    imageneu = ImageTk.PhotoImage(logoimageresize)                  #Hier wird das Bild so verarbeitet, dass tkinter es darstellen kann
    logo = Label(chatgui, image=imageneu)                           #Hier wird ein Label erstellt mit dem Logo, sodass das Logo angezeigt wird
    logo.place(x=137, y=150)                                        #Der .place Command sagt dem Programm wo das Label hin soll

    welcome = Label(chatgui, text="Welcome to our Chatbot!", font="Avenir 16", background = bg_color1 , foreground="#C14F00")
    welcome.place(x=80, y=80)                                       #Hier wird die Willkommen-Schrift erstellt und im GUI platziert
    welcome.config()

    loginButton = Button(text="Login", width="30", command=login, style='log.TButton')      #Hier wird der Login Knopf erstellt mit dem Style der oben erstellt wurde und mit dem Command der später noch definiert wird
    loginButton.place(x=90, y=290)
    loginButton.config()
    chatgui.bind('<Return>',lambda event:login())                   #Der .bind Command kann einer Taste auf dem Keyboard eine Funktion zu weisen

    registerButton = Button(text="Register", width="30", command=register, style='log.TButton')     #Hier wird der Register Knopf erstellt
    registerButton.place(x=90, y=340)
    registerButton.config()

    exit1 = Button(text="Exit", width=10, command=quit, style='log.TButton')        #Hier der Exit Knopf
    exit1.place(x=310, y=425)
    chatgui.bind('<Shift_L><Return>', lambda event:quit())          #Dieses Mal wird einer Tastenkombination eine Funktion zugewiesen

    chatgui.mainloop()                                              #Dieser Command ist sehr wichtig, da er den Mainscreen ausführt und immer wieder aktualisiert

def userselection():                                                #Diese Funktion erzeugt das Chatfenster und die Eingabe
    user = therealusername                                          #Hier wird der Username im Chatbot gesetzt
    print(f"user has been selected: {user}")
    loginButton.destroy()                                           #Diese beide Zeilen zerstören die Login und Register Knöpfe
    registerButton.destroy()

    scrollbar = Scrollbar(chatgui, style='arrowless.Vertical.TScrollbar')   #Die Scrollbar wird hier mit dem arrowlees Style erstellt
    scrollbar.place(x=380, y=6, height=390)
    chatdisplay = Text(chatgui, yscrollcommand=scrollbar.set, bd=1, bg="#17202A", width=50, height=8, font=("Avenir", 14), foreground="#FFFFFF")    #Hier wird das Textfeld erstellt mit einer bestimmten Hintergund- und Textfarbe
    chatdisplay.place(x=6, y=6, width=w-26, height=h-110)                                                                                           #Dazu wird noch festgelegt, dass das Textfeld die Scrollbar verändern kann
    chatdisplay.configure(cursor="arrow", state=DISABLED)           #Diese Zeile verhindert, dass man direkt etwas im Textfeld verändern kann
    info2 = Label(chatgui, text="Press 'Enter' or press the 'Enter' button to enter your message \nPress 'Left Shift + Enter' or press the 'Exit' button to exit the Program", background=bg_color1, foreground=txt_color)
    info2.place(x=6, y=455)                                         #Das Info-Label wird hier erstellt
    scrollbar.config(command=chatdisplay.yview)                     #Dieser Command sorgt dafür, dass die Scrollbar funktioniert

    input = StringVar()                                             #Input ist eine Variable, die benutzt wird um den Input vom User zu holen
    inputentry = Entry(chatgui, textvariable=input, font=("Avenir", 12), background=bg_color2)      #Das hier ist das Input-Feld
    inputentry.place(x=6, y=400, width=w-100, height=50)
    inputentry.focus()                                              #Der .focus Command sorgt dafür, dass man dieses Feld nicht extra anklicken muss sondern, dass man direkt anfangen kann zu schreiben

    def delay():                                                    #Die delay-Funktion sorgt für das Verzögern beim Schließen des Fensters
        chatdisplay.configure(state=NORMAL)                         #Diese Zeile und sorgt dafür, dass der Bot etwas schreiben kann
        chatdisplay.insert(END, f"This window will now be destroyed. \nPlease do not press anything. \n")       #Hier verabschiedet sich der Bot
        chatdisplay.yview(END)                                      #Hier wird das Textfeld nach unten bewegt
        chatdisplay.configure(cursor="arrow", state=DISABLED)       #Hier wird wieder sicher gestellt das der User nichts im textfeld verändern kann
        chatgui.after(2500, quit)                                   #Diese Zeile löst die Zerstör-Funktion nach 2500ms aus

    exit2 = Button(text="Exit", width=10, command=delay, style='log.TButton')       #Exit Knopf, der delay ausführt, wird erstellt
    exit2.place(x=310, y=425)
    chatgui.bind('<Shift_L><Return>', lambda event:delay())         #Siehe Z.68

    web_input = ""                                                  #Variable für die Internetsuche

    def callback():                                                 #Diese Funktion wird aktiviert wen der User etwas eingibt
        inp = input.get()                                           #Hier wird die Eingabe abgefragt
        if inp == "":                                               #Diese if-clause schaut ob etwas im input ist, wenn nichts drin ist dann passiert auch nichts
            return
        else:
            print(f"Input has been confirmed and send as: {inp}")
            chatdisplay.configure(state=NORMAL)                     #Siehe Z.93
            chatdisplay.insert(END, f'{user}: {inp} \n')            #Hier wird der Userinput im Textfeld angezeigt
            chatdisplay.configure(cursor="arrow", state=DISABLED)   #Siehe Z.96
            inputentry.delete(0, END)                               #Diese Zeile lehrt das Eingabefeld
            res = get_response(inp)                                 #Hier holt sich der Bot eine Antwort aus dem chat.py Programm
            print(f"Response: {res}")
            restag = get_tag(inp)                                   #Hier holt sich der Bot den Tag der Antwort aus dem chat.py Programm 
            print(f"Tag: {restag}")
            if restag == "datetime":                                #Hier wird geschaut ob der Tag datetime ist
                time = datetime.now()                               #Wenn ja so wird eine Variable erstellt, die die Aktuelle Zeit und das Aktuelle Datum hat
                timenow = time.strftime("%H:%M")                    #Hier wird die Darstellungsweise von der Zeit festgelegt
                datenow = time.strftime("%d/%m/%Y")                 #Hier wird die Darstellungsweise vom Datum festgelegt
                chatdisplay.configure(state=NORMAL)                 #Siehe Z.93
                chatdisplay.insert(END, f'{bot_name}: The time is {timenow} and the date is \n{datenow} \n')        #Diese Zeile packt dann die Antwort in das Textfeld
                chatdisplay.yview(END)                              #Siehe Z.95
                chatdisplay.configure(cursor="arrow", state=DISABLED)       #Siehe Z.96
            elif restag == "":                                      #Diese Zeile schaut ob es einen Tag gibt
                global web_input                                    #wenn nicht dann wird mit Hilfe der globalen Variable web_input der Input gespeichert
                web_input = inp
                print(f'web_input: {web_input}')
                chatdisplay.configure(state=NORMAL)                 #Siehe Z.93
                chatdisplay.insert(END, f'{bot_name}: {res} \n')    #Hinter der Antwort die hier in das Textfeld getan wird, verbirgt sich die Antwort die by chat.py festgelegt ist, wenn kein Tag erkannt wurden ist
                chatdisplay.yview(END)                              #Siehe Z.95
                chatdisplay.configure(cursor="arrow", state=DISABLED)       #Siehe Z.96
            elif restag == "yes":                                   #Hier wird geschaut ob der Tag yes ist
                webbrowser.open(url + web_input)                    #Wenn dies stimmt öffnet das Programm eine Google-Suche im Browser mit dem vorherigen Input, der als web_input gespeichert ist
                print(f'web_input: {web_input}')
                chatdisplay.configure(state=NORMAL)                 #Siehe Z.93
                chatdisplay.insert(END, f'{bot_name}: Please wait a moment! \n')        #Mit dieser Zeile bittet der Bot um Geduld beim Öffnen der Website
                chatdisplay.yview(END)                              #Siehe Z.95
                chatdisplay.configure(cursor="arrow", state=DISABLED)       #Siehe Z.96
            elif restag == "no":    	                            #Wen der Tag no ist, erkennt diese Zeile das
                chatdisplay.configure(state=NORMAL)                 #Siehe Z.93
                chatdisplay.insert(END, f'{bot_name}: Ok, Please type something else. \n')      #Der Bot bittet dann, dass User etwas anderes schreibt
                chatdisplay.yview(END)                              #Siehe Z.95
                chatdisplay.configure(cursor="arrow", state=DISABLED)       #Siehe Z.96
            else:
                chatdisplay.configure(state=NORMAL)                 #Siehe Z.93
                chatdisplay.insert(END, f'{bot_name}: {res} \n')    #Wenn kein besonderer Tag erkannt wurde, antwortet der bot einfach mit der Antwort, die er aus chat.py bekommen hat
                chatdisplay.yview(END)                              #Siehe Z.95
                chatdisplay.configure(cursor="arrow", state=DISABLED)       #Siehe Z.96
                if restag == "goodbye" or restag == "thanks":       #Wenn die Tags goodbye oder thanks erkannt werden, löst das Programm dann noch die delay-Funktion aus
                    chatgui.after(1500, delay)
                    
    enter = Button(text="Enter", width=10, command=callback, style='log.TButton')       #Dieser Knopf ist für die Eingabe und führt deshalb die callback-Funktion aus
    enter.place(x=310, y=400)
    chatgui.bind('<Return>',lambda event:callback())                #Siehe Z.60

def quit():                                                         #Diese Funktion zerstört das ganze GUI
    chatgui.destroy()
    print("window has been destroyed")

def register():                                                     #Diese Funktion registriert die neuen User
    global username
    global password
    global username_entry                                           #Hier werden wieder globale Variablen festgelegt damit alle funktionieren und arbeiten können
    global password_entry
    global registerScreen

    registerScreen = Toplevel(chatgui)                              #Hier wird ein Popup erstellt wo sich der User registrieren kann
    registerScreen.geometry("300x250")
    registerScreen.title("Registration")
    registerScreen["background"] = bg_color1

    username = StringVar()                                          #Das sind wieder zwei Variablen um den Input vom User abzufragen
    password = StringVar()

    Label(registerScreen, text="", background=bg_color1).pack()     #Diese beiden leeren Labels sind da um Abstände zu machen
    Label(registerScreen, text="", background=bg_color1).pack()
    Label(registerScreen, text="Please enter an username and a password!", background=bg_color1, foreground=txt_color).pack()       #Dieses Label gibt dem User Anweisungen
    Label(registerScreen, text="", background=bg_color1).pack()     #Das hier ist wieder ein Abstandshalter
    Label(registerScreen, text="Username", background=bg_color1, foreground=txt_color).pack()       #Dieses Label ist für die Username Eingabe
    username_entry = Entry(registerScreen, textvariable=username)   #Das hier ist das Eingabefeld für den Username
    username_entry.pack()                                           #Der .pack Command platziert das Element mittig
    username_entry.focus()                                          #Siehe Z.90
    Label(registerScreen, text="Password", background=bg_color1, foreground=txt_color).pack()       #Hier wird das Label vom Password Eingabefeld erstellt
    password_entry = Entry(registerScreen, textvariable=password, show="*")         #Das Eingabefeld vom Password hat eine Besonderheit, nämlich die show-Eigenschaft, die in diesem Fall nur einen * zeigt für alles, was der User in gibt
    password_entry.pack()                                           #Siehe Z.184
    Label(registerScreen, text="", background=bg_color1).pack()     #Siehe Z.181
    Button(registerScreen, text="Register", width="10", command=registerUser, style='log.TButton').pack()       #Als letztes wird noch der Knopf erstellt, der die Registrierung auslöst
    registerScreen.bind('<Return>', lambda event:registerUser())    #Siehe Z.60

def registerUser():                                                 #Diese Funktion registriert den User
    if username.get() == "" or password.get() == "":                #Hier wird geschaut, ob es einen Input gibt
        tkinter.messagebox.showinfo(title="Info", message="No input recognized!")       #Hier wird ein Info-Fenster erstellt, was sagt, dass es kein Input gab
    else: 
        username_info = username.get()                              #Hier werden Username und Passwort angefordert
        password_info = password.get()

        file = open(username_info, "w")                             #Hier wird eine Datei erstellt, die den Username als Namen hat
        file.write(username_info+"\n")                              #Hier wird der Username in die Datei geschrieben
        file.write(password_info)                                   #Und hier das Password in der nächsten Zeile
        file.close()                                                #Hier wird die Datei wieder geschlossen

        username_entry.delete(0, END)                               #Mit diesen beiden Zeilen werden die Eingabefelder geleert
        password_entry.delete(0, END)

        tkinter.messagebox.showinfo(title="Info", message="Registration succesful!")        #Diese Zeile erstellt ein Info-Fenster, was die Registrierung bestätigt
        registerScreen.destroy()                                    #Hier wird das Registrierungsfenster zerstört

def login():                                                        #Diese Funktion kümmert sich um das Einloggen
    global loginScreen
    global username_verify
    global password_verify                                          #Zuerst werden wieder globale Variablen erstellt
    global username_entry1
    global password_entry1

    loginScreen = Toplevel(chatgui)                                 #Dann wird ein Popup erstellt, was sich um den Login kümmert
    loginScreen.title("Login")
    loginScreen.geometry("300x250")
    loginScreen["background"] = bg_color1

    username_verify = StringVar()                                   #Siehe Z.175
    password_verify = StringVar()

    Label(loginScreen, text="", background=bg_color1).pack()        #Siehe Z.178
    Label(loginScreen, text="", background=bg_color1).pack()
    Label(loginScreen, text="Please enter your username and password to login!", background=bg_color1, foreground=txt_color).pack()         #Siehe Z.180
    Label(loginScreen, text="", background=bg_color1).pack()        #Siehe Z.181
    Label(loginScreen, text="Username", background=bg_color1, foreground=txt_color).pack()          #Siehe Z.182
    username_entry1 = Entry(loginScreen, textvariable=username_verify)          #Siehe Z.183
    username_entry1.pack()                                          #Siehe Z.184
    username_entry1.focus()                                         #Siehe Z.90
    Label(loginScreen, text="Password", background=bg_color1, foreground=txt_color).pack()          #Siehe Z.186
    password_entry1 = Entry(loginScreen, textvariable=password_verify, show = "*")          #Siehe Z.187
    password_entry1.pack()                                          #Siehe Z.184
    Label(loginScreen, text="", background=bg_color1).pack()        #Siehe Z.181
    Button(loginScreen, text="Login", width="10", command=loginUser, style='log.TButton').pack()        #Als letztes wird noch der Knopf erstellt, der den User eingeloggt
    loginScreen.bind('<Return>', lambda event:loginUser())          #Siehe Z.60

def loginUser():                                                    #Diese Funktion loggt den User ein
    global therealusername                                          #Hier wird wieder eine Globale Variable erstellt

    username_input = username_verify.get()                          #Mit diesen beiden Zeilen wird der Input vom User abgefragt
    password_input = password_verify.get()

    username_entry1.delete(0, END)                                  #Diese beiden Zeilen leeren die Eingabefelder
    password_entry1.delete(0, END)

    list_of_files = os.listdir()                                    #Hier wird eine Variable erstellt, die aus einer Liste an Dateien besteht fom aktuellen Path
    if username_input in list_of_files:                             #Diese If-Clause schaut, ob der angegebene Username in der Liste von Dateien ist
        file1 = open(username_input, "r")                           #Wenn ja, dann wird hier diese Datei geöffnet
        verify = file1.read().splitlines()                          #Hier werden die beiden Zeilen der Datei getrennt gelesen
        if password_input in verify:                                #Diese If-Clause überprüft, ob das angegebene Passwort mit dem gespeichertem übereinstimmt
            tkinter.messagebox.showinfo(title="Info", message="Login succesful!")       #Ist dies der Fall, so kommt ein Info-Fenster was sagt, dass das Einlogen funktioniert hat
            therealusername = username_input                        #Hier wird dann der Username gespeichert, damit der Bot dann die Eingaben als die vom Username bezeichnen kann
            loginScreen.destroy()                                   #Hier wird das Login-Fenster zerstört
            userselection()                                         #Und die Funktion userselection() wird ausgeführt
        else:
            tkinter.messagebox.showinfo(title="Info", message="Password is wrong!")         #Wenn das Passwort falsch ist, wird ein Info-Fenster erstellt, das dies sagt
            password_entry1.delete(0, END)                          #Und die Eingabe vom User im Feld vom Passwort wird gelöscht
    else:
        tkinter.messagebox.showinfo(title="Info", message="Username is wrong!")         #Falls keine Datei mit dem Username gefunden wird, wird ein Info-Fenster erstellt, das dies sagt
        username_entry1.delete(0, END)                              #Diese beiden Zeilen leeren die Eingabefelder
        password_entry1.delete(0, END)
        loginScreen.destroy()
        login()

mainscreen()                                                        #Um das Programm zu starten, wird einmal die Funktion mainscreen() ausgeführt