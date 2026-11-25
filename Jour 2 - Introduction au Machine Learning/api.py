# Import de fastapi
from fastapi import FastAPI



# Création de l'objet FastAPI
app = FastAPI()


# Création d'une route
@app.get("/")
def root():
    return "Hello World"


@app.get("/square")
def square(n:int=0):
    return n*n


@app.get("/hello")
def hello(name:str="Jon Doe"):
    return f"Hello {name} !"


















import pickle


# Création d'un point de terminaison: train_perceptron 

@app.get("/train_perception")
def train_perception():
    import pandas as pd
    path = 'https://raw.githubusercontent.com/Quera-fr/Python-Programming/main/data_clean.csv'

    print("Télécharment des fichiers")
    df = pd.read_csv(path)

    y = df.Ever_Married
    X = df.drop(["Ever_Married"], axis=1)

    #import du modèle 
    from sklearn.linear_model import Perceptron

    model = Perceptron()
    print("Début de l'entrainement")
    #entreinement du modèle 
    model.fit(X, y)
    
    #évaluation du modèle 
    score = model.score(X, y)
    print("Evaluation du modèle, Accuracy : ", score)
    #retour avec le score 

    print("Save - model_ever_maried.pkl")
    with open("model_ever_maried.pkl", "wb") as f:
        pickle.dump(model, f)

    return float(score), "model_ever_maried.pkl"



# Création d'un point de terminaison: train_linear 
  

  








