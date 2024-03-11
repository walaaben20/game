import tkinter as tk

class JeuDevinette(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jeu de Devinette")
        self.geometry("400x200")
        self.configure(bg='black')

        self.mot_a_deviner = ""
        self.indice = 0

        self.label1 = tk.Label(self, text="Joueur 1: Saisissez un mot à deviner :", fg='white', bg='black')
        self.label1.pack()

        self.entry1 = tk.Entry(self, show="*")
        self.entry1.pack()

        self.label2 = tk.Label(self, text="Joueur 2: Choisissez 1 pour commencer sans indice ou 2 pour avoir 3 indices", fg='white', bg='black')
        self.label2.pack()

        self.entry2 = tk.Entry(self)
        self.entry2.pack()

        self.button = tk.Button(self, text="Valider", command=self.start_game)
        self.button.pack()

    def start_game(self):
        self.mot_a_deviner = self.entry1.get()
        choix = int(self.entry2.get())

        if choix == 1:
            print("Le joueur 2 commence sans indice.")
            # Ajoutez ici la logique pour permettre au joueur 2 de deviner sans indice
        elif choix == 2:
            print("Le joueur 2 a choisi d'avoir 3 indices.")
            # Ajoutez ici la logique pour donner des indices au joueur 2 et lui permettre de deviner

if __name__ == '__main__':
    app = JeuDevinette()
    app.mainloop()