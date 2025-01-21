import random

# Choisi un mot depuis le fichier "mots.txt"
mots = []
with open("mots.txt") as fl:
    for l in fl:
        mots.append(l.rstrip("\n"))
mot = random.choice(mots)

# Variable cle
lettres = []
faux = 0
trouve = False
corp_plein = ["O", "/", "|", "\\", "/", "\\"]
corp = [" ", " ", " ", " ", " ", " "]

# Affiche le pendu et les mots 
while not trouve: 
    trouve = True
    print(" +---+")
    print(" |   |")
    print(" |   {}".format(corp[0]))
    print(" |  {}{}{}".format(corp[1], corp[2], corp[3]))
    print(" |  {} {}".format(corp[4], corp[5]))
    print("_|_")
    print("| |")
    for l in mot:
        if l in lettres:
            print(l, end=" ")
        else:
            trouve = False
            print("_", end=" ")
    print()
    print("Lettres utilisees - ", end="")
    for l in lettres:
        print(l, end=" | ")
    print()

    if faux > 5:
        print("Tu as perdu!")
        print("Mot - {}".format(mot))
        break
    
    if trouve:
        print("Tu as gagne!")
        break

# Affiche l'option entréz une lettre 
    lettre = input("Entez une lettre: ")
    lettres.append(lettre)

# Gestion des erreurs   
    if lettre not in mot:
        corp[faux] = corp_plein[faux]
        faux += 1
                  


