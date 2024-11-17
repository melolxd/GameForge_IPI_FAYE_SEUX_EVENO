import sys
import os

# Ajouter le dossier parent pour importer redis_script
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from redis_script import enregistrer_deplacement, recuperer_deplacement
import time

# Enregistrer un déplacement
player_id = 1
position1 = "x:10,y:15"
timestamp1 = int(time.time())
enregistrer_deplacement(player_id, position1, timestamp1)
print(f"Déplacement enregistré pour le joueur {player_id}: {position1}")

# Récupérer le déplacement
mouvement = recuperer_deplacement(player_id)
print(f"Dernier déplacement récupéré : {mouvement}")

# Attendre que le TTL expire
print("Attente de 11 secondes pour tester l'expiration...")
time.sleep(11)
mouvement_expire = recuperer_deplacement(player_id)
print(f"Après expiration : {mouvement_expire}")
