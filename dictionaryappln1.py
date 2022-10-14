#29MAR2022

#This is translator using dictionary
from webbrowser import get

dir_eng_french= {"Good Morning":"Bonjour", "Good Evening":"Bonsoir","Good Night":"Bonne nuit","Dinner":"Dîner"}

a = input("ENTER YOUR WORD: ")
print("This is the translated version:", dir_eng_french.get(a.title())) 
#.title converts the input into title i.e all the words start with capital letter