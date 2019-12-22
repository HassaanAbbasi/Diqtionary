import json
from difflib import get_close_matches
import tkinter
import tkinter.font as tkFont
from tkinter import messagebox

data = json.load(open("Program/defs.json"))

#Prints the defintions of a given word
def definition(word):
    word = word.lower()

    #Case where the word is correctly spelled and in data
    if (word in data):
        allDefinition = data[word]
        enum = enumerate(allDefinition,1)

        print(word.title())
        for definition in enum:
            print(f"{definition[0]} - {definition[1]}")

    #Case where the word is a proper noun (Manchester, Paris, etc.)
    elif (word.title() in data):
        allDefinition = data[word.title()]
        enum = enumerate(allDefinition,1)

        print(word.title())
        for definition in enum:
            print(f"{definition[0]} - {definition[1]}")

    #Case where the user enters acronyms (NASA,UN, etc.)
    elif (word.upper() in data):
        allDefinition = data[word.upper()]
        enum = enumerate(allDefinition,1)

        print(word.title())
        for definition in enum:
            print(f"{definition[0]} - {definition[1]}")

    #Case where the word is spelled incorrectly
    else:
        matches = get_close_matches(word,data)

        #Given word does not exist (has no matches)
        if (len(matches) == 0):
            print("That word doesn't exist in our dictionary. Sorry!")

        else:
            for match in matches:
                selection = input(f"Did you mean {match}? Please input either 'Yes' or 'No': ")
                while (selection != "Yes" and selection != "No"):
                    selection = input("Please input either 'Yes' or 'No': ")

                if (selection == "Yes"):
                    allDefinition = data[match]
                    enum = enumerate(allDefinition,1)

                    print(match.title())
                    for definition in enum:
                        print(f"{definition[0]} - {definition[1]}")
                    break
                elif (selection == "No"):
                    #Case where the last possible match has been reached and rejected
                    if (matches.index(match) == (len(matches) - 1)):
                        print("That word doesn't exist in our dictionary. Sorry!")
                    else:
                        continue

#Initializing the GUI
window = tkinter.Tk()
window.title("Diqtionary")
window.minsize(300,300)
window.iconbitmap("Program/dictionary.ico")
messagebox.showinfo('Welcome!', "Welcome to Diqtionary! Enter a word to get it's defintion.")

#Defining fonts
prompt = tkFont.Font(family="Helvetica", size = 12, weight = "bold", underline = 1)

#Prompting user for word
tkinter.Label(window, text="Enter a word please:", font = prompt).grid(row = 0, column = 0, padx = 6)
e1 = tkinter.Entry(window)
e1.grid(row = 0, column = 1, padx = 10, pady = 10)

#Handling word
button1 = tkinter.Button(window, text = "Get definition", command = definition)
button1.grid(row = 1, column = 0, sticky = tkinter.W, padx = 8)

#Displaying word
#TODO
# -Use a textbox or something?

window.mainloop()

# word = input("Welcome to Diqtionary!\nEnter 'Q' if you want to close the program.\nEnter a word please: ") 
# while (word != "Q"):
#     definition(word)
#     word = input("\nEnter 'Q' if you want to close the program.\nEnter a word please: ")

# print("\nThanks for using Diqtionary!")