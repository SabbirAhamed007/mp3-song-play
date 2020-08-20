import os
from tkinter.filedialog import askdirectory

import pygame
from mutagen.id3 import ID3
import tkinter
from tkinter import *

root = Tk()
root.minsize(300, 300)

listofsongs = []
realnames = []
index = 0

def directorychooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endwith(".mp3"):

            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])

            listofsongs.append(files)


    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()


label = Label(root, text='Music Player')
label.pack()

listbox = Listbox(root)
listbox.pack()

#listofsongs.reverse()
realnames.reverse()

for item in realnames:
    listbox.insert(0, item)

realnames.reverse()

#listofsongs.reverse()

nextbutton = Button(root,text = 'Next Song')
nextbutton.pack()

previousbutton = Button(root,text = 'Previous Song')
previousbutton.pack()

stopbutton = Button(root,text = 'Stop Music')
stopbutton.pack()


directorychooser()

root.mainloop()


