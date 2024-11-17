import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from redis_script import enregistrer_combat, enregistrer_deplacement, recuperer_interactions

class TestRedisInteractions(unittest.TestCase):
    def test_enregistrer_combat(self):
        enregistrer_combat(1, 2, 50, 1668619200)
        combats = recuperer_interactions("combat")
        self.assertTrue(len(combats) > 0)
        self.assertEqual(combats[0]["degats"], 50)

    def test_enregistrer_deplacement(self):
        enregistrer_deplacement(1, {"x": 10, "y": 20}, 1668619200)
        mouvements = recuperer_interactions("move")
        self.assertTrue(len(mouvements) > 0)
        self.assertEqual(mouvements[0]["position"], {"x": 10, "y": 20})

if __name__ == "__main__":
    unittest.main()
