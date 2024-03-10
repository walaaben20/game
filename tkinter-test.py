import unittest
import tkinter as tk
from interface_jeu import DevinetteGUI

class TestInterfaceGraphique(unittest.TestCase):
    def test_fenetre_principale(self):
        root = tk.Tk()
        self.assertIsInstance(root, tk.Tk)  # Vérifie que la fenêtre est bien une instance de Tkinter
        root.destroy()

if __name__ == '__main__':
    test_support.run_unittest(TestInterfaceGraphique)
    test_support.destroy_default_root()