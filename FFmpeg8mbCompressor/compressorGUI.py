import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import font
import compressor
import os
import random

root = tk.Tk()
root.title('File Compressor')
root.resizable(True, True)
root.geometry('500x200')

#default file size
fileCompressSize = 8
newDir = 'Finished Compressed Files'
parentDir = os.getcwd()
path = os.path.join(parentDir, newDir)
if not os.path.isdir(path):
    os.mkdir(path)


def select_file():
    filetypes = (
        ('All files', '*.*'),
        ('mp4 files', '*.mp4'),
        ('jpg files', '*.jpg'),
        ('png files', '*.png')
    )

    filename = fd.askopenfilename(
        title = 'Open a file',
        initialdir = '/',
        filetypes = filetypes
        )
    if filename:
        fileExtension = filename.split('.')[-1]
        print(os.getcwd())
        print(filename)
        randNum = random.randrange(0, 1000)
            
        compressor.compress_video(filename,f'{path}\compressed_{randNum}.{fileExtension}', fileCompressSize *1000 , fileExtension)
        message = 'Successful Compression'
    else:
        message = 'No File Selected'
    showinfo(
        title = 'File Compressor',
        message = message
    )


def selFileSize(size):
    labelSize ['text'] = 'Current Size: '+ str(size)+"mb"
    global fileCompressSize
    fileCompressSize = size



labelTitle = tk.Label(text="Welcome to FFMPEG Compressor", fg="black")
labelSize = tk.Label(text="Select a file size.", fg="black")
labelInfo = tk.Label(text="*PNGs will compress as best as possible", fg="black")



open_button = ttk.Button(
    root,
    text = 'Open a File',
    command = select_file
)

size8mb = ttk.Button(
    root,
    text = '8mb',
    command =  lambda: selFileSize(8)
)
size50mb = ttk.Button(
    root,
    text = '50 mb',
    command = lambda: selFileSize(50)
)

labelTitle.pack()
f = font.Font(labelTitle, labelTitle.cget("font"))
f.configure(underline=True)
labelTitle.configure(font=(f,20))
labelSize.pack()
labelInfo.pack()
size8mb.pack()
size50mb.pack()
open_button.pack(expand=True)


root.mainloop()


