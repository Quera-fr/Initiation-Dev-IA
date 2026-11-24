def pass_word(mot_de_passe_attendu="Quera_Password", tentatives_max=3):
    
    print("Début de la fontion")
    
    for tentative in range(tentatives_max):
        mot_de_passe_saisi = input("Quel est votre mot de passe ?")

        if mot_de_passe_saisi == str(mot_de_passe_attendu):
            print("Mot de passe correct. Accès autorisé.")
            return True
        
        elif tentative != 2:
            print(f"Mot de passe incorrect. Il vous reste {tentatives_max-tentative-1} tentative(s).")
        
        else:
            print("Nombre maximal de tentatives atteint. Accès refusé.")
            return False


def test():
    print("Hello World")


if __name__ == "__main__":
    pass_word()