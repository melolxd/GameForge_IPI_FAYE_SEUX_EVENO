import redis
import time

# Connexion à Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Créer un profil joueur
def create_player_profile(player_id, pseudo, classe, niveau, competences, inventaire):
    key = f"player:{player_id}"
    redis_client.hset(key, mapping={
        "player_id": player_id,
        "pseudo": pseudo,
        "classe": classe,
        "niveau": niveau,
        "competences": competences,
        "inventaire": inventaire,
        "date_connexion": time.strftime('%Y-%m-%d %H:%M:%S')
    })
    print(f"Profil du joueur {pseudo} créé avec succès !")

# Mettre à jour un inventaire
def update_inventory(player_id, new_items):
    key = f"player:{player_id}"
    inventaire = redis_client.hget(key, "inventaire")
    updated_inventory = f"{inventaire},{new_items}" if inventaire else new_items
    redis_client.hset(key, "inventaire", updated_inventory)
    print(f"Inventaire du joueur {player_id} mis à jour : {updated_inventory}")

# Récupérer un profil
def get_player_profile(player_id):
    key = f"player:{player_id}"
    profile = redis_client.hgetall(key)
    if profile:
        print(f"Profil du joueur {player_id} : {profile}")
    else:
        print(f"Aucun profil trouvé pour le joueur {player_id}.")
    return profile

# Ajouter un score au classement
def update_leaderboard(player_id, score):
    redis_client.zadd("leaderboard", {player_id: score})
    print(f"Score du joueur {player_id} ajouté au classement.")

# Récupérer le top 10 des joueurs
def get_top_players():
    top_players = redis_client.zrevrange("leaderboard", 0, 9, withscores=True)
    print("Top 10 joueurs :", top_players)
    return top_players

# Enregistrer un mouvement avec TTL
def store_movement(player_id, x, y, ttl=60):
    key = f"move:{player_id}"
    redis_client.setex(key, ttl, f"{{'x': {x}, 'y': {y}}}")
    print(f"Mouvement du joueur {player_id} enregistré pour {ttl} secondes.")

# Enregistrer une attaque
def store_attack(player_id, enemy_id, damage):
    key = f"attack:{player_id}:{enemy_id}"
    redis_client.hset(key, mapping={
        "damage": damage,
        "timestamp": time.time()
    })
    print(f"Combat enregistré entre {player_id} et {enemy_id} avec {damage} dégâts.")
