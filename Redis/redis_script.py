import redis
import json
import logging

# Configuration de Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Configuration des logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Validation des données
def valider_donnees_profil(pseudo, classe, niveau, inventaire, competences):
    if not isinstance(pseudo, str) or len(pseudo) < 1:
        raise ValueError("Le pseudo doit être une chaîne non vide.")
    if not isinstance(classe, str):
        raise ValueError("La classe doit être une chaîne.")
    if not isinstance(niveau, int) or niveau < 0:
        raise ValueError("Le niveau doit être un entier positif.")
    if not isinstance(inventaire, list):
        raise ValueError("L'inventaire doit être une liste.")
    if not isinstance(competences, list):
        raise ValueError("Les compétences doivent être une liste.")

# CRUD des Profils
def creer_profil(player_id, pseudo, classe, niveau, inventaire, competences):
    """Créer ou mettre à jour un profil joueur."""
    valider_donnees_profil(pseudo, classe, niveau, inventaire, competences)
    profil = {
        "pseudo": pseudo,
        "classe": classe,
        "niveau": niveau,
        "inventaire": json.dumps(inventaire),
        "competences": json.dumps(competences),
    }
    redis_client.hset(f"profile:{player_id}", mapping=profil)
    logger.info(f"Profil créé pour player_id={player_id}")

def lire_profil(player_id):
    profil = redis_client.hgetall(f"profile:{player_id}")
    if not profil:
        raise ValueError(f"Aucun profil trouvé pour l'ID joueur {player_id}")
    profil["inventaire"] = json.loads(profil["inventaire"])
    profil["competences"] = json.loads(profil.get("competences", "[]"))
    return profil

def supprimer_profil(player_id):
    redis_client.delete(f"profile:{player_id}")
    logger.info(f"Profil supprimé pour player_id={player_id}")

def mettre_a_jour_profil(player_id, **kwargs):
    """Mettre à jour un profil joueur avec les données fournies."""
    key = f"profile:{player_id}"
    for champ, valeur in kwargs.items():
        if champ in ["inventaire", "competences"]:
            valeur = json.dumps(valeur)
        redis_client.hset(key, champ, valeur)
    logger.info(f"Profil mis à jour pour player_id={player_id} avec {kwargs}")

def rechercher_par_classe(classe):
    """Rechercher les joueurs par classe."""
    logger.info(f"Recherche des joueurs de classe {classe}")
    joueurs = []
    for key in redis_client.keys("profile:*"):
        profil = redis_client.hgetall(key)
        if profil.get("classe") == classe:
            joueurs.append(profil)
    return joueurs

# CRUD des Interactions
def enregistrer_combat(player_id, ennemi_id, degats, timestamp, ttl=60):
    key = f"combat:{player_id}:{ennemi_id}"
    combat = {"degats": degats, "timestamp": timestamp}
    redis_client.set(key, json.dumps(combat), ex=ttl)
    logger.info(f"Combat enregistré entre {player_id} et {ennemi_id} avec {degats} dégâts.")

def recuperer_deplacement(player_id, filtre_temps=None):
    """Récupérer les déplacements d'un joueur spécifique."""
    key = f"move:{player_id}"
    ttl = redis_client.ttl(key)
    if ttl > 0:
        donnees = redis_client.get(key)
        if donnees:
            mouvement = json.loads(donnees)
            if not filtre_temps or mouvement["timestamp"] >= filtre_temps:
                return mouvement
    return None

def enregistrer_deplacement(player_id, position, timestamp, ttl=10):
    key = f"move:{player_id}"
    mouvement = {"position": position, "timestamp": timestamp}
    redis_client.set(key, json.dumps(mouvement), ex=ttl)
    logger.info(f"Déplacement enregistré pour player_id={player_id} à {position}.")

def recuperer_interactions(prefixe, filtre_temps=None):
    """Récupérer les actions (combat, déplacement) avec un filtre optionnel."""
    cles = redis_client.keys(f"{prefixe}:*")
    resultats = []
    for cle in cles:
        ttl = redis_client.ttl(cle)
        if ttl > 0:
            donnees = redis_client.get(cle)
            if donnees:
                donnees = json.loads(donnees)
                if not filtre_temps or donnees["timestamp"] >= filtre_temps:
                    resultats.append(donnees)
    return resultats


# CRUD des Classements
def mettre_a_jour_classement(player_id, score):
    redis_client.zadd("leaderboard", {player_id: score})
    logger.info(f"Score de {score} mis à jour pour player_id={player_id}.")

def recuperer_classement(top_n=10):
    return redis_client.zrevrange("leaderboard", 0, top_n - 1, withscores=True)

