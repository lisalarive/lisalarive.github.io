#Fichier qui contient d'autre sfonction nécessaire au code
#
# Fonction présentes :
#   generateur_aleatoire_difficulte(nombre_question: int)->list
#   nombre_question_en_fonction_taille(texte_brute : str)->int

from random import choices
from math import ceil


def generateur_aleatoire_difficulte(nombre_question: int)->list:
    """Génération aléatoire de niveaux de difficulté en fonction d'un pourcentage:
        - Facile : 50
        - Moyen : 35 %
        - Difficile : 15%

    Args:
        nombre_question (int): nombre entier qui va permettre de définir la taille de la liste des difficultés à générer

    Returns:
        list: liste des difficultés tirées au sort d'une longueur nombre_question
    """


    niveaux = ["facile", "moyen", "difficile"]
    probabilites = [0.50, 0.35, 0.15]
    
    liste_choix = choices(niveaux, weights=probabilites, k=nombre_question)
    
    return liste_choix


def nombre_question_en_fonction_taille(texte_brute : str)->int:
    """fonction qui a partir d'un texte brute calcul sa longueur et renvoi le nombre de mot divisé par 250. Ce qui permet d'avoir environ une question tout les 250 mots

    Args:
        texte_brute (str): texte brute d'une page wikipédia

    Returns:
        int: valeur permettant d'inquiquer le nombre de questions en fonctions de la longueur du texte
    """
     
    tab = texte_brute.split()
    count = 0
    for mot in tab:
        count+=1
    
    resultat = count / 250 #on a environ 1 question tous les 250 mots 
    return ceil(resultat)

