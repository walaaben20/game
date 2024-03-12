from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import random

class JeuDevinette(App):
    def build(self):
        self.mot_a_deviner = self.generer_mot()
        self.tentatives_restantes = 3

        layout = BoxLayout(orientation='vertical')

        self.label_titre = Label(text="Bienvenue dans le jeu Devinette !", font_size=24)
        layout.add_widget(self.label_titre)

        self.label_instructions = Label(text="Trouvez le mot mystère en devinant les lettres.", font_size=16)
        layout.add_widget(self.label_instructions)

        self.label_mot = Label(text="_ " * len(self.mot_a_deviner), font_size=20)
        layout.add_widget(self.label_mot)

        self.label_tentatives = Label(text=f"Tentatives restantes : {self.tentatives_restantes}", font_size=16)
        layout.add_widget(self.label_tentatives)

        self.entree_lettre = TextInput(hint_text="Entrez une lettre", font_size=16)
        layout.add_widget(self.entree_lettre)

        self.bouton_valider = Button(text="Valider", font_size=16)
        self.bouton_valider.bind(on_press=self.valider_lettre)
        layout.add_widget(self.bouton_valider)

        return layout

    def generer_mot(self):
        mots = ["python", "programmation", "ordinateur", "jeu", "intelligence"]
        return random.choice(mots)

    def valider_lettre(self, instance):
        lettre = self.entree_lettre.text.lower()
        if len(lettre) != 1 or not lettre.isalpha():
            self.afficher_popup("Erreur", "Veuillez entrer une seule lettre valide.")
            return

        if lettre in self.mot_a_deviner:
            self.afficher_popup("Bravo", f"La lettre {lettre} est dans le mot mystère !")
            self.mettre_a_jour_mot(lettre)
        else:
            self.afficher_popup("Dommage", f"La lettre {lettre} n'est pas dans le mot mystère.")
            self.tentatives_restantes -= 1
            self.label_tentatives.text = f"Tentatives restantes : {self.tentatives_restantes}"
            if self.tentatives_restantes == 0:
                self.afficher_popup("Perdu", f"Le mot mystère était {self.mot_a_deviner}. Vous avez perdu !")

        self.entree_lettre.text = ""

    def mettre_a_jour_mot(self, lettre):
        nouveau_mot = ""
        for caractere in self.mot_a_deviner:
            if caractere == lettre:
                nouveau_mot += lettre + " "
            else:
                nouveau_mot += "_ "
        self.label_mot.text = nouveau_mot

    def afficher_popup(self, titre, message):
        popup = Popup(title=titre, content=Label(text=message, font_size=16), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == "__main__":
    JeuDevinette().run()
