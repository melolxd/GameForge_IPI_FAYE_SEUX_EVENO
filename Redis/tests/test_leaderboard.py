import unittest
import sys
import os

# Ajouter le chemin vers le script principal
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from redis_script import mettre_a_jour_classement, recuperer_classement

class TestLeaderboard(unittest.TestCase):
    def test_mettre_a_jour_et_recuperer_classement(self):
        # Ajouter des joueurs au classement
        mettre_a_jour_classement("Pylan", 100)
        mettre_a_jour_classement("Pattéo", 200)

        # Récupérer les meilleurs joueurs
        classement = recuperer_classement(2)
        self.assertEqual(classement[0][0], "Pattéo")
        self.assertEqual(classement[1][0], "Pylan")

if __name__ == "__main__":
    unittest.main()
