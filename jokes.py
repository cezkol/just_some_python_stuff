###Script that randomly draw a joke on given subject (from https://icanhazdadjoke.com)###

from pyfiglet import figlet_format
from colorama import init
from termcolor import colored
from random import choice
from requests import get

#page url
url="https://icanhazdadjoke.com/search"

#function just for printing colored ascii art
def print_ascii(txt, clr):
    #valid colors
	valid_clrs=["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
	if clr not in valid_clrs:
		clr="green"
        
	print(colored(figlet_format(txt),clr))

#function for subject definition
def ask_subject():
	topic=input("Let me tell you a joke. REEEEALY good joke. Just give a subject:\n")
	return topic

#main function
def tell_joke(temat):
    
    #requesting jokes on particular subject
	res=get(
		url, 
		headers={"Accept":"application/json"},
		params={
			"term":temat
		}
	)
    
    #how much jokes found
	counter=res.json()["total_jokes"]

	if counter==0:
		print(f"\nSorry, I don't know any jokes about '{temat}' ;(")
	else:
		joke=choice(res.json()["results"])["joke"] #joke choice
		print(f"\nI know {counter} GREAT jokes about '{temat}'.\nHere is one of them:")
		print("\n#################################")
		print(joke)
		print("#################################\n")

#MAIN
init()
print_ascii("REALLY GREAT JOKES", "red")
tell_joke(ask_subject())

