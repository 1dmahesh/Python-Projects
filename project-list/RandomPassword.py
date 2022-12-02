# This is a GUI Programm it will generate a random password for you.

from tkinter import *
import tkinter as tk
import string
import random
text = list(string.ascii_letters + string.digits + "!@#$%^&*()\/")

# From this we will create a Display Window.
root=tk.Tk()
root.geometry('800x500')
root.resizable(0,0)
root.title("Password Generator")
tk.Label(root,text = 'Random Password Generator', font ='Rockwell 26 bold').pack(pady=10)

password_store=tk.IntVar()

tk.Label(root, text = 'Paste The Number of characters', font = 'Consolas 18 bold',).place(x= 200 , y = 80)
pass_enter=tk.Entry(root, width = 15,textvariable = password_store).place(x = 310, y = 140)

# This function below will generate and show that password to use in the display.
def pass_genetaor():
    namevar=password_store.get()
    password_length = namevar
    random.shuffle(text)
    password = []
    for i in range(password_length):
        password.append(random.choice(text))

    random.shuffle(password)

    password = "".join(password)
    passstore = tk.StringVar()
    print("Your New password is: " + str(password))
    e = Entry(root, width = 50,textvariable=passstore, font = 'Raavi 12 bold').place(x = 200, y = 340, bordermode=OUTSIDE, height= 30)
   
    passstore.set(password)
    s = passstore.get()

button = Button(root,text = 'Generate Password', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2,command = pass_genetaor ).place(x=270 ,y = 200)   

root.mainloop()
