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
        if len(mot) == 0:
            return False
        for c in mot:
            if not c.isalpha():
                return False
        return True

