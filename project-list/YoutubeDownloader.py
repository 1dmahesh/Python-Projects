# This program will download youtube videos for you, with options to select the resolution.

from pytube import YouTube
from sys import argv
from pytube import *
from tkinter import *
import tkinter as tk
from tkinter import messagebox
path = ".\\YTDownloads\\"


# Here we will create a Display window.
root=tk.Tk()
root.geometry('800x500')
root.resizable(0,0)
root.title("Video Downloaded")
tk.Label(root,text = 'Youtube Video Downloaded',fg= "red" ,font ='Rockwell 26 bold').pack(pady=10)
tk.Label(root, text = 'Please select the video resolution to download', font='raavi 20 bold').place(x= 100 , y = 200)


link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 310 , y = 100)
link_enter = Entry(root, width = 80,textvariable = link).place(x= 160 , y = 140)



# Below functions will check what resolution a user wants.
def Download_240():    
     print("This will download video from Youtube") 
     url =YouTube(link.get())
     video = url.streams.filter(res='240p').first()
     video.download(str(path))
     return messagebox.showinfo('message','Hurray,Task Completed!')

def Download_360():    
     print("This will download video from Youtube") 
     url =YouTube(link.get())
     video = url.streams.filter(res='360p').first()
     video.download(str(path))
     return messagebox.showinfo('message','Hurray,Task Completed!')

def Download_480():    
     print("This will download video from Youtube") 
     url =YouTube(link.get())
     video = url.streams.filter(res='480p').first()
     video.download(str(path))
     return messagebox.showinfo('message','Hurray,Task Completed!')

def Download_720():    
     print("This will download video from Youtube") 
     url =YouTube(link.get())
     video = url.streams.filter(res='720p').first()
     video.download(str(path))
     return messagebox.showinfo('message','Hurray,Task Completed!')

def Download_1080():    
     print("This will download video from Youtube") 
     url =YouTube(link.get())
     video = url.streams.filter(res='1080p').first()
     video.download(str(path))
     return messagebox.showinfo('message','Hurray,Task Completed!')

# These are all buttons for all the available resolutions.  
def buttons():
    button_s = tk.Button(root , text="240p", fg="green",command=Download_240).place(x = 180, y = 280, bordermode=OUTSIDE, height= 30)
    button_m = tk.Button(root, text="360p",fg="blue",command=Download_360).place(x = 280, y = 280, bordermode=OUTSIDE, height= 30)
    button_m = tk.Button(root, text="480p",fg= "red",command=Download_480).place(x = 380, y = 280, bordermode=OUTSIDE, height= 30)
    button_m = tk.Button(root, text="720p",fg= "yellow",bg="black",command=Download_720).place(x = 480, y = 280, bordermode=OUTSIDE, height= 30)
    button_m = tk.Button(root, text="1080p",fg="magenta",command=Download_1080).place(x = 580, y = 280, bordermode=OUTSIDE, height= 30)

buttons()
mainloop()