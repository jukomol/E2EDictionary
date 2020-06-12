<<<<<<< HEAD
from tkinter import *
import json
from difflib import get_close_matches


window = Tk()

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        yn=yn.upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check it."


def outputresult():
    output= translate(e1_value.get())
    if type(output)== list:
        for item in output:
            t1.insert(END,item)
        else:
            t1.insert(END, output)

e1_value = StringVar()
e1=Entry(window, textvariable= e1_value)
e1.grid(row=0, column=0)

b1=Button(window, text="Find", command= outputresult)
b1.grid(row=0, column=1)

t1= Text(window, height=3, width= 60)
t1.grid(row=1, column=0)




window.mainloop()
=======
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        yn=yn.upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
>>>>>>> d55ec21e165ac8df6154cd0f150a75ebeabc0fdd
