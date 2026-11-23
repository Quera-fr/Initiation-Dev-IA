# Initiation au Machine Learning et à FastAPI

Cette journée présente les premières étapes du machine learning supervisé,
puis propose de découvrir FastAPI pour exposer une prédiction au moyen d'une
API.

## Contenu du projet

- `Machine_Learning_Perceptron.ipynb` : notebook de cours et d'exercices sur
  le perceptron et la régression linéaire.
- `api.py` : squelette à compléter pour créer une API FastAPI et un point de
  prédiction.

## Les notions abordées

### Machine learning

Le notebook s'appuie sur NumPy, Pandas et Scikit-learn pour manipuler des
données et entraîner des modèles.

- Chargement d'un jeu de données avec Pandas
- Séparation des variables explicatives `X` et de la cible `y`
- Principe d'un modèle de classification supervisée : le perceptron
- Entraînement, prédiction et évaluation d'un modèle
- Mise en pratique avec un projet de régression linéaire

L'exemple du perceptron utilise la colonne `Ever_Married` comme cible. Le
notebook contient des étapes guidées à compléter ainsi qu'un exercice de
régression linéaire.

### Création d'une API avec FastAPI

Le fichier `api.py` sert de point de départ pour apprendre à :

- importer FastAPI et créer une application ;
- déclarer une route ;
- ajouter un point de terminaison pour recevoir des données et renvoyer une
  prédiction.

Le fichier est un squelette pédagogique : il faut compléter l'application et
les routes avant de pouvoir démarrer le serveur.

## Installer les dépendances

Depuis le dossier du jour 2, installez les bibliothèques nécessaires :

```bash
pip install numpy pandas scikit-learn fastapi uvicorn
```

Le notebook charge son jeu de données depuis une URL GitHub ; une connexion
Internet est nécessaire pour exécuter cette étape.

## Lancer l'API

Après avoir défini l'application FastAPI dans `api.py`, démarrez le serveur
avec :

```bash
uvicorn api:app --reload
```

L'interface interactive de documentation est alors disponible à
`http://127.0.0.1:8000/docs`.
