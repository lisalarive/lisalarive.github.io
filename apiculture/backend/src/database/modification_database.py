# Fichier contenant des fonctions de modifications de la base de données, (ajout, suppression, changement etc)
#
# Fonction présentes :
#   ajouter_reponse_gemini(db_chemin: str, liste_questions: list, titre_page: str) -> None
#   update_est_traitee_page_wiki(db_chemin: str, titre_page: str)-> None
#   refaire_question_sur_titre(db_chemin: str, idpw: int)

import sqlite3

def ajouter_reponse_gemini(db_chemin: str, liste_questions: list, titre_page: str) -> None: 
    """Fonction qui permet d'ajouter les questions, réponses et difficultés générées par Gemini à la base de données. 

    Args:
        db_chemin (str): Chemin de la base de données.
        liste_questions (list): Liste des objets QuizQuestion générés par Gemini ( question, réponse et difficulté).
        titre_page (str): Titre de la page wiki.
    """

    connexion = sqlite3.connect(db_chemin)
    curseur = connexion.cursor()

    # recherche l'idpw correspondant au titre
    curseur.execute("""
    Select pw.idpw
    from page_wiki pw
    where pw.titre_page = ?
    """, (titre_page,))

    idpw = curseur.fetchone()[0] #récupèration du nombre 


    for q_obj in liste_questions:
        question = q_obj.question
        reponse = q_obj.reponse
        difficulte = q_obj.difficulte
        
        curseur.execute("""
            INSERT OR IGNORE INTO reponse_gem (question, reponse, difficulte, idpw)
            VALUES (?, ?, ?, ?)
        """, (question, reponse, difficulte, idpw))
    
    connexion.commit()
    connexion.close()


def update_est_traitee_page_wiki(db_chemin: str, titre_page: str)-> None:
    """Fonction qui permet de mettre à jour la base de données en indiquant que cette page Wikipédia vient d'être traitée ( en changeant le booléen est_traitee de 0 à 1). 

    Args:
        db_chemin (str): Chemin vers la base de données.
        titre_page (str): Titre d'une page Wikipédia.
    """

    connexion = sqlite3.connect(db_chemin)
    curseur = connexion.cursor()

    curseur.execute("""
    update page_wiki
    set est_traitee = 1
    where titre_page = ?
    """, (titre_page,))

    connexion.commit()
    connexion.close()

def refaire_question_sur_titre(db_chemin: str, idpw: int):
    """Fonction qui permet de supprimer toutes les questions créees sur le titre d'une page wiki (son identifiant : idpw)

    Args:
        db_chemin (str): Chemmin vers la base de donnée
        idpw (int): identifiant du titre d'une page wikipédia 
    """

    
    connexion = sqlite3.connect(db_chemin)
    curseur = connexion.cursor()

    curseur.execute("""
    update page_wiki
    set est_traitee = 0
    where idpw = ?
    """, (idpw,))


    curseur.execute("""
    delete from reponse_gem
    where idpw = ?
    """, (idpw,))


    connexion.commit()
    connexion.close()


#chemin_db = "SQL/api_culture.db"
#refaire_question_sur_titre(chemin_db,         )