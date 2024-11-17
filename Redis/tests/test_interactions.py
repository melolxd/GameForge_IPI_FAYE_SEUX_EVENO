import sys
import os
import time

# Ajouter le chemin vers le répertoire parent contenant redis_script.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from redis_script import enregistrer_combat, enregistrer_deplacement, recuperer_interactions

# Test des interactions en temps réel
print("=== Test des Combats ===")
enregistrer_combat(1, 2, 100, 1668619200, ttl=3)
print("Avant expiration :", recuperer_interactions("combat"))
time.sleep(4)
print("Après expiration :", recuperer_interactions("combat"))

print("\n=== Test des Déplacements ===")
enregistrer_deplacement(1, {"x": 5, "y": 10}, 1668619200, ttl=3)
print("Avant expiration :", recuperer_interactions("move"))
time.sleep(4)
print("Après expiration :", recuperer_interactions("move"))
