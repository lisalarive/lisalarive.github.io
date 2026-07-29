#importation des fonctions 
from wiki import wiki, choix_page_wiki
from gem.gem import ask, QuizQuestion, QuizOutput
from autre_fonctions_utiles import generateur_aleatoire_difficulte, nombre_question_en_fonction_taille
from database.modification_database import update_est_traitee_page_wiki, ajouter_reponse_gemini
from questions_joueur import recuperation_des_six_themes

chemin_db = "database/api_culture.db"
gemini_prompt="gem/gemini_prompt.txt"


def generateur_question():
    """Fonction qui permet de générer les questions afin de remplir la base de données. Elle fait principalement des appels aux autres fonctions.
    """

    #chargement prompt pour gemini
    with open(gemini_prompt, mode="r", encoding="utf-8") as fichier_prompt:
        modele_prompt = fichier_prompt.read()

    liste_themes = ["Cinema"] 
    #recuperation_des_six_themes(chemin_db)

    for theme in liste_themes:
    
        for i in range (10): #83 *6 = 498 , en 3 jours on peut avoir notre base de donnée
            #choix aléatoire de titre de page wiki
            titre = choix_page_wiki(chemin_db, theme)
            #API wikipédia
            contenu_wikipedia_brut = wiki(titre)
            

            nombre_question = nombre_question_en_fonction_taille(contenu_wikipedia_brut)
            listes_difficultes = generateur_aleatoire_difficulte(nombre_question)
        
            #injection des variables dans le prompt
            prompt_a_envoyer = modele_prompt.format(
                titre=titre,
                theme=theme,
                nombre=nombre_question,
                listes_difficultes=", ".join(listes_difficultes),
                contenu=contenu_wikipedia_brut
            )
                    
            #API Gemini
            tab_gemini= ask(prompt_a_envoyer)

            ajouter_reponse_gemini(chemin_db, tab_gemini.questions, titre)
            update_est_traitee_page_wiki(chemin_db, titre)


generateur_question()