import sys
import os

# Ajouter le chemin vers le répertoire parent contenant redis_script.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from redis_script import creer_profil, lire_profil, supprimer_profil
import unittest

class TestRedisProfiles(unittest.TestCase):
    def test_create_profiles(self):
        creer_profil(1, "TestUser", "Mage", 10, ["Épée"], ["Magie"])
        profil = lire_profil(1)
        self.assertEqual(profil["pseudo"], "TestUser")
        self.assertEqual(profil["classe"], "Mage")

    def test_delete_profiles(self):
        creer_profil(2, "TempUser", "Guerrier", 5, [], [])
        supprimer_profil(2)
        with self.assertRaises(ValueError):
            lire_profil(2)

if __name__ == "__main__":
    unittest.main()
