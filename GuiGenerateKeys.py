import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
from mainEncrypt import *

def choice():
    publicKey, publicPQ= publicKeyGeneration()
    list1 =[]
    list1.append(publicKey[0])
    list1.append(publicKey[1])
    filename1 = "filePublicKey.csv"
    itemsToFile= [list1]
    with open(filename1, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows(itemsToFile)
    list2 =[]
    list2.append(publicPQ[0])
    list2.append(publicPQ[1])
    filename2 = "filePublicPQ.csv"
    itemsToFile= [list2]
    with open(filename2, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows(itemsToFile)
    createLabel(publicKey)
def createLabel(ciphertext):
    label3 = tk.Label(root, text=ciphertext, width=40, bg="white")
    # adding the font features to the label
    label3.config(font=bold_font)
    # placing the label in the canvas
    canvas.create_window(200, 100, window=label3)

# Creating a window
root = tk.Tk()
# For changing the title of the title bar
root.title("Generate Public Key")
# To set the dimensions of the window
root.geometry("400x200")
# To set whether we can resize the window or not.The below line doesn't allow the resizing of the window.
root.resizable(width=FALSE, height=FALSE)
# Creating a canvas
canvas = tk.Canvas(root, height=200, width=400, bg="lightgreen")
# Set the family,size and style of the font
bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
# Creating a label with a text and attaching it to the root
label4 = tk.Button(root, text="Generate Public Key", padx=20, command=choice, bg="lightgreen")
label4.config(font=bold_font)
canvas.create_window(200, 50, window=label4)
canvas.pack()


root.mainloop()