// Nombre de session terminée
let sessionsTerminees = localStorage.getItem('nbr_session_finish');
if (sessionsTerminees === null) {
	localStorage.setItem('nbr_session_finish', 0)
}
console.log("nombre de sessions terminées : " + localStorage.getItem('nbr_session_finish'));

function ajout_plus_un_nbr_sessions_complete(){
    sessionsTerminees = localStorage.getItem('nbr_session_finish');
    sessionsTerminees++
    localStorage.setItem('nbr_session_finish', sessionsTerminees);
    console.log("nombre de sessions terminées après ajour +1 : " + localStorage.getItem('nbr_session_finish'));
}

let Session_complete = document.querySelector('p.nbr_session_finish');
if (Session_complete) {
    Session_complete.textContent = localStorage.getItem('nbr_session_finish');
}



//Nombre de questions répondues
let QuestionRepondues = localStorage.getItem('nbr_question_repondues')
if (QuestionRepondues === null){
    localStorage.setItem('nbr_question_repondues', 0)
}
console.log("nombre de questions répondues : " + localStorage.getItem('nbr_question_repondues'));

function ajout_plus_un_nbr_question_repondues(){
    QuestionRepondues= localStorage.getItem('nbr_question_repondues')
    QuestionRepondues++;
    localStorage.setItem('nbr_question_repondues',QuestionRepondues);
    console.log("nombre de questions répondues après ajout +1: " + localStorage.getItem('nbr_question_repondues'));
}

let Nbr_question = document.querySelector('p.nbr_question_repondues');
if (Nbr_question) {
    Nbr_question.textContent = localStorage.getItem('nbr_question_repondues');
}



//Meilleur score lors d'une session
let MeilleurScore = localStorage.getItem('meilleur_score')
if (MeilleurScore === null){
    localStorage.setItem('meilleur_score', 0)
}
console.log("Le meilleur score lors d'une session est de : " + localStorage.getItem('meilleur_score'));


function calcul_meilleur_score(){
    MeilleurScore = parseInt(localStorage.getItem('meilleur_score'));
    score_actuel = parseInt(localStorage.getItem('score_session'));

    console.log("Le score actuel est de : " + localStorage.getItem('score_session'));
    if(score_actuel > MeilleurScore){
        localStorage.setItem('meilleur_score', score_actuel);
    }
    console.log("Le meilleur score lors d'une session est de, après comparaison avec score actuel : " + localStorage.getItem('meilleur_score'));
}

let MeilleurScoreAffichage = document.querySelector('p.meilleur_score');
if(MeilleurScoreAffichage){
    MeilleurScoreAffichage.textContent = localStorage.getItem('meilleur_score') + '/10'
}



//Score minimum lors d'une session
let ScoreMinimum = localStorage.getItem('score_minimum')
if (ScoreMinimum === null){
    localStorage.setItem('score_minimum', "0")
}
console.log("Le score minimum lors d'une session est de : " + localStorage.getItem('score_minimum'));

function calcul_score_minimum(){
    ScoreMinimum = parseInt(localStorage.getItem('score_minimum'));
    score_actuel = parseInt(localStorage.getItem('score_session'));

    console.log("Le score actuel est de : " + localStorage.getItem('score_session'));
    if(ScoreMinimum ="ND"){
        localStorage.setItem('score_minimum', score_actuel);
    }
    
    if(score_actuel < ScoreMinimum){
        localStorage.setItem('score_minimum', score_actuel);
    }
    console.log("Le score minimum lors d'une session est de , après comparaison avec score actuel : " + localStorage.getItem('score_minimum'));
}

let ScoreMinimumAffichage = document.querySelector('p.score_minimum');
if(ScoreMinimumAffichage){
    ScoreMinimumAffichage.textContent = localStorage.getItem('score_minimum') + '/10';
}



//Nombre de réponse correcte
let NbrBonneReponses = localStorage.getItem('nbr_reponses_correctes')
if (NbrBonneReponses === null){
    localStorage.setItem('nbr_reponses_correctes', 0)
}
console.log("Le nombre total de bonne réponse est de : " + localStorage.getItem('nbr_reponses_correctes'));

function ajout_plus_un_nbr_bonne_reponses(){
    NbrBonneReponses= localStorage.getItem('nbr_reponses_correctes')
    NbrBonneReponses++;
    localStorage.setItem('nbr_reponses_correctes',NbrBonneReponses);
    console.log("Le nombre total de bonne réponse après ajout +1 : " + localStorage.getItem('nbr_reponses_correctes'));
}

let NombreBonneReponseAffichage = document.querySelector('p.nbr_reponses_correctes');
if(NombreBonneReponseAffichage){
    NombreBonneReponseAffichage.textContent = localStorage.getItem('nbr_reponses_correctes')
}



//Score moyen par session
let ScoreBonneReponseSurSessionFinies = localStorage.getItem('score_moyen')
if(ScoreBonneReponseSurSessionFinies === null){
    localStorage.setItem('score_moyen', 0)
}
console.log("Le score moyen par session est de : "+ localStorage.getItem('score_moyen'))

function ajout_bonne_reponse_au_score_moyen(){
    score_session = parseInt(localStorage.getItem('score_session'))
    ScoreBonneReponseSurSessionFinies = parseInt(localStorage.getItem('score_moyen'))
    ScoreBonneReponseSurSessionFinies = ScoreBonneReponseSurSessionFinies + score_session
    localStorage.setItem('score_moyen', ScoreBonneReponseSurSessionFinies)
}

let ScoreMoyenAffichage = document.querySelector('p.score_moyen')
if(ScoreMoyenAffichage){
    ScoreBonneReponseSurSessionFinies = parseInt(localStorage.getItem('score_moyen'))
    let moyenne =0;
    if (ScoreBonneReponseSurSessionFinies > 0) {
            total_sessions = parseInt(localStorage.getItem('nbr_session_finish'));

            moyenne = ScoreBonneReponseSurSessionFinies / total_sessions;
    }
    moyenne = Math.round(moyenne * 10) / 10;
    ScoreMoyenAffichage.textContent = moyenne + '/10'

}
