import sys
import os

# Ajouter le chemin vers le répertoire parent contenant redis_script.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from redis_script import mettre_a_jour_classement, recuperer_classement

# Test des classements
print("=== Test des Classements ===")
mettre_a_jour_classement("Hero", 100)
mettre_a_jour_classement("Wizard", 200)
mettre_a_jour_classement("Warrior", 150)

print("Classement complet :", recuperer_classement(10))
print("Top 3 :", recuperer_classement(3))
