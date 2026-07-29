function ajout_num_question(){
    num_question= localStorage.getItem('num_question')
    console.log("num de la question : " + localStorage.getItem('num_question'));
    num_question++;
    localStorage.setItem('num_question',num_question);
    console.log("num de la question après ajout +1 : " + localStorage.getItem('num_question'));

    if (num_question > 10){
	window.location.href = "../html/Questions_Fin_Session.html";
	}else{
        window.location.href = "../html/Questions.html";
    }

}
