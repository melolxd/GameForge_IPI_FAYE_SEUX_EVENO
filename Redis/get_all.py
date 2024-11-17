import redis
import json

# Configuration Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

def verifier_profil(player_id):
    """Récupère et affiche les informations d'un profil joueur."""
    profil = redis_client.hgetall(f"profile:{player_id}")
    if not profil:
        print(f"Aucun profil trouvé pour l'ID joueur {player_id}")
        return None

    # Convertir les champs JSON en listes
    profil["inventaire"] = json.loads(profil["inventaire"])
    profil["competences"] = json.loads(profil["competences"])

    print(f"Profil pour l'ID {player_id} : {profil}")
    return profil

def verifier_tous_les_profils(limite=10):
    """Affiche les informations des premiers profils jusqu'à une limite."""
    clefs = redis_client.keys("profile:*")[:limite]
    if not clefs:
        print("Aucun profil trouvé dans Redis.")
        return

    print(f"Les {limite} premiers profils :")
    for clef in clefs:
        profil = redis_client.hgetall(clef)
        profil["inventaire"] = json.loads(profil["inventaire"])
        profil["competences"] = json.loads(profil["competences"])
        print(f"{clef} : {profil}")

def verifier_classement(top_n=10):
    """Récupère et affiche le classement des joueurs."""
    classement = redis_client.zrevrange("leaderboard", 0, top_n - 1, withscores=True)
    if not classement:
        print("Aucun joueur dans le classement.")
        return

    print(f"Top {top_n} du classement :")
    for rank, (player_id, score) in enumerate(classement, start=1):
        print(f"{rank}. {player_id} - {score} points")

if __name__ == "__main__":
    print("=== Vérification des Données Redis ===")
    print("1. Vérifier un profil spécifique")
    verifier_profil(1)

    print("\n2. Vérifier plusieurs profils")
    verifier_tous_les_profils(5)

    print("\n3. Vérifier le classement")
    verifier_classement(10)
