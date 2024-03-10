class Devinette:
    def __init__(self, choix):
        self.choix = choix

    def condition(self):
        if self.choix == 1:
            print("vous avez 3 indices seulement")
        elif self.choix == 2:
            print("commencer sans indice")
        else:
            print("choisir 1 ou 2")

    def mot_valide(self, mot):
        for c in mot:
            if not c.isalpha() or len(mot) == 0:
                return False
        return True

# Main code
print("Bienvenue dans le jeu Devinette !")
print("joueur 1 : donner votre mot à deviner : ")
mot = input()
m = Devinette(mot)

if not m.mot_valide(mot) or len(mot) == 0:
    while not m.mot_valide(mot) or len(mot) == 0:
        print("donner un autre mot :")
        mot = input()
        m = Devinette(mot)

print("joueur 2 : choisir 1 si vous voulez avoir un indice \n           sinon 2 si vous voulez commencer directement\n")
choix = int(input())
d = Devinette(choix)
d.condition()

if d.choix == 1:
    test = False
    i = 1
    while not test:
        print("joueur 1 : taper l'indice numéro :" + str(i))
        indice = input()
        print("joueur 2: deviner le mot: ")
        j2 = input()
        
        if j2 != mot:
            if i < 3:
                print("vous avez perdu la chance " + str(i))
                test = False
                i += 1
            else:
                print("fin de jeu, vous avez perdu")
                break
        else:
            test = True
            print("super ! vous avez gagné le jeu")
            break

if d.choix == 2:
    print("joueur 2: deviner le mot")
    i = 1
    test = False
    while not test:
        mot1 = input()
        
        if mot1 != mot:
            if i < 4:
                print("vous avez perdu la " + str(i) + " chance, devinez une autre fois :")
                test = False
                i += 1
            else:
                print("désolé(e), vous avez perdu le jeu.")
                break
        else:
            print("super! vous avez gagné !")
            test = True
            break