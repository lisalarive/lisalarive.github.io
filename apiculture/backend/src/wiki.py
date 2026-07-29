#Fichier contenat les fonction nécessaire pour le choix de la page wiki, aini que la récupération du texte d'une page wiki
#
# Fonction présentes :
#   wiki(link : str)->str
#   choix_page_wiki(db_chemin: str, nom_theme: str) -> str


import requests
import json 
import sqlite3
import random 

def wiki(link : str)->str:
    """Fonction qui, à partir du titre d'une page Wikipédia, renvoie le texte brut de cette page. Le texte est un peu nettoyé en enlevant notamment les liens externes.

    Args:
        link (str): Titre d'une page Wikipédia.

    Returns:
        str: Contenu brut de la page Wikipédia.
    """

	#adresse API
    nom_page = "https://en.wikipedia.org/w/api.php"

    parametres = {
        "action": "query",
        "format": "json",
		"formatversion": "2",
        "titles": link,
        "prop": "extracts",
        "explaintext": "1" #texte brut sans balise html
    }

    headers = {'User-Agent': 'MediaWiki REST API docs examples/0.1 (https://meta.wikimedia.org/wiki/User:APaskulin_(WMF))'}

    response = requests.get(nom_page, headers=headers, params=parametres)
    response = json.loads(response.text)

	#navigation dans les dossiers du dictionnaire pour cibler les pages
    pages = response["query"]["pages"]
	#on prend le premier dossier trouvé
    page_info = pages[0]
	#récupération de la section extract
    lines = page_info["extract"].splitlines()

    #suppression de la partie après External link
    last_line = len(lines)
    for i,line in enumerate(lines):
        if "External links" in line:
            last_line=i
            break
    response = "\n".join(lines[:last_line])

    return response


def choix_page_wiki(db_chemin: str, nom_theme: str) -> str:
    """ Fonction qui renvoie le titre d'une page wiki non traitée 

    Args:
        db_chemin (str): Chemin vers la base de données
        nom_theme (str): Nom du thème choisi

    Returns:
        str: Renvoie le titre d'une page wiki non traitée 
    """

    connexion = sqlite3.connect(db_chemin)
    curseur = connexion.cursor()

    # sélection uniquement des pages non traitées 
    curseur.execute("""
        SELECT pw.titre_page 
        FROM page_wiki pw
        WHERE est_traitee = 0
        AND EXISTS (
            SELECT idt
            FROM theme t
            WHERE t.idt = pw.idt AND lower(t.nom) = ?
        )
    """, (nom_theme.lower(),))


    tab = []
    for ligne in curseur:
        tab.append(ligne[0]) # ligne[0] : texte du titre
        
    connexion.close()

    if not tab:
        return None

    wiki = random.choice(tab)
    return str(wiki).strip()

    