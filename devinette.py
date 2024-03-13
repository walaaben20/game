from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class DevinetteApp(App):
    def build(self):
        self.choix = None
        self.mot_a_deviner = ""
        self.tentatives = 0

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label_titre = Label(text="Bienvenue dans le jeu Devinette de Wala !", font_size=30, color=(0,0,1,1))
        layout.add_widget(self.label_titre)

        self.label_instructions = Label(text="Joueur 1 : donnez le mot à deviner", font_size=30, color=(0, 0, 1, 1))
        layout.add_widget(self.label_instructions)

        self.input_mot = TextInput(hint_text="Entrez le mot", password=True, multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.input_mot)

        self.bouton_valider_mot = Button(text="Valider", on_press=self.valider_mot, background_color=(0, 1, 0, 1), size_hint_y=None, height=60)
        layout.add_widget(self.bouton_valider_mot)

        self.label_choix = Label(text="Joueur 2 : Choisissez 1 si vous voulez avoir des tentatives ou 2 pour deviner sans avoir des tentatives ",font_size=20, color=(0, 0, 1, 1))
        layout.add_widget(self.label_choix)

        self.input_choix = TextInput(hint_text="Entrez votre choix", multiline=False,size_hint_y=None, height=40)
        layout.add_widget(self.input_choix)

        self.bouton_valider_choix = Button(text="Valider", on_press=self.valider_choix,background_color=(0, 1, 0, 1), size_hint_y=None, height=60)
        layout.add_widget(self.bouton_valider_choix)

        self.label_message_joueur = Label(font_size=20)
        layout.add_widget(self.label_message_joueur)

        self.label_resultat = Label(font_size=20)
        layout.add_widget(self.label_resultat)

        self.input_mot.bind(on_text_validate=self.valider_mot_entree)  # Lier la touche "Entrée" à la fonction valider_mot_entree
        self.input_choix.bind(on_text_validate=self.valider_choix_entree)  # Lier la touche "Entrée" à la fonction valider_choix_entree

        return layout

    def valider_mot(self, instance):
        self.mot_a_deviner = self.input_mot.text
        self.input_mot.text = "*****"  # Remplacer le texte par des étoiles pour le cacher
        self.label_instructions.text = "Joueur 2 : devinez le mot"
        self.input_mot.disabled = True
        self.bouton_valider_mot.disabled = True

    def valider_mot_entree(self, instance):
        self.valider_mot(instance)

    def valider_choix(self, instance):
        choix = self.input_choix.text
        if choix == "1" or choix == "2":
            self.choix = int(choix)
            self.input_choix.disabled = True
            self.bouton_valider_choix.disabled = True
            self.label_choix.text = ""
            self.jouer()
        else:
            self.label_message_joueur.text = "Veuillez entrer 1 ou 2"

    def valider_choix_entree(self, instance):
        self.valider_choix(instance)

    def jouer(self):
        if self.choix == 1:
            self.label_instructions.text = "Joueur 2 : Vous avez 3 tentatives"
            self.tentatives = 3
        else:
            self.label_instructions.text = "Joueur 2 : Vous pouvez commencer à deviner"

        self.input_mot_joueur = TextInput(hint_text="Entrez votre devinette")  # Utilisation du texte sauvegardé
        self.root_widget.add_widget(self.input_mot_joueur)

        self.bouton_deviner = Button(text="Deviner", on_press=self.deviner_mot)
        self.root_widget.add_widget(self.bouton_deviner)

    def deviner_mot(self, instance):
        mot_joueur = self.input_mot_joueur.text
        if mot_joueur == self.mot_a_deviner:
            self.label_resultat.text = "Bravo! Vous avez deviné le mot correctement."
        else:
            self.tentatives -= 1
            if self.tentatives > 0:
                self.label_resultat.text = f"Incorrect! Il vous reste {self.tentatives} tentatives."
            else:
                self.label_resultat.text = f"Désolé, vous n'avez pas deviné le mot. Le mot était {self.mot_a_deviner}."


if __name__ == "__main__":
    DevinetteApp().run()
