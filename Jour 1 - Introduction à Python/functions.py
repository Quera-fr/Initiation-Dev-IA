def password():    
    mot_de_passe_attendu = "Quera_Password"
    tentatives_max = 3
    for tentative in range(tentatives_max):
        mdp = input('Quel est le mot de passe ? ')
        if mdp == mot_de_passe_attendu:
            print("Mot de passe correct. Accès autorisé.")
            return True
        elif tentative != 2:
            print("Mot de passe incorrect. Il vous reste " + str(2 - tentative) + ' tentatives')
        else:
            print('Nombre maximal de tentatives atteint. Accès refusé.')
            return False

if __name__ == "__main__":
    password()
