import random

nb= random.randint(1, 100)
rep= 0

print("trouver le nombre mytère, indice: il s'agit d'un nombre compris entre 1 et 100")
while (int(rep)!=nb):
    rep=input()
    if int(rep)<nb:
        print("le nombre mytère est plus grand !")
    elif int(rep)>nb:
        print("le nombre mytère est plus petit !")
print("tu as trouvé le nombre mystère bien joué ! il s'agissait bien du nombre "+ str(nb))