from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.questions_joueur import questions_joueur
from src.verifier_la_reponse_du_joueur import verifier_reponse

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    
    print("aled")
    return {"message": "Hello World"}


@app.get("/question/{theme}")
async def question(theme:str):

    if theme in ["Sciences et Ingénierie", "Musique", "Histoire et Littérature", "Nature et Géographie", "Internet", "Cinema"]:
        dix_questions = questions_joueur("src/database/api_culture.db", theme)
    return {"questions" : dix_questions}


@app.get("/verifier_reponse_joueur/{reponse_joueur}/{reponse_attendue}")
async def verifier_reponse_joueur(reponse_joueur: str, reponse_attendue: str):
    return verifier_reponse(reponse_joueur, reponse_attendue)
