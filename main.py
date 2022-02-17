from tkinter import *
import pyperclip
import random
import string

def generator():
    password = ""
    for x in range(0, 8):
        password = password + random.choice(string.ascii_lowercase + (string.ascii_uppercase if options.find("u") < 0 else "") + (string.digits if options.find("d") < 0 else "") + (string.punctuation if options.find("p") < 0 else ""))
    passwordv.set(password)

def toggleU():
    global options
    if toggleup.config('relief')[-1] == 'sunken':
        toggleup.config(relief="raised")
        options = options.replace("u", "")
    else:
        toggleup.config(relief="sunken")
        options = options + "u"

def toggleD():
    global options
    if toggledigit.config('relief')[-1] == 'sunken':
        toggledigit.config(relief="raised")
        options = options.replace("d", "")
    else:
        toggledigit.config(relief="sunken")
        options = options + "d"

def toggleP():
    global options
    if togglepuc.config('relief')[-1] == 'sunken':
        togglepuc.config(relief="raised")
        options = options.replace("p", "")
    else:
        togglepuc.config(relief="sunken")
        options = options + "p"

def copyPass():
    pyperclip.copy(passwordv.get())

window = Tk()
window.geometry("400x250")
window.resizable(0,0)
window.title("8 letters Password Generator")
Label(window, text="Password Generator", font="arial 15 bold").pack()
passwordv = StringVar()
Button(window, text = "GENERATE PASSWORD!!!" , command = generator).pack(pady= 5)
Entry(window , textvariable = passwordv).pack()
Button(window, text = 'COPY TO CLIPBOARD', command = copyPass).pack(pady=5)
options = ""
toggleup = Button(text="Upper", width=12, relief="raised", command=toggleU)
toggleup.place(x=25, y=180)
toggledigit = Button(text="Digits", width=12, relief="raised", command=toggleD)
toggledigit.place(x=150, y=180)
togglepuc = Button(text="Special", width=12, relief="raised", command=toggleP)
togglepuc.place(x=280, y=180)
window.mainloop()