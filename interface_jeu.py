import tkinter as tk

class DevinetteGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu de Devinette")

        self.label = tk.Label(master, text="Bienvenue dans le jeu Devinette !")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Valider", command=self.check_guess)
        self.button.pack()

    def check_guess(self):
        user_guess = self.entry.get()
        # Ajoutez ici la logique pour vérifier la devinette et afficher le résultat

if __name__ == "__main__":
    root = tk.Tk()
    app = DevinetteGUI(root)
    root.mainloop()