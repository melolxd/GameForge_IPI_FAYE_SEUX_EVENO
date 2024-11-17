import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from redis_script import creer_profil, lire_profil, mettre_a_jour_profil, supprimer_profil

creer_profil(5, "Archer", "Hunter", 7, ["Bow"], ["Snipe"])
print("Profil après création :", lire_profil(5))

mettre_a_jour_profil(5, pseudo="Sniper")
print("Profil après mise à jour :", lire_profil(5))

supprimer_profil(5)
print("Profil supprimé.")

