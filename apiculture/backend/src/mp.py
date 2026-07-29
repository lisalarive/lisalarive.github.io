from questions_joueur import recuperation_des_six_themes, questions_joueur
from verifier_la_reponse_du_joueur import verifier_reponse

def main():
    """Fonction principale qui permet de poser les questions à l'utilisateur afin qu'il puisse y répondre, en lui indiquant s'il a ou non la bonne réponse.
    """


    theme = "Musique"
    dix_questions = questions_joueur("database/api_culture.db", theme)
    count = 0

    print("Thème : "+ theme)
    
    for question in dix_questions:

        print("Difficulté : "+ question['difficulte'])
        print(question["question"])
        reponse_user = input("Saisissez votre réponse : \n")
        vrai_reponse =question['reponse']
        reponse_comparee_boolean = verifier_reponse(reponse_user , vrai_reponse) #compare la réponse du joueur et la vraie réponse puis renvoie un bolean 
        
        #affiche résultat joueur
        if reponse_comparee_boolean : 
            print("Vous avez la bonne réponse ! ")
            count+=1
            print("(" + vrai_reponse+ ")\n")
        else: 
            print("Mauvaise réponse. ") 
            print(f"La bonne réponse était : {vrai_reponse}\n" )  

    print("Votre score lors de cette session : " + str(count)) 
    
     

main()