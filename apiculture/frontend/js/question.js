let liste_question = undefined;
let num = localStorage.getItem('num_question');
const choix_theme = localStorage.getItem('choix_theme');
console.log("le joueur a choisi " + localStorage.getItem('choix_theme'));
let liste_q={}

async function charger(){
	if (localStorage.getItem('telechargement_autorise') === 'oui'){
		
		liste_question = await fetch("http://localhost:8080/question/" +choix_theme);
		const data = await liste_question.json();
		liste_q = data.questions
		for(let i=0;i<10;i++){
			localStorage.setItem(i +'q',liste_q[i].question);
			localStorage.setItem(i +'r',liste_q[i].reponse);
			localStorage.setItem(i +'d',liste_q[i].difficulte);
			localStorage.setItem(i +'t',liste_q[i].titre)
			console.log("question " + (i+1) +" :" + localStorage.getItem(i+'q'));
			console.log("reponse " + (i+1) +" :" + localStorage.getItem(i+'r'));
			console.log("difficulte " + (i+1) +" :" + localStorage.getItem(i+'d'));
			console.log("titre " + (i+1) +" :" + localStorage.getItem(i+'t'));
		}
		localStorage.setItem('telechargement_autorise', 'non');
	}

	let titreQuestion = document.querySelector('h2.titre_questions');
	if (titreQuestion) {
		titreQuestion.textContent = 'Question n° '+ localStorage.getItem('num_question');
        console.log("score de la session : " + localStorage.getItem('score_session'));
	}

	let titreDifficulte = document.querySelector('h2.titre_difficulte');
	if (titreDifficulte) {
		titreDifficulte.textContent = 'Difficulté: ' + localStorage.getItem((num-1) + 'd');
	}

	let questionPosee = document.querySelector('p.question_posee');
	if (questionPosee) {
		
		questionPosee.textContent = localStorage.getItem((num-1) + 'q');
	}

	let reponseFausse = document.querySelector('p.mauvaise_reponse');
	if (reponseFausse) {
		BonneReponse = localStorage.getItem((num-1)+'r');
		reponseFausse.textContent = 'Aïe, ça pique ! Réponse : \n' + BonneReponse
	}

	let titrePageWiki =document.querySelector('a.titre_page_wiki')
	if (titrePageWiki){

		let titre = localStorage.getItem((num-1) + 't');
		let urlWiki = 'https://en.wikipedia.org/wiki/' + titre;
		titrePageWiki.textContent = 'En savoir plus sur Wikipédia';
		titrePageWiki.href = urlWiki;
		
		// ouvre la page sur un autre onglet
		titrePageWiki.target = "_blank";
	}

	let lien_image = '../img/Abeilles/' + choix_theme +'.png';

	let AbeilleTheme = document.querySelector('img.img_abeilles_themes');
	if(AbeilleTheme){
		AbeilleTheme.src = lien_image;
	}

	let AbeilleThemeVF = document.querySelector('img.img_abeilles_themes_v_f');
	if(AbeilleThemeVF){
		AbeilleThemeVF.src = lien_image;
	}
}

charger();

let bool_reponse_joueur=undefined

async function recuperer_input_reponse(){
	//réponse joueur
	let input_reponse = document.querySelector('.input_reponse').value;
	console.log("La réponse de l'utilisateur est "+ input_reponse);


	if (input_reponse === '') {
        alert("Merci de saisir une réponse !");
        return;
    }

	//num question actuelle
	let num_actuel = localStorage.getItem('num_question');
	console.log("Le nuémro actuel de la quetsion est : " + num_actuel);

	//réponse attendue 
	let reponse_attendue = localStorage.getItem((num_actuel-1)+'r');
	console.log("La réponse attendue est : ", reponse_attendue);

	//comparer
	let reponse_serveur = await fetch("http://localhost:8080/verifier_reponse_joueur/" + input_reponse + "/" + reponse_attendue);
	bool_reponse_joueur = await reponse_serveur.json();
	console.log("Le résultat de la vérification est :", bool_reponse_joueur);

	//aller sur page question_vrai ou question_faux 
	if(bool_reponse_joueur == 1 ){
		window.location.href = "../html/Questions_Vrai.html";
	}else{
		window.location.href = "../html/Questions_Faux.html";
	}

}












