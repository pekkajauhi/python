# Dynamic dictionary
# This programs returns defition(s) of words that user enters
# If the word is not included in the dictionary, it checks if the word 
# was miss spelled and suggests the correctly spelled word.


import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def translate(word):
	word = word.lower()
	
	if word in data:
	    return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word,data.keys(), n=1, cutoff=0.8)) > 0:
		yn = input("Did you mean '%s' instead? Enter Y if yes and N if no: " % get_close_matches(word,data.keys(), n=1, cutoff=0.8)[0]) 
		if yn == 'Y':
			return data[get_close_matches(word,data.keys(), n=1, cutoff=0.8)[0]]
		elif yn == 'N':
			return "The word doesn't exist."
		
		else:
			return "\nI don't understand what you meant" 
	else:
		return "The word doesn't exist."
		

		
		
word = input("Enter word: ")

output = translate(word)

if type(output) == list:	
    for item in output:
	    print("\n"+item)
	    
	    
else:
	print(output)
