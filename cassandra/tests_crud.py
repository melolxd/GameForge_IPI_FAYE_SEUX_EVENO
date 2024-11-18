from crud_cassandra import create_stat, read_stat, update_xp, delete_stat
import uuid
from datetime import datetime



# Mon joueur de test
player_id = uuid.uuid4()
timestamp = datetime.now()
type_action = "attaque"
xp = 1500

print("---- TEST CRUD CASSANDRA ----")

# Test de l'insertion (CREATE)
print("---- CREATE ----")
create_stat(player_id, timestamp, type_action, xp)

# Test de la lecture (READ)
print("---- READ ----")
read_stat(player_id)

# Test de la mise à jour (UPDATE)
print("---- UPDATE ----")
new_xp = 2000
update_xp(player_id, new_xp)

# Vérification de la mise à jour en relisant les données
print("---- READ AFTER UPDATE ----")
read_stat(player_id)

# Test de la suppression (DELETE)
print("---- DELETE ----")
delete_stat(player_id)

# Vérification de la suppression en relisant les données
print("---- READ AFTER DELETE ----")
read_stat(player_id)
