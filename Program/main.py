import json
data = json.load(open("Program/defs.json"))

def defReturn(word):
    word = word.lower()
    
    if word in data:
        allDefinition = data[word]
        enum = enumerate(allDefinition,1)

        print(word.title())
        for definition in enum:
            print(f"{definition[0]} - {definition[1]}")
    else:
        print("That word doesn't exist in our dictionary. Sorry!")

word = input("Welcome to Diqtionary!\nEnter a word please: ") 
defReturn(word)