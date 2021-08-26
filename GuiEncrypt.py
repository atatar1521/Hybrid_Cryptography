import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
from mainEncrypt import *


def encryptionChoice():
    ciphertext = main(user_text.get())
    createLabel(ciphertext)


def createLabel(ciphertext):
    label3 = tk.Label(root, text=ciphertext, width=40, bg="white")
    # adding the font features to the label
    label3.config(font=bold_font)
    # placing the label in the canvas
    canvas.create_window(200, 350, window=label3)


# Creating a window
root = tk.Tk()
# For changing the title of the title bar
root.title("Text Encryptor- Decryptor")
# To set the dimensions of the window
root.geometry("400x500")
# To set whether we can resize the window or not.The below line doesn't allow the resizing of the window.
root.resizable(width=FALSE, height=FALSE)
# Creating a canvas
canvas = tk.Canvas(root, height=500, width=400, bg="lightgreen")
# Set the family,size and style of the font
bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
# Creating a label with a text and attaching it to the root

label1 = tk.Label(root, text="Enter the Text", width=20, bg="lightgreen")
# adding the font features to the label
label1.config(font=bold_font)
# placing the label in the canvas
canvas.create_window(200, 100, window=label1)
# Text Area
user_text = tk.StringVar()
entry = tk.Entry(root, width=40, textvariable=user_text)
canvas.create_window(200, 150, window=entry)
# Creating a label with a text and attaching it to the root
label2 = tk.Label(root, text="Choose an Operation", width=25, bg="lightgreen")
# adding the font features to the label
label2.config(font=bold_font)
# placing the label in the canvas
canvas.create_window(200, 200, window=label2)
# Tkinter Variable
v = tk.IntVar()
# Radio Button for Encryption
label4 = tk.Button(root, text="Encrypt", padx=20, command=encryptionChoice, bg="lightgreen")
label4.config(font=bold_font)
canvas.create_window(200, 250, window=label4)
# # Creating a label with a text and attaching it to the root
label5 = tk.Label(root, text="Converted Text ", width=20, bg="lightgreen")
# adding the font features to the label
label5.config(font=bold_font)
# placing the label in the canvas
canvas.create_window(200, 300, window=label5)
canvas.pack()


root.mainloop()
