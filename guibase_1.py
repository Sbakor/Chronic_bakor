#Sets a basic GUI to start the game.

#imports
from tkinter import *

#defining game variables
Character_Name = "No Character"

#create a character function
def createcharacter(event):
    char_root = Tk()

    char_name = Label(char_root, text="Enter your name")
    char_entry = Entry(char_root)
    char_name.grid(row=0, column=1)
    char_entry.grid(row=0, column=2)

    char_root.mainloop()


#creates the root main window
root = Tk()
charname_label1 = Label(root, text="Character Name")
charname_label2 = Label(root, text="Null") #input from create character function will go here eventually
charname_label1.grid(row=0, column=1)
charname_label2.grid(row=0, column=2)

#create character button
button1 = Button(root, text="Create Character", fg="red")
button1.bind("<Button-1>", createcharacter)
button1.grid(row=10, column=1, sticky=W)

button2 = Button(root, text="Inventory", fg="green")
button3 = Button(root, text="Stats", fg="orange")
button4 = Button(root, text="Fight!", fg="blue")


button2.grid(row=10, column=2, sticky=W)
button3.grid(row=10, column=3, sticky=W)
button4.grid(row=10, column=4, sticky=E)


root.mainloop()