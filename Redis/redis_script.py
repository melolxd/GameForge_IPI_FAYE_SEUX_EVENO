import redis
import json

# Connexion à Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# CRUD des Profils
def creer_profil(player_id, pseudo, classe, niveau, inventaire, competences):
    """Créer ou mettre à jour un profil joueur."""
    profil = {
        "pseudo": pseudo,
        "classe": classe,
        "niveau": niveau,
        "inventaire": json.dumps(inventaire),
        "competences": json.dumps(competences),
    }
    redis_client.hset(f"profile:{player_id}", mapping=profil)

def lire_profil(player_id):
    profil = redis_client.hgetall(f"profile:{player_id}")
    if not profil:
        raise ValueError(f"Aucun profil trouvé pour l'ID joueur {player_id}")
    profil["inventaire"] = json.loads(profil["inventaire"])
    profil["competences"] = json.loads(profil.get("competences", "[]"))
    return profil

def mettre_a_jour_profil(player_id, **kwargs):
    """Mettre à jour un profil joueur avec les données fournies."""
    key = f"profile:{player_id}"
    for champ, valeur in kwargs.items():
        if champ in ["inventaire", "competences"]:
            valeur = json.dumps(valeur)
        redis_client.hset(key, champ, valeur)

def supprimer_profil(player_id):
    """Supprimer un profil joueur."""
    redis_client.delete(f"profile:{player_id}")

def statistiques_competences():
    """Calculer les statistiques globales des compétences."""
    statistiques = {}
    for key in redis_client.keys("profile:*"):
        profil = redis_client.hgetall(key)
        competences = json.loads(profil.get("competences", "[]"))
        for competence in competences:
            statistiques[competence] = statistiques.get(competence, 0) + 1
    return statistiques

# CRUD des Interactions
def enregistrer_combat(player_id, ennemi_id, degats, timestamp):
    """Journaliser un combat avec un TTL."""
    key = f"combat:{player_id}:{ennemi_id}"
    combat = {"degats": degats, "timestamp": timestamp}
    redis_client.set(key, json.dumps(combat), ex=60)

def enregistrer_deplacement(player_id, position, timestamp):
    """Journaliser un déplacement d'un joueur avec un TTL."""
    key = f"move:{player_id}"
    mouvement = {
        "position": position,
        "timestamp": timestamp
    }
    redis_client.set(key, json.dumps(mouvement), ex=10)

def recuperer_deplacement(player_id):
    """Récupérer le dernier déplacement d'un joueur."""
    key = f"move:{player_id}"
    mouvement = redis_client.get(key)
    if mouvement:
        return json.loads(mouvement)
    else:
        return f"Aucun déplacement trouvé pour le joueur {player_id}"

def recuperer_interactions(prefixe, filtre_temps=None):
    """Récupérer les actions (combat, déplacement) avec un filtre optionnel."""
    cles = redis_client.keys(f"{prefixe}:*")
    resultats = []
    for cle in cles:
        donnees = redis_client.get(cle)
        if donnees:
            donnees = json.loads(donnees)
            if not filtre_temps or donnees["timestamp"] >= filtre_temps:
                resultats.append(donnees)
    return resultats

# CRUD des Classements

def mettre_a_jour_classement(player_id, score):
    """Mettre à jour le classement des joueurs."""
    redis_client.zadd("leaderboard", {player_id: score})

def recuperer_classement(top_n=10):
    """Récupérer les N meilleurs joueurs."""
    return redis_client.zrevrange("leaderboard", 0, top_n - 1, withscores=True)

def classement_par_periode(min_timestamp, max_timestamp):
    """Obtenir un classement entre deux timestamps."""
    return redis_client.zrangebyscore("leaderboard", min_timestamp, max_timestamp, withscores=True)
