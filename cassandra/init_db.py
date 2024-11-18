from cassandra.cluster import Cluster
import uuid
from datetime import datetime


def get_session():
    cluster = Cluster(['127.0.0.1'])  # Remplacez par l'adresse de votre cluster si nécessaire
    session = cluster.connect()
    return session


def create_keyspace(session):
    """
    Création du keyspace
    :param session: la connexion à la bdd cassandra
    :return:
    """
    query = """
    CREATE KEYSPACE IF NOT EXISTS tp_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};
    """
    session.execute(query)
    print("Keyspace 'tp_keyspace' créé ou déjà existant.")


def use_keyspace(session):
    """
    On se place sur le keyspace
    :param session: la connexion à la bdd cassandra
    :return:
    """
    query = "USE tp_keyspace;"
    session.execute(query)
    print("Keyspace 'tp_keyspace' utilisé.")


def create_table(session):
    query = """
    CREATE TABLE IF NOT EXISTS statistiques_joueur (
        player_id UUID PRIMARY KEY,
        type_action TEXT,
        xp int,
        timestamp TIMESTAMP
    );
    """
    session.execute(query)
    print("Table 'statistiques_joueur' créée ou déjà existante.")


def insert_sample_data(session):
    data = [
        ('attaque', 100, '2024-01-01 10:00:00'),
        ('defense', 50, '2024-01-02 11:30:00'),
        ('victoire', 200, '2024-01-03 14:20:00'),
        ('attaque', 120, '2024-01-04 09:45:00'),
        ('defense', 70, '2024-01-05 12:10:00'),
        ('victoire', 250, '2024-01-06 16:05:00'),
        ('attaque', 110, '2024-01-07 13:25:00'),
        ('defense', 65, '2024-01-08 08:30:00'),
        ('victoire', 300, '2024-01-09 17:50:00'),
        ('attaque', 130, '2024-01-10 19:15:00')
    ]

    # Pour chaque ligne de données, créer un UUID et insérer
    for action, xp, timestamp in data:
        query = """
        INSERT INTO statistiques_joueur (player_id, type_action, xp, timestamp) 
        VALUES (uuid(), %s, %s, %s);
        """
        session.execute(query, (action, xp, datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')))
        print(f"Donnée insérée pour l'action '{action}' avec {xp} XP.")


def main():
    try:
        session = get_session()
        create_keyspace(session)  # Crée le keyspace
        use_keyspace(session)  # Sélectionne le keyspace
        create_table(session)  # Crée la table
        insert_sample_data(session)  # Insère les données d'exemple
    except Exception as e:
        print(f"Erreur lors de l'exécution des commandes : {e}")


if __name__ == "__main__":
    main()
