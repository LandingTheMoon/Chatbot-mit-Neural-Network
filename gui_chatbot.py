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

url = "https://www.google.com/search?q="

def mainscreen():
    global chatgui
    global loginButton
    global registerButton
    global info1
    global exit1
    global w
    global h

    w = 400
    h = 500
    chatgui = Tk()
    chatgui.title("Chatbot by Louis and Jan")
    chatgui.configure(width=w, height=h)
    chatgui.resizable(width=False, height=False)
    
    theme = Style()
    theme.theme_use('vista')

    stylegui = Style(chatgui)
    stylegui.configure('.', font=("Avenir", 9))

    stylescrollbar = Style(chatgui)
    stylescrollbar.layout('arrowless.Vertical.TScrollbar', [('Vertical.Scrollbar.trough', {'children': [('Vertical.Scrollbar.thumb', {'expand': '1', 'sticky': 'nswe'})], 'sticky': 'ns'})])
    
    stylebutto2 = Style(chatgui)
    stylebutto2.configure('red.TButton', height="1")

    stylebutton = Style(chatgui)
    stylebutton.configure('log.TButton', height="2")

    logoimage = Image.open("logo.png")
    logoimageresize = logoimage.resize((125,90), Image.ANTIALIAS)
    imageneu = ImageTk.PhotoImage(logoimageresize)
    logo = Label(chatgui, image=imageneu)
    logo.place(x=137, y=70)

    welcome = Label(chatgui, text="Welcome to our Chatbot!", font="Avenir 16", foreground="Red")
    welcome.place(x=80, y=35)
    welcome.config()

    loginButton = Button(text="Login", width="30", command=login, style='log.TButton')
    loginButton.place(x=90, y=175)
    loginButton.config()

    registerButton = Button(text="Register", width="30", command=register, style='log.TButton')
    registerButton.place(x=90, y=225)
    registerButton.config()

    Label(text="")
    info1 = Label(chatgui, text="Press 'Enter' or press the 'Submit' button to submit your Username \n Press 'Left Shift + Enter' or press the 'Exit' button to exit the Program")
    info1.place(x=5, y=300)

    exit1 = Button(text="Exit", width=10, command=quit)
    exit1.place(x=310, y=425)
    chatgui.bind('<Shift_L><Return>', lambda event:quit())

    chatgui.mainloop()

def userselection():
    user = therealusername
    print(f"user has been selected: {user}")
    loginButton.destroy()
    registerButton.destroy()

    scrollbar = Scrollbar(chatgui, style='arrowless.Vertical.TScrollbar')
    scrollbar.place(x=380, y=6, height=390)
    chatdisplay = Text(chatgui, yscrollcommand=scrollbar.set, bd=1, bg="black", width=50, height=8, font=("Avenir", 14), foreground="#FFFFFF")
    chatdisplay.place(x=6, y=6, width=w-26, height=h-110)
    chatdisplay.configure(cursor="arrow", state=DISABLED)
    info2 = Label(chatgui, text="Press 'Enter' or press the 'Enter' button to enter your message \n Press 'Left Shift + Enter' or press the 'Exit' button to exit the Program")
    info2.place(x=6, y=455)
    scrollbar.config(command=chatdisplay.yview)

    input = StringVar()

    inputentry = Entry(chatgui, textvariable=input, font=("Avenir", 20))
    inputentry.place(x=6, y=400, width=w-100, height=50)
    inputentry.focus()

    def delay():
        chatdisplay.configure(state=NORMAL)
        chatdisplay.insert(END, f"This window will now be dertoyed. Please do not press anything. \n")
        chatdisplay.yview(END)
        chatdisplay.configure(cursor="arrow", state=DISABLED)
        chatgui.after(2500, quit)

    exit2 = Button(text="Exit", width=10, command=delay)
    exit2.place(x=310, y=425)
    chatgui.bind('<Shift_L><Return>', lambda event:delay())

    web_input = ""

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
            if restag == "datetime":
                time = datetime.now()
                timenow = time.strftime("%H:%M")
                datenow = time.strftime("%d/%m/%Y")
                chatdisplay.configure(state=NORMAL)
                chatdisplay.insert(END, f'{bot_name}: The time is {timenow} and the date is {datenow} \n')
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
                if restag == "goodbye":
                    chatgui.after(1500, delay)
                    
    enter = Button(text="Enter", width=10, command=callback)
    enter.place(x=310, y=400)
    chatgui.bind('<Return>',lambda event:callback())

def quit():
    chatgui.destroy()
    print("window has been destroyed")

def register():
    global username
    global password
    global username_entry
    global password_entry
    global registerScreen

    registerScreen = Toplevel(chatgui)
    registerScreen.geometry("300x250")
    registerScreen.title("Registration")

    username = StringVar()
    password = StringVar()

    Label(registerScreen, text="Please enter an username and a password!").pack()
    Label(registerScreen, text="").pack()
    Label(registerScreen, text="Username").pack()
    username_entry = Entry(registerScreen, textvariable=username)
    username_entry.pack()
    username_entry.focus()
    Label(registerScreen, text="Password").pack()
    password_entry = Entry(registerScreen, textvariable=password, show="*")
    password_entry.pack()
    Label(registerScreen, text="").pack()
    Button(registerScreen, text="Register", width="10", command=registerUser, style='reg.TButton').pack()
    registerScreen.bind('<Return>', lambda event:registerUser())

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

def login():
    global loginScreen
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1

    loginScreen = Toplevel(chatgui)
    loginScreen.title("Login")
    loginScreen.geometry("300x250")

    username_verify = StringVar()
    password_verify = StringVar()

    Label(loginScreen, text="Please enter your username and password to login!").pack()
    Label(loginScreen, text="").pack()
    Label(loginScreen, text="Username").pack()
    username_entry1 = Entry(loginScreen, textvariable=username_verify)
    username_entry1.pack()
    username_entry1.focus()
    Label(loginScreen, text="Password").pack()
    password_entry1 = Entry(loginScreen, textvariable=password_verify, show = "*")
    password_entry1.pack()
    Label(loginScreen, text="").pack()
    Button(loginScreen, text="Login", width="10", command=loginUser, style='reg.TButton').pack()
    loginScreen.bind('<Return>', lambda event:loginUser())

def loginUser():
    global therealusername

    username_input = username_verify.get()
    password_input = password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

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

mainscreen()