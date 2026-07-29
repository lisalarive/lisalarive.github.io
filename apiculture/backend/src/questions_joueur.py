#Fichier contenant les fonction qui permette de récupérer les questions de la base de données
#
#   questions_joueur(db_chemin : str, theme : str)->list
#   recuperation_des_six_themes(db_chemin: str)->list


import sqlite3
import random 

def questions_joueur(db_chemin : str, theme : str)->list:
    """Fonction qui récupère 10 questions aléatoires sur un thème donné pour le joueur.

    La requête utilise une logique de double tirage au sort pour une plus grande diversité dans les questions:
    - 1er RANDOM (partitionnement) : On regroupe les questions par page Wikipédia et on en choisit une seule au hasard par page. Cela évite d'interroger le joueur plusieurs fois sur le même sujet.
    - 2ème RANDOM (à la fin) : On mélange toutes les questions uniques obtenues, puis on en garde seulement 10. [Sans cette étape, la base de données renvoyait toujours les 10 mêmes premières pages trouvées (car rangé par ordre alphabétique)]

    Args:
        db_chemin (str): Chemin de la base de données.
        theme (str): thème choisi.

    Returns:
        list: Liste contenant 10 dictionnaires, chacun regroupant question, réponse, difficulté et le titre de la page associée.
    """

    connexion = sqlite3.connect(db_chemin)
    curseur = connexion.cursor()

    #PARTITION BY pw.idpw : Création de sous-groupes par article
    #ORDER BY RANDOM() : Mélange des questions à l'intérieur de chaque sous-groupe
    #WHERE random_sort = 1 : Conservation uniquement de la première question de chaque sous-groupe
    #ORDER BY RANDOM() : Empêche la sélection systématique des mêmes premiers articles de la base
    
    curseur.execute("""
        SELECT question, reponse, difficulte, titre_page
        FROM (
            SELECT rg.question, rg.reponse, rg.difficulte, pw.titre_page,
                   ROW_NUMBER() OVER(PARTITION BY pw.idpw ORDER BY RANDOM()) as random_sort
            FROM reponse_gem rg
            JOIN page_wiki pw ON rg.idpw = pw.idpw
            WHERE pw.est_traitee = 1
            AND EXISTS (
                SELECT t.idt FROM theme t WHERE t.idt = pw.idt AND lower(t.nom) = ?
            )
        )
        WHERE random_sort = 1 
        ORDER BY RANDOM()
        LIMIT 10
      
    """, (theme.lower(),))

    lignes = curseur.fetchall()
    
    dix_questions = []
    for ligne in lignes:
        dix_questions.append({
            "question": ligne[0],
            "reponse": ligne[1],
            "difficulte": ligne[2],
            "titre": ligne[3]
        })

        
    connexion.close()
    return dix_questions


def recuperation_des_six_themes(db_chemin: str)->list:
    
    """Fonction qui permet de récupérer la liste des six thèmes 

    Args:
        db_chemin (str): Chemin de la base de donnée

    Returns:
        list: Retourne la liste des six thèmes

    """
    
    connexion = sqlite3.connect(db_chemin)
    curseur = connexion.cursor()

    curseur.execute("""
        select nom
        from theme
    """)

    lignes =curseur.fetchall()

    tab_nom_theme = []

    for ligne in lignes:
        nom_du_theme = ligne[0]
        tab_nom_theme.append(nom_du_theme)
        
    connexion.close()
    return tab_nom_theme

