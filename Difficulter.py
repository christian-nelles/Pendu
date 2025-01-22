import time 
import os 

def choisir_difficulte():
    while True:
        print("=== Choisir le niveau de Difficulté ==")
        print("1. Facile")
        print("2. Moyen")
        print("3. Difficile")
        print("4. Quitter")
        choix = input("Entrez votre choix (1 2 3 ou 4) : ")
        
        os.system('cls' if os.name == 'nt' else 'clear') 

        if choix == "1":
            print("Niveau simple mais pas tout est simple")
            niveau = "Facile"
            break 
        elif choix == "2":
            print("Niveau Moderer donc tenez vous pret")
            niveau = "Moyen"
            break
        elif choix == "3":
            print("Preparation maximum car la difficulté est aussi au maximum")
            niveau = "Difficile"
            break
        elif choix == "4":
            print("Au revoir")
            exit()
    return niveau

niveau_choisi = choisir_difficulte()
print(f"Vous avez choisi le niveau : {niveau_choisi}")
