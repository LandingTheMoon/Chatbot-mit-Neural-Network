from tkinter import *
import numpy as np
from chat import get_response, get_tag, bot_name
from datetime import datetime

w = 400
h = 500
chatgui = Tk()
chatgui.title("Chatbot by Louis and Jan")
chatgui.configure(width=w, height=h)
chatgui.resizable(width=False, height=False)

def userselection():
    user = username.get()
    if user == "":
        return
    else:
        print(f"user has been selected: {user}")
        usernameentry.destroy()
        label_user.destroy()
        submit.destroy()
        info1.destroy()
        exit1.destroy()

        chatdisply = Text(chatgui, bd=1, bg="black", width=50, height=8, font=("Arial", 14), foreground="#FFFFFF")
        chatdisply.place(x=6, y=6, width=w-12, height=h-110)
        chatdisply.configure(cursor="arrow", state=DISABLED)
        info2 = Label(chatgui, text="Press 'Enter' or press the 'Enter' button to enter your message \n Press 'Left Shift + Enter' or press the 'Exit' button to exit the Program")
        info2.place(x=6, y=455)

        input = StringVar()

        inputentry = Entry(chatgui, textvariable=input)
        inputentry.place(x=6, y=400, width=w-100, height=50)
        inputentry.focus()

        def callback():
            inp = input.get()
            if inp == "":
                return
            else:
                print(f"Input has been confirmed and send as: {inp}")
                chatdisply.configure(state=NORMAL)
                chatdisply.insert(END, f'{user}: {inp} \n')
                chatdisply.configure(cursor="arrow", state=DISABLED)
                inputentry.delete(0, END)
                res = get_response(inp)
                print(f"Response: {res}")
                restag = get_tag(inp)
                print(f"Tag: {restag}")
                if restag == "datetime":
                    time = datetime.now()
                    timenow = time.strftime("%H:%M")
                    datenow = time.strftime("%d/%m/%Y")
                    chatdisply.configure(state=NORMAL)
                    chatdisply.insert(END, f'{bot_name}:The time is {timenow} and the date is {datenow} \n')
                    chatdisply.configure(cursor="arrow", state=DISABLED)
                else:
                    chatdisply.configure(state=NORMAL)
                    chatdisply.insert(END, f'{bot_name}: {res} \n')
                    chatdisply.configure(cursor="arrow", state=DISABLED)
                    if restag == "goodbye":
                        chatgui.after(1500, delay)

        def delay():
            chatdisply.configure(state=NORMAL)
            chatdisply.insert(END, f"This window will now be dertoyed. Please do not press anything.")
            chatdisply.configure(cursor="arrow", state=DISABLED)
            chatgui.after(2500, quit)

        exit2 = Button(text="Exit", width=10, command=delay)
        exit2.place(x=310, y=425)
        chatgui.bind('<Shift_L><Return>', lambda event:delay())
        

        enter = Button(text="Enter", width=10, command=callback)
        enter.place(x=310, y=400)
        chatgui.bind('<Return>',lambda event:callback())

welcome = Label(chatgui, text="Welcome to our Chatbot \n Enter a Username to start", font="Avenir 16", fg="Red")
welcome.place(x=50, y=5)
welcome.config()
label_user = Label(chatgui, text="User Name:")
label_user.place(x=5, y=135)
username = StringVar()
usernameentry = Entry(chatgui, bd=3, textvariable=username)
usernameentry.place(x=75, y=133, width=200, height=25)
usernameentry.focus()
submit = Button(chatgui, text="Submit", width=10, command=userselection)
submit.place(x=280, y=132)
chatgui.bind('<Return>',lambda event:userselection())
info1 = Label(chatgui, text="Press 'Enter' or press the 'Submit' button to submit your Username \n Press 'Left Shift + Enter' or press the 'Exit' button to exit the Program")
info1.place(x=5, y=160)

def quit():
    chatgui.destroy()
    print("window has been destroyed")

exit1 = Button(text="Exit", width=10, command=quit)
exit1.place(x=310, y=425)
chatgui.bind('<Shift_L><Return>', lambda event:quit())

chatgui.mainloop()