# Initiation au développement IA

Ce dépôt accompagne une journée d'initiation à Python. Il contient un
notebook de cours avec des exercices guidés, puis une page d'exercice avec
Streamlit.

## Contenu du projet

- `1. Introduction à Python.ipynb` : cours interactif pour découvrir Python.
- `Home.py` : base d'une application Streamlit à compléter.

## Les notions abordées

### Python

- Variables et types : `int`, `float`, `str`, `bool` et `list`
- Opérations arithmétiques
- Chaînes de caractères et concaténation
- Fonctions intégrées : `input()`, `print()`, `range()`, `type()`, `len()`...
- Comparaisons : `==`, `!=`, `<`, `<=`, `>`, `>=`
- Opérateurs logiques : `and`, `or`, `not`, `in`
- Conditions : `if`, `elif`, `else`
- Boucles : `for`, `while`, `break` et `continue`
- Exercices avec des listes, des saisies utilisateur et des boucles

### Projet : gestion de mot de passe

Le projet demande de créer un programme qui :

1. Stocke un mot de passe attendu.
2. Autorise au maximum trois tentatives.
3. Demande le mot de passe à l'utilisateur avec `input()`.
4. Affiche un message lorsque l'accès est autorisé ou refusé.
5. Arrête la boucle immédiatement lorsque le mot de passe est correct.

Exemple de variables principales :

```python
mot_de_passe_attendu = "Quera_Password"
tentatives_max = 3
```

### Introduction à Streamlit

Le fichier `Home.py` prépare une interface avec les éléments suivants :

- un titre ;
- du texte ;
- un champ de saisie ;
- un bouton ;
- une image ;
- une vidéo ;
- des colonnes ;
- une barre latérale ;
- une seconde page.


## Installer Streamlit

```bash
pip install streamlit
```

Puis lancez l'application :

```bash
streamlit run Home.py
```
