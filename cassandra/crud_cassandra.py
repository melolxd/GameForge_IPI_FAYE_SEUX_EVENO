from cassandra.cluster import Cluster
import uuid
from datetime import datetime

def get_session():
    """
    Connexion à Cassandra
    :return: code de retour
    """
    try:
        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect('tp_keyspace')
        print("Connexion à Cassandra réussie")
        return session
    except Exception as e:
        print(f"Erreur lors de la connexion à Cassandra: {e}")
        return None

def create_stat(player_id, timestamp, type_action, xp):
    """
    Créer un nouvel enregistrement
    :param player_id: id du joueur
    :param timestamp: timestamp de l'action
    :param type_action: le type de l'action: victoire, défaite, défense, attaque
    :param xp: l'xp récupérer suite à l'action
    :return: code de retour
    """
    session = get_session()

    if not isinstance(player_id, uuid.UUID):
        print("Erreur : player_id doit être un UUID")
        return
    if not isinstance(timestamp, datetime):
        print("Erreur : timestamp doit être un datetime")
        return

    try:
        query = "INSERT INTO statistiques_joueur (player_id, timestamp, type_action, xp) VALUES (%s, '%s', %s, %s)"
        session.execute(query, (player_id, timestamp, type_action, xp))  # Exécution avec les paramètres
        print(f"Statistiques créées pour le joueur {player_id}")
    except Exception as e:
        print(f"Erreur lors de l'insertion dans la table : {e}")


def read_stat(player_id):
    """
    Lire un enregistrement par player_id
    :param player_id: id du joueur
    :return: code de retour
    """
    session = get_session()

    try:
        query = "SELECT * FROM statistiques_joueur WHERE player_id = %s"
        result = session.execute(query, (player_id,))  # Exécution avec les paramètres

        # Affichage des résultats
        for row in result:
            print(f"Player ID: {row.player_id}, Timestamp: {row.timestamp}, Type Action: {row.type_action}, XP: {row.xp}")
    except Exception as e:
        print(f"Erreur lors de la lecture de la table : {e}")


def update_xp(player_id, new_xp):
    """
    Mettre à jour les points d'expérience d'un joueur
    :param player_id: id du joueur
    :param new_xp: le bouveau montant d'xp
    :return: code de retour
    """
    session = get_session()

    try:
        query = "UPDATE statistiques_joueur SET xp = %s WHERE player_id = %s"
        session.execute(query, (new_xp, player_id,))  # Exécution avec les paramètres
        print(f"XP du joueur {player_id}  mis à jour à {new_xp}")
    except Exception as e:
        print(f"Erreur lors de la mise à jour de la table : {e}")


def delete_stat(player_id):
    """
    Supprimer un enregistrement par player_id
    :param player_id: id du joueur
    :return: code de retour
    """
    session = get_session()

    try:
        query = "DELETE FROM statistiques_joueur WHERE player_id = %s"
        session.execute(query, (player_id,))  # Exécution avec les paramètres
        print(f"Statistiques supprimées pour le joueur {player_id}")
    except Exception as e:
        print(f"Erreur lors de la suppression de la table : {e}")
