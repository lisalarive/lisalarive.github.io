import requests
import json
import os
from google import genai
from google.genai.types import HttpOptions, HttpRetryOptions
from pydantic import BaseModel, Field

 
ma_cle_secrete = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=ma_cle_secrete, http_options=HttpOptions(
        retry_options=HttpRetryOptions(attempts=1) 
    )
)
#structure d'une question
class QuizQuestion(BaseModel):
    """Création d'une classe de type QuizQuestion, ce qui va permettre de forcer ce type de retour à Gemini.

    """

    question: str
    reponse: str
    difficulte: str

#structure d'une liste de plusieurs questions
class QuizOutput(BaseModel):
    """Création d'une classe qui contient une liste reprenant la structure d'une question, c'est-à-dire un QuizQuestion.

    """
    questions: list[QuizQuestion]

def ask(prompt: str):
    """Fonction qui permet de générer la liste QuizOutput grâce à Gemini, qui contient une liste de QuizQuestion.

    Args:
        prompt (str): Chemin du fichier texte qui contient le prompt expliquant à Gemini son rôle de générateur de questions.

    Returns:
        QuizOutput: Structure de liste de plusieurs questions, dont le format de retour a été forcé pour être un QuizOutput.
    """
    
    response = client.models.generate_content(
    model= "gemini-3.1-flash-lite-preview", 
    contents = prompt,
    config={
            'response_mime_type': 'application/json', #on force la sortie au format json
            'response_schema': QuizOutput, #utilisation de la classe QuizOutput comme structure de renvoi
            'temperature': 0.2 #réduit la créativité , plus précis
        }
    )
    return response.parsed  #transforme en un objet python exploitable


