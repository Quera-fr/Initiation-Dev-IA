# Import de fastapi




# Création de l'objet FastAPI




# Création d'une route
























# Création d'un point de terminaison: train_perceptron 

@app.get("/train_perception")
def train_perception():
    import pandas as pd

    path = 'https://raw.githubusercontent.com/Quera-fr/Python-Programming/main/data_clean.csv'

    df = pd.read_csv(path)
    df

    y = df.Ever_Married
    X = df.drop(["Ever_Married"], axis=1)

    #import du modèle 
    
    #entreinement du modèle 

    #évaluation du modèle 

    #retour avec le score 



# Création d'un point de terminaison: train_linear 
  

  








