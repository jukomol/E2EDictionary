from tkinter import *
import json
from difflib import get_close_matches


window = Tk()
window.resizable(0,0)
window.title("DICTIONARY")
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    else:
        return "The word doesn't exist. Please double check it."


def closematch():
     if len(get_close_matches(w, data.keys())) > 0:
        t2=Text(window, height=1,width=60)
        t2.grid(row=4,column=0)

        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        t2.insert(yn,END)


        yn=yn.upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
     else:
        return "We didn't understand your entry"


def outputresult():
    output= translate(e1_value.get())
    if type(output)== list:
        for item in output:
            t1.insert(END,item)
    else:
        t1.insert(END, output)


def clearText():
    t1.config(state=NORMAL)
    t1.delete(1.0,END)
    e1.delete(0,'end')


e1_value = StringVar()
e1=Entry(window, textvariable= e1_value)
e1.grid(row=1, column=0)

b1=Button(window, text="Find", command= outputresult)
b1.grid(row=2, column=0,pady=2)

t1= Text(window, height=8, width= 60)
t1.grid(row=3, column=0)

b2=Button(window, text="Clear", command= clearText)
b2.grid(row=3,column=1,padx=2)

Label(window,text="DICTIONARY").grid(row=0)


window.mainloop()
