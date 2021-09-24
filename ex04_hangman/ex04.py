import os
import re
from random import *
import random


random_words = ["efrei", "auxerre", "windows", "manette", "bleach", "fifa"]
word = random.choice(random_words)
word_lenght = len(word)
i = randint(0, word_lenght-1)
life = 4


to_guess = [" _ "]*word_lenght
to_guess[i] = word[i]
print(to_guess)


while life != 0 :
    user_choice = input("deviner une des lettres ")
    if len(user_choice) != 1 :
        print("entrez une lettre")


    elif user_choice in word :
        print("correct ! "+user_choice+" est dans le mot !")
        matches = re.finditer(user_choice, word)
        index_letter = [match.start() for match in matches]
        for j in index_letter :
            to_guess[j] = word[j]
        if " _ " not in to_guess :
            break


    elif user_choice not in word :
        life -= 1
        print("la lettre n'est pas dans le mot !")
    print(to_guess)
    print("nombre de vie: ",life,"\n")


result = "tu as perdu !"
if " _ " not in to_guess and life > 0 :
    result = "tu as gagné, bien joué !"



print(result)
choice = input("veux tu rejouer ? (Y/N)")
if choice == "Y" or choice == "y" :
    print("")
    os.system("py ./ex04.py") 
exit()