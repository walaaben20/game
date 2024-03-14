import pytest
from kivy.clock import Clock
from kivy.tests.common import GraphicUnitTest

from devinette.py import DevinetteApp


@pytest.fixture
def app():
    app = DevinetteApp()
    yield app
    app.stop()


class TestDevinetteApp(GraphicUnitTest):
    def test_valider_mot(self, app):
        # Appel de la méthode valider_mot
        app.valider_mot(None)

        # Vérification que l'étiquette d'instructions est mise à jour
        assert app.label_instructions.text == "Joueur 2 : devinez le mot"

        # Vérification que le champ de texte est désactivé
        assert app.input_mot.disabled
        # Vérification que le bouton est désactivé
        assert app.bouton_valider_mot.disabled

    def test_valider_choix(self, app):
        # Appel de la méthode valider_choix avec un choix valide
        app.input_choix.text = "1"
        app.valider_choix(None)

        # Vérification que l'étiquette d'instructions est mise à jour
        assert app.label_instructions.text == "Joueur 2 : Vous avez 3 tentatives"

        # Appel de la méthode valider_choix avec un choix invalide
        app.input_choix.text = "3"
        app.valider_choix(None)

        # Vérification que l'étiquette de message joueur est mise à jour
        assert app.label_message_joueur.text == "Veuillez entrer 1 ou 2"

    def test_deviner_mot_correct(self, app):
        # Configuration de l'état du jeu
        app.mot_a_deviner = "test"
        app.input_mot_joueur.text = "test"

        # Appel de la méthode deviner_mot avec une devinette correcte
        app.deviner_mot(None)

        # Vérification que le résultat est affiché correctement
        assert app.label_resultat.text == "Bravo! Vous avez deviné le mot correctement."

    def test_deviner_mot_incorrect(self, app):
        # Configuration de l'état du jeu
        app.mot_a_deviner = "test"
        app.input_mot_joueur.text = "incorrect"

        # Appel de la méthode deviner_mot avec une devinette incorrecte
        app.deviner_mot(None)

        # Vérification que le résultat est affiché correctement
        assert app.label_resultat.text == "Désolé, vous n'avez pas deviné le mot. Le mot était test."
