import json

data = json.load(open("data.json"))


def definition():
    word = input("Enter a word: ").lower()
    if word in data:
        return data[word]
    else:
        return "No such word"


print(definition())
