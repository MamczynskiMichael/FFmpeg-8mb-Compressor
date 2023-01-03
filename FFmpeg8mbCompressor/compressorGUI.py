import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import font
import compressor
import os

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

    filename = fd.askopenfilenames(
        title = 'Open a file',
        initialdir = '/',
        filetypes = filetypes
        )
    if filename:
        for fileLocation in filename:
            file = os.path.basename(fileLocation)
            fileTitle = file.split('.')
            fileEnd = fileTitle[-1]
            fileTitle = fileTitle[0]
            compressor.compress_video(fileLocation,f'{path}\{fileTitle}_%03d.{fileEnd}', fileCompressSize *1000 , fileEnd)
            

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


