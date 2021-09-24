import random

print("bienvenue dans le jeu du pierre feuille ciseaux !")
rep=0
nb=0

while (rep==nb):
    print("saisissez votre main (1= pierre 2= feuille 3= ciseaux")
    rep=int(input())
    nb= random.randint(1, 3)
    lt=["la pierre", "la feuille", "le ciseaux"]

    if(rep==nb):
        print("égalité, vous avez tous les deux choisis "+ lt[nb-1])
    elif((rep==1 and nb==3) or (rep==2 and nb==1) or (rep==3 and nb==2)):
        print("gagné, votre adversaire avait choisis "+ lt[nb-1] +" et vous " + lt[rep-1])
    else:
        print("perdu, votre adversaire avait choisis "+ lt[nb-1] +" et vous " + lt[rep-1])