import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
from decryptOptions import *
from writingFiles import *


def decryptionChoice():
    plainText = mainDecrypt()
    createLabel(plainText)


def filesDecryption():
    decryptedText = mainDecrypt()
    txtWritingFile(decryptedText.encode('utf-8'))
    createLabel("File decrypted")


def createLabel(plaintext):
    label3 = tk.Label(root, text=plaintext, width=40, bg="white")
    # adding the font features to the label
    label3.config(font=bold_font)
    # placing the label in the canvas
    canvas.create_window(200, 200, window=label3)


# Creating a window
root = tk.Tk()
# For changing the title of the title bar
root.title("Text Encryptor-Decryptor")
# To set the dimensions of the window
root.geometry("400x300")
# To set whether we can resize the window or not.The below line doesn't allow the resizing of the window.
root.resizable(width=FALSE, height=FALSE)
# Creating a canvas
canvas = tk.Canvas(root, height=300, width=400, bg="lightgreen")
# Attaching the canvas
canvas.pack()
# Set the family,size and style of the font
bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
# Creating a label with a text and attaching it to the root
label2 = tk.Label(root, text="Choose an Operation", width=25, bg="lightgreen")
# adding the font features to the label
label2.config(font=bold_font)
# placing the label in the canvas
canvas.create_window(200, 50, window=label2)
# Tkinter Variable
v = tk.IntVar()
# Radio Button for Decryption
label6 = tk.Button(root, text="Decrypt Text", padx=20, command=decryptionChoice, bg="lightgreen")
label6.config(font=bold_font)
canvas.create_window(200, 100, window=label6)
label9= tk.Button(root, text="Decrypt File", padx=20, command=filesDecryption, bg="lightgreen")
label9.config(font=bold_font)
canvas.create_window(200, 150, window=label9)
# Creating a label with a text and attaching it to the root
label7 = tk.Label(root, text="Converted Text ", width=20, bg="lightgreen")
# adding the font features to the label
label7.config(font=bold_font)
# placing the label in the canvas
canvas.create_window(200, 200, window=label7)

root.mainloop()
