import json

data = json.load(open("data.json"))


def definition():
    word = input("Enter a word: ")
    return data[word]


print(definition())
