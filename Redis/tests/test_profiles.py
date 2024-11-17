import unittest
import sys
import os

# Ajouter le dossier parent pour importer redis_script
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from redis_script import creer_profil, lire_profil, supprimer_profil

class TestRedisProfiles(unittest.TestCase):
    def test_create_profiles(self):
        # Créer des profils
        creer_profil(
            player_id=1,
            pseudo="Pattéo",
            classe="Voleur",
            niveau=20,
            inventaire=["Dagues jumelles", "Lame empoisonnée"],
            competences=["Furtivité", "Vol épique"]
        )
        profile_matteo = lire_profil(1)
        self.assertEqual(profile_matteo["pseudo"], "Pattéo")
        self.assertEqual(profile_matteo["classe"], "Voleur")

        creer_profil(
            player_id=2,
            pseudo="Pylan",
            classe="Cuisinier",
            niveau=15,
            inventaire=["Spatule sacrée", "Couteau de chef légendaire"],
            competences=["Motivation culinaire"]
        )
        profile_mylan = lire_profil(2)
        self.assertEqual(profile_mylan["pseudo"], "Pylan")
        self.assertEqual(profile_mylan["classe"], "Cuisinier")

        creer_profil(
            player_id=3,
            pseudo="Palexis",
            classe="Hooligan",
            niveau=25,
            inventaire=["Chaise pliante", "Bâton de hooligan"],
            competences=["Troupes enragées"]
        )
        profile_alexis = lire_profil(3)
        self.assertEqual(profile_alexis["pseudo"], "Palexis")
        self.assertEqual(profile_alexis["classe"], "Hooligan")

    def test_retrieve_profiles(self):
        # Vérification que les profils créés sont bien récupérables
        profile_matteo = lire_profil(1)
        self.assertIn("pseudo", profile_matteo)
        self.assertEqual(profile_matteo["pseudo"], "Pattéo")

        profile_mylan = lire_profil(2)
        self.assertIn("pseudo", profile_mylan)
        self.assertEqual(profile_mylan["pseudo"], "Pylan")

        profile_alexis = lire_profil(3)
        self.assertIn("pseudo", profile_alexis)
        self.assertEqual(profile_alexis["pseudo"], "Palexis")

if __name__ == '__main__':
    unittest.main()
