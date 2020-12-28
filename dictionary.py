import json


data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word. data.keys())) > 0:
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes and n for no")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("The word")
        else:
            return("You have entered wrong input, please enter just y or m")

    
    else:
        print("you have entered the wrong keys")



word = input("Enter the word you want to search") 
output = translate(word)


if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)