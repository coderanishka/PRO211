import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from playsound import playsound
import pygame
from pygame import mixer
import os
import ftplib
from ftplib import FTP
import time
import ntpath
from pathlib import Path

PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name = None
listbox = None
filePathLabel = None
global soung_counter
song_counter = 0

def browseFiles():
    global listbox
    global filePathLabel
    global song_counter

    try:
        fileName = filedialog.askopenfilename()
        HOSTNAME = '127.0.0.1'
        USERNAME = 'lftpd'
        PASSWORD = 'lftpd'

        ftp_server = FTP(HOSTNAME, USERNAME, PASSWORD)
        ftp_server.encoding = 'utf-8'
        ftp_server.cwd('share_files')
        fname = ntpath.basename(fileName)
        with open(fileName, 'rb') as file:
            ftp_server.storbinary(f'STOR {fname}', file)
        ftp_server.dir()
        ftp_server.quit()
    except FileNotFoundError:
        print('Cancel Button Pressed')

def play():
    global song_selected
    song_selected = listbox.get(ANCHOR)
    pygame
    mixer.init()
    mixer.music.load('shared_files/' + song_selected)
    mixer.music.play()
    if(song_selected != ''):
        infoLabel.configure(text = 'Now Playing: ' + song_selected)
    else:
        infoLabel.configure(text = '')

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/' + song_selected)
    mixer.music.play()
   

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/' + song_selected)
    mixer.music.pause()

    
def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/' + song_selected)
    mixer.music.pause()


def musicWindow():
    global song_counter
    global filePathLabel
    global listbox
    global infoLabel


    window = Tk()
    window.title('music Window')
    window.geometry("300x400")
    window.configure(bg = 'purple')

    selectlabel = Label(window, text = 'Select Song', bg = 'purple', font = ('Calbiri', 8))
    selectlabel.place(x = 2, y = 1)

    listbox = Listbox(window, height = 10, width = 39, activestyle = 'dotbox', bg = 'purple', borderwidth = 2, font = ('Calbiri', 10))
    listbox.place(x = 10, y = 10)

    for file in os.listdir('shared_files'):
        filename = os.fsdecode(file)
        listbox.insert(song_counter, filename)
        song_counter = song_counter + 1


    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1, relx = 1)
    scrollbar1.config(command = listbox.yview)

    PlayButton = Button(window, text = 'Play', width = 10, bd = 1, bg = 'Skyblue', font = ('Calbiri', 10), command = play)
    PlayButton.place(x = 30, y = 200)

    Stop = Button(window, text = 'Stop', width = 10, bd = 1, bg = 'Skyblue', font = ('Calbiri', 10), command = stop)
    Stop.place(x = 200, y = 200)

    Upload = Button(window, text = 'Upload', width = 10, bd = 1, bg = 'Skyblue', font = ('Calbiri', 10))
    Upload.place(x = 30, y = 250)

    Resume = Button(window, text = 'Resume', width = 10, bd = 1, bg = 'Skyblue', font = ('Calbiri', 10), command = resume)
    Resume.place(x = 30, y = 300)

    Pause = Button(window, text = 'Pause', width = 10, bd = 1, bg = 'Skyblue', font = ('Calbiri', 10), command = pause)
    Pause.place(x = 200, y = 300)

    Download = Button(window, text = 'Download', width = 10, bd = 1, bg = 'Skyblue', font = ('Calbiri', 10))
    Download.place(x = 200, y = 250)

    infoLabel = Label(window, text = '', fg = 'blue', font = ('Calbiri', 8))
    infoLabel.place(x = 4, y = 280)
    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    musicWindow()

setup()