import json
from difflib import get_close_matches
import tkinter
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import scrolledtext
import sys
import os

data = json.load(open(os.path.join(sys.path[0], "defs.json"), "r"))

#Prints the defintions of a given word
def definition():
    word = e1.get().lower()
    text.config(state = "normal")
    text.delete(1.0, tkinter.END)
    
    #Case where the word is correctly spelled and in data
    if (word in data):
        allDefinition = data[word]
        enum = enumerate(allDefinition,1)

        temp1 = word.title()
        header.config(text = temp1)
        for definition in enum:
            temp2 = f"{definition[0]} - {definition[1]}\n\n"
            text.insert(tkinter.END, temp2)
        text.config(state = "disabled")

    #Case where the word is a proper noun (Manchester, Paris, etc.)
    elif (word.title() in data):
        allDefinition = data[word.title()]
        enum = enumerate(allDefinition,1)

        temp1 = word.title()
        header.config(text = temp1)
        for definition in enum:
            temp2 = f"{definition[0]} - {definition[1]}\n\n"
            text.insert(tkinter.END, temp2)
        text.config(state = "disabled")

    #Case where the user enters acronyms (NASA,UN, etc.)
    elif (word.upper() in data):
        allDefinition = data[word.upper()]
        enum = enumerate(allDefinition,1)

        temp1 = word.title()
        header.config(text = temp1)
        for definition in enum:
            temp2 = f"{definition[0]} - {definition[1]}\n\n"
            text.insert(tkinter.END, temp2)
        text.config(state = "disabled")

    #Case where the word is spelled incorrectly
    else:
        matches = get_close_matches(word,data)

        #Given word does not exist (has no matches)
        if (len(matches) == 0):
            text.insert(tkinter.END, "That word doesn't exist in our dictionary. Sorry!")
            text.config(state = "disabled")

        #Matches have been found
        else:
            for match in matches:
                selection = messagebox.askquestion("Matches found", f"Did you mean {match}?")

                if (selection == "yes"):
                    allDefinition = data[match]
                    enum = enumerate(allDefinition,1)

                    temp1 = match.title()
                    header.config(text = temp1)
                    for definition in enum:
                        temp2 = f"{definition[0]} - {definition[1]}\n\n"
                        text.insert(tkinter.END, temp2)
                    break
                elif (selection == "no"):
                    #Case where the last possible match has been reached and rejected
                    if (matches.index(match) == (len(matches) - 1)):
                        text.insert(tkinter.END, "That word doesn't exist in our dictionary. Sorry!")
                        text.config(state = "disabled")
                    else:
                        continue
            text.config(state = "disabled")

#Initializing the GUI
window = tkinter.Tk()
window.title("Diqtionary")
window.minsize(300,300)
window.config(bg = "#446ec2")
window.iconbitmap("dictionary.ico")
window.resizable(False, False)
messagebox.showinfo('Welcome!', "Welcome to Diqtionary! Enter a word to get it's defintion. An example has been loaded for you.")

#Defining fonts
prompt = tkFont.Font(family = "Helvetica", size = 14, weight = "bold", underline = 1)
tFont = tkFont.Font(family = "Helvetica")
tHead = tkFont.Font(family = "Helvetica", size = 12, slant = tkFont.ITALIC)

#Prompting user for word
tkinter.Label(window, text = "Enter a word please:", font = prompt).pack(pady = 5)
e1 = tkinter.Entry(window)
e1.pack(pady = 5)
e1.insert(tkinter.END, "Hello")

#Handling word
button1 = tkinter.Button(window, text = "Get definition", command = definition)
button1.pack(pady = 2)

#Displaying word
header = tkinter.Label(window, text="Hello", font = tHead, bg = "#13eb70")
header.pack(anchor = tkinter.W, padx = 2)
text = scrolledtext.ScrolledText(window, undo = True, width = 50, height = 15, wrap = "word", font = tFont)
text.pack(pady = 5)
default = "1 - Expression of greeting used by two or more people who meet each other."
text.insert(tkinter.END, default)

window.mainloop()
