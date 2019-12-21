import json
from difflib import get_close_matches

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

word = input("Welcome to Diqtionary!\nEnter 'Exit' if you want to close the program.\nEnter a word please: ") 
while (word != "Exit"):
    if (word == "Exit"):
        break
    else:
        definition(word)
        word = input("\nEnter 'Exit' if you want to close the program.\nEnter a word please: ")

print("\nThanks for using Diqtionary!")