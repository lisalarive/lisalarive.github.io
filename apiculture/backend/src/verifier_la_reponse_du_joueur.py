# Fichier contenant les fonctions qui permettent de vérifier la réponse du joueur avec la réponse attendu
#
# Fonction présentes :
#   insensible(chain : str)->str
#   verifier_reponse(reponse_joueur: str, reponse_attendue: str) -> bool
#   levenshtein_distance(a: str, b: str )-> int

import unicodedata

articles_francais = [
    "le", "la", "l'", "les",# Articles Définis
    "un", "une", "des",# Articles Indéfinis
    "au", "aux", "du", "des",# Articles Contractés 
    "de la", "de l'", # Articles Partitifs 
    "de", "d'", "ès" # Articles "réduits" 
] 

def insensible(chain : str)->str:
    """Fonction permettant de rendre une chaîne de caractères insensible à la casse. On : 
        - met la chaîne en minuscules,
        - enlève les éventuels points et espaces à la fin et au début,
        - retire les accents,
        - retire les articles devant.

    Args:
        chain (str): Chaîne de caractères qui peut être la bonne réponse d'une question ou bien la réponse de l'utilisateur.

    Returns:
        str: La chaîne de caractères rendue insensible à la casse selon nos critères.
    """
    ins : str = chain.lower() #transforme tout en minuscules
    ins = ins.strip(" .") #retire les eventuelles points et espaces à la fin et au début
    ins = ins.replace("'", "' ") #remplace les apostrophes pour que le split fonctionne bien après
    ins = unicodedata.normalize('NFKD',ins)#reformate les caractères
    ins = ''.join([c for c in ins if not unicodedata.combining(c)]) #retire les accents
    
    L : List[str] = ins.split() #sépare la chaine de caractère sans aucune virgule

    L_propre = [] # liste vide
    for mot in L: # Pour chaque mot dans la liste d'origine
        if mot not in articles_francais: # Si ce n'est PAS un article
            L_propre.append(mot) # On l'ajoute à la nouvelle liste
    
    ins = "".join(L_propre) #réassemble la chaine de caractère
    return ins


def levenshtein_distance(a: str, b: str )-> int :
    """Fonction qui calcule la distance de Levenshtein entre deux chaînes de caractères

    Args:
        a (str): Chaîne de caractères qui est la réponse du joueur
        b (str): Chaîne de caractères qui est la réponse attendue

    Returns:
        int: Renvoie la valeur de la distance de Levenshtein entre la reponse du joueur et la reponse attendue
    """

    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[n][m]


def verifier_reponse(reponse_joueur: str, reponse_attendue: str) -> bool:
    """Vérifie si la réponse est bonne en prenant en compte :
        -Le nettoyage (espaces, accents, majuscules)
        -La tolérance aux fautes de frappe selon la longueur du mot attendu.

    Args:
        reponse_joueur (str): Réponse du joueur
        reponse_attendue (str): Réponse qui était attendue

    Returns:
        bool: Renvoie Vrai si la réponse joueur est acceptée selon nos critères, Faux sinon
    """ 
    
    # nettoyage des deux chaînes 
    clean_joueur = insensible(reponse_joueur)
    clean_attendue = insensible(reponse_attendue)
    
    # Si c'est parfait, on retourne True tout de suite
    if clean_joueur == clean_attendue:
        return True
        
    # Sinon, on regarde si c'est une "petite" erreur de frappe
    distance = levenshtein_distance(clean_joueur, clean_attendue)
    
    longueur = len(clean_attendue)
        
    if longueur < 5:
        tolerance = 0  # "Oie" vs "Pie" -> Faux (trop court pour tolérer une erreur)
    elif 5 <= longueur <= 10:
        tolerance = 1  # "Maison" vs "Mison" -> Vrai
    else: # Pour 11 lettres et plus
        tolerance = 2  # "Constitution" vs "Constitussion" -> Vrai
        
    # 4. Verdict
    if distance <= tolerance:
        return True
        
    return False