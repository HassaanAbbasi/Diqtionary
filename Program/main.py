import json
data = json.load(open("Program/defs.json"))

def defReturn(word):
    allDefinition = data[word]
    enum = enumerate(allDefinition,1)
    print(word.title())
    for definition in enum:
        print(f"{definition[0]} - {definition[1]}")

defReturn("hot")