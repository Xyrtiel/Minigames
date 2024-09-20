import random
import os
from turtle import *

def mode_triche(lettres_trouvees, affichage_mot, mots_possibles):
    # Fréquence des lettres dans la langue française
    freq_lettres = {
        'a': 7.636, 'b': 0.901, 'c': 3.260, 'd': 3.669, 'e': 14.715, 'f': 1.066, 
        'g': 0.866, 'h': 0.937, 'i': 7.529, 'j': 0.813, 'k': 0.074, 'l': 5.456, 
        'm': 2.968, 'n': 7.095, 'o': 5.796, 'p': 2.521, 'q': 1.362, 'r': 6.693, 
        's': 7.948, 't': 7.244, 'u': 6.311, 'v': 1.838, 'w': 0.049, 'x': 0.427, 
        'y': 0.708, 'z': 0.326
    }

    # Filtrer pour retirer les lettres déjà proposées
    suggestions = {lettre: freq for lettre, freq in freq_lettres.items() if lettre not in lettres_trouvees}

    # Si le mot commence à prendre forme, essayer de proposer un mot entier
    if "_" not in affichage_mot:
        return ''.join(affichage_mot)

    # Filtrer les mots possibles en fonction des lettres découvertes et de la longueur
    mots_filtrés = [mot for mot in mots_possibles if len(mot) == len(affichage_mot)]
    
    # Réduire les mots possibles en fonction des lettres découvertes dans l'affichage_mot
    for i, lettre in enumerate(affichage_mot):
        if lettre != "_":
            mots_filtrés = [mot for mot in mots_filtrés if mot[i] == lettre]

    if len(mots_filtrés) == 1:
        # Si un seul mot correspond, le proposer directement
        return mots_filtrés[0]
    
    # Proposer la lettre la plus fréquente parmi celles restantes
    meilleure_lettre = max(suggestions, key=suggestions.get)
    return meilleure_lettre


def jeu_du_pendu():

    # Liste de mots aléatoires
    mots_aleatoires = []
    
    try:
        with open("mots.txt", "r", encoding="utf8") as fichier:
            for ligne in fichier:
                mots_aleatoires.append(ligne.strip())
    except FileNotFoundError:
        print("Le fichier mots.txt est introuvable. Basons nous alors sur une liste d'environ 50 mots pour régler ce problème.")
        mots_aleatoires = ["chat", "chien", "maison", "voiture", "ordinateur", "pomme", "livre", "fleur", "arbre", "soleil",
                       "lune", "étoile", "ville", "jardin", "rivière", "montagne", "plage", "bâteau", "cheval", "oiseau",
                       "table", "chaise", "fenêtre", "porte", "horloge", "moulin", "route", "ciel", "forêt", "champ", "papa", "amande", "amende",
                       "cuirassé", "coquillage", "antisocial", "antijeu"]

    

    # Choisir un mot aléatoire dans la liste
    mot_a_deviner = random.choice(mots_aleatoires)

    # Initialiser l'affichage du mot avec des underscores (_)
    affichage_mot = ["_"] * len(mot_a_deviner)
    lettres_trouvees = []  # Liste pour stocker les lettres trouvées
    penalites = 0  # Compte des pénalités
    lettres_entrees = ""  # Stocker les lettres déjà proposées

    choix = str(input("Avant de commencer, voulez-vous utiliser le mode Triche de ce fameux jeu de pendu ? (Ecrivez Oui pour confirmer votre choix) : ")).lower()

    print("Mot à deviner : ", " ".join(affichage_mot))

    # Boucle principale du jeu
    while "_" in affichage_mot:
        if choix == "oui":
            # Proposer une lettre ou un mot entier avec le mode triche
            suggestion = mode_triche(lettres_trouvees, affichage_mot, mots_aleatoires)
            if suggestion and len(suggestion) == 1:
                print(f"Mode triche : Vous devriez essayer la lettre : '{suggestion}'")
            elif suggestion:
                print(f"Mode triche : L'IA pense que le mot est : '{suggestion}'")

        # Demander une proposition de lettre ou de mot entier
        proposition = input("Proposez une lettre ou devinez le mot entier : ").lower()

        # Vérification si le joueur propose le mot entier
        if len(proposition) == len(mot_a_deviner) and proposition == mot_a_deviner:
            print("Mon dieu, vous êtes un Dieu ! Vous avez deviné le mot entier !")
            break

        # Si la proposition est une lettre
        if len(proposition) == 1:
            if proposition in lettres_trouvees:
                print("Vous avez déjà proposé cette lettre.")
                continue

            lettres_trouvees.append(proposition)  # Ajoute la lettre à la liste des lettres proposées
            lettres_entrees += proposition + " "

            if proposition in mot_a_deviner:
                # Si la lettre est dans le mot, on l'ajoute à l'affichage
                for i, lettre in enumerate(mot_a_deviner):
                    if lettre == proposition:
                        affichage_mot[i] = proposition
                print("Bonne lettre !")
            else:
                penalites += 1
                print(f"Lettre incorrecte ! Vous avez {penalites} pénalités.")
        else:
            print(f"La proposition '{proposition}' est incorrecte. Vous avez {penalites} pénalités.")
            penalites += 5

        # Afficher l'état du mot et les lettres proposées
        print("Mot à deviner : ", " ".join(affichage_mot))
        print("Les lettres que vous avez proposées : ", lettres_entrees)

        # Condition de victoire
        if "_" not in affichage_mot:
            print(">>> Gagné! <<<")
            break


# Démarrer le jeu
jeu_du_pendu()
