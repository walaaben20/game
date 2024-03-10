import unittest
from devinette import Devinette

class TestDevinette(unittest.TestCase):
    def test_mot_valide(self):
        m = Devinette("")
        self.assertFalse(m.mot_valide(""))  # Test avec un mot vide
        self.assertTrue(m.mot_valide("Bonjour"))  # Test avec un mot valide
        self.assertFalse(m.mot_valide("123"))  # Test avec des chiffres

    def test_condition(self):
        d = Devinette(1)
        self.assertEqual(d.condition(), "vous avez 3 indices seulement")  # Test avec choix 1
        d = Devinette(2)
        self.assertEqual(d.condition(), "commencer sans indice")  # Test avec choix 2
        d = Devinette(3)
        self.assertEqual(d.condition(), "choisir 1 ou 2")  # Test avec choix par défaut

if __name__ == '__main__':
    unittest.main()