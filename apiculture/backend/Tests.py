import sys
sys.path.append("src")

import random
from insensible import insensible
from fonction_levenshtein_distance import levenshtein_distance
from verifier_reponse import verifier_reponse
from choix_page_wiki import choix_page_wiki
from wiki import wiki 
from nombre_question_en_fontion_taille import nombre_question_en_fonction_taille
from generateur_aleatoire_difficulte import generateur_aleatoire_difficulte

#test fonction insensible
assert insensible("Chat.") == "chat"
assert insensible("Napoléon Bonaparte") == "napoleonbonaparte"
assert insensible("éèếëëÈË") == "eeeeeee"
assert insensible("le chât") == "chat" 
assert insensible("l'oisEaû") == "oiseau" # Apostrophe collée
assert insensible("l' oisEaû") == "oiseau" # Apostrophe

#test fonction levenshtein_distance
assert levenshtein_distance("chat", "chien") == 3
assert levenshtein_distance("chat", "chat") == 0
assert levenshtein_distance("chat", "that") == 1
assert levenshtein_distance("chat", "hat") == 1

#test fonction verifier_reponse
assert verifier_reponse("parie", "Paris") == True #5 lettres -> Tolérance 1 -> Distance 1 (parie/paris)
assert verifier_reponse("par", "Paris") == False # 5 lettres -> Tolérance 1 -> Distance 2 (par/paris) 
assert verifier_reponse("chat", "Char") == True # 4 lettres -> Tolérance 1 -> Distance 1 (chat/char)
assert verifier_reponse("cat", "Car") == False #3 lettres -> Tolérance 0 -> Distance 1 (cat/car)

#test fonction choix_page_wiki
#random.seed(3)
#assert choix_page_wiki("SQL/api_culture.db", "Informatique") == "Ada_Lovelace"

#test fonction nombre_question_en_fonction_taille et utilisation de fonction wiki
#?test avec page de Alan Turing (page longue)
texte = wiki("Alan_Turing")
nombre = nombre_question_en_fonction_taille(texte)
assert nombre == 32 

#?test avec page de Jhungara (page très petite)
texte = wiki("Jhungara")
nombre = nombre_question_en_fonction_taille(texte)
assert nombre == 1

#test fonction generateur_aleatoire_difficulte
random.seed(8)
assert generateur_aleatoire_difficulte(5) == ['facile', 'difficile', 'facile', 'moyen', 'facile']


