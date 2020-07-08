#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#Python
#title 		:Dictionary.py
#description 	:This is a dictionary app
#author 	:JohnBedeir
#website	:johnydesigns.com
#date		:08July20
"""


import json

from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        ans = input("Did you mean %s instead? Enter Y, or N: " % get_close_matches(w, data.keys())[0]) 
        if ans == "y":
            return data[get_close_matches(w, data.keys()) [0]]
        elif ans == "n":
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand the entry"
    else:
        return "The word doesn't exist. Please double check it"

word = input("Type the word: ")

output = translate(word)

if type(output) == list:
    for i in output:
        print ("\n", i)
else:
    print(output)

