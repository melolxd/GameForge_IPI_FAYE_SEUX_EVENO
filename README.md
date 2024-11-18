# **GameForge - Projet IPI**

## **Description**
GameForge est un projet collaboratif de gestion de jeux multijoueurs massifs développé dans le cadre du TP IPI. Ce projet repose sur une architecture distribuée combinant trois bases de données pour optimiser les performances et la gestion des données :
- **Redis** : Gestion en temps réel (interactions, profils, classements).
- **MongoDB** : Stockage de données complexes et persistantes.
- **Cassandra** : Analyse et stockage massif des logs.

---

## **Installation de l'Environnement**

### **Prérequis**
Assurez-vous d'avoir installé :
- **Python 3.9+**
- **Docker et Docker Compose**

### **Étapes d'Installation**

1. **Cloner le dépôt** :
    ```bash
    git clone https://github.com/melolxd/GameForge_IPI_FAYE_SEUX_EVENO.git
    cd GameForge_IPI_FAYE_SEUX_EVENO
    ```

2. **Créer et activer un environnement virtuel** :
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Installer les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```

4. **Démarrer les services via Docker Compose** :
    ```bash
    cd docker
    docker-compose up -d
    ```
    Le fichier docker-compose a été fait intégralement par Alexis EVENO

5. **Vérifier que Redis fonctionne** :
    ```bash
    redis-cli ping
    ```
    Résultat attendu :
    ```
    PONG
    ```

---

## **Partie Redis**

### **Fonctionnalités Implémentées**

1. **Gestion des Profils** :
   - Création, lecture, mise à jour et suppression des profils.
   - Informations prises en charge :
     - **Pseudo**
     - **Classe**
     - **Niveau**
     - **Inventaire**
     - **Compétences**

2. **Interactions en Temps Réel** :
   - Journalisation des combats et déplacements des joueurs avec expiration automatique (TTL).

3. **Classements** :
   - Gestion des scores et des classements :
     - Récupération des meilleurs joueurs (top N).
     - Classements par périodes définies.

---

### **Commandes Importantes**

1. **Lancer les tests unitaires** :
    ```bash
    python3 -m unittest discover -s tests -p "test_*.py"
    ```

2. **Exemples d'utilisation** :

   - **Créer un profil** :
     ```python
     creer_profil(1, "TestUser", "Mage", 10, ["Épée"], ["Magie"])
     print(lire_profil(1))
     ```

   - **Enregistrer un combat** :
     ```python
     enregistrer_combat(1, 2, 50, int(time.time()))
     print(recuperer_interactions("combat"))
     ```

   - **Mettre à jour un score et récupérer le classement** :
     ```python
     mettre_a_jour_classement("player1", 100)
     print(recuperer_classement(3))
     ```

---

## **Partie MongoDB**
**Fonctionnalités Implémentées** :  

---

## **Partie Cassandra**
**Fonctionnalités Implémentées** :  
Avec Cassandra, on souhaite enregistrer des statistiques concernant les joueurs, par exemple: le nombre d'expérience que chaque actions rapporte.

- **Créer une statistique**:
```python
create_stat(player_id, timestamp, type_action, xp)

```

- **Lire une statistique**:
```python
read_stat(player_id)
```

- **Mettre à jour une statistique**:
```python
new_xp = 2000
update_xp(player_id, new_xp)

```

- **Supprimer une statistique**:
```python
delete_stat(player_id)
```


Notre base de données Cassandra est situé dans un cluster avec plusieurs noeuds, ce qui rend la rend scalable et tolérente aux pannes.
Les noeux se partagent les données situé dans le keyspace.

Plus d'info dans la documentation technique.
## **Auteurs**
- **Redis** : Mattéo FAYE
- **MongoDB** : Mylan SEUX
- **Cassandra** : Alexis EVENO