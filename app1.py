import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    x = get_close_matches(word , data.keys())[0]
    word = word.lower()
    if word in data:
        return data[word]
    elif len(x) > 0:
        yn = input(f"did you mean {x}, Y for yes and N for no: ")
        if yn == "Y":
            return data[x]
        elif yn == "N":
            return "sorry! we couldn't find a word"
        else :
            return "we didn't get you"
        

    else :
        print("please double check it")

        
word = input("enter a word: ")

print(translate(word))