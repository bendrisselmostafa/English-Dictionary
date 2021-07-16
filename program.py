import json
import difflib

data = json.load(open("data.json"))


def definition():
    word = input("Enter a word: ").lower()
    if word in data:
        return data[word]
    elif len(difflib.get_close_matches(word, data.keys())) > 0:
        close_word = difflib.get_close_matches(word, data.keys())[0]
        choice = input(
            "Did you mean %s instead ? Y = Yes | N = No : " % close_word
        ).lower()

        while not (choice == "y" or choice == "n"):
            print("Invalid input")
            choice = input(
                "Did you mean %s instead ? Y = Yes | N = No : " % close_word
            ).lower()
        if choice == "y":
            return data[close_word]
        return "Please check Again"
    else:
        return "No such word"


print(definition())
