from pymongo import MongoClient
def get_database():
    client = MongoClient('localhost', 27017)
    db = client['mydatabase']
    return db


def main():
    db = get_database()
    
    # Check if collections exist and drop them if they do
    collections = ['Compétences', 'Inventaire', 'Joueurs']
    for collection in collections:
        if collection in db.list_collection_names():
            db[collection].drop()
    
    # Create collections
    db.create_collection('Compétences')
    db.create_collection('Inventaire')
    db.create_collection('Joueurs')

    # Insert data into Compétences
    
    ajouterCompetence("Bouclier Magique", 15)
    ajouterCompetence("Frappe de Foudre", 12)
    ajouterCompetence("Coup Rapide", 5)
    ajouterCompetence("Soin", 8)
    ajouterCompetence("Cri de Guerre", 20)
    ajouterCompetence("Pluie de Flèches", 18)
    ajouterCompetence("Invisibilité", 25)
    ajouterCompetence("Téléportation", 30)
    ajouterCompetence("Rage du Berserker", 40)
    ajouterCompetence("Vague de Feu", 22)
    ajouterCompetence("Mur de Glace", 28)
    ajouterCompetence("Poison Mortel", 12)
    ajouterCompetence("Guérison de Masse", 50)
    ajouterCompetence("Éclair de Givre", 14)
    ajouterCompetence("Explosion Sismique", 45)
    ajouterCompetence("Bouclier Divin", 60)
    ajouterCompetence("Lame Sanguinaire", 20)
    ajouterCompetence("Barrière de Vent", 25)
    ajouterCompetence("Éclair du Phoenix", 55)
    # Insert data into Inventaire
    
    ajouterInventaire("Épée du Brave")
    ajouterInventaire("Bouclier de Fer")
    ajouterInventaire("Potion de Soin")
    ajouterInventaire("Potion de Mana")
    ajouterInventaire("Arc Long")
    ajouterInventaire("Amulette de Force")
    ajouterInventaire("Anneau de Sagesse")
    ajouterInventaire("Cape d'Invisibilité")
    ajouterInventaire("Bottes de Vitesse")
    ajouterInventaire("Casque de l'Inébranlable")
    ajouterInventaire("Gants d'Assassin")
    ajouterInventaire("Hache de Guerre")
    ajouterInventaire("Bâton de Mage")
    ajouterInventaire("Anneau de Régénération")
    ajouterInventaire("Talisman de Protection")
    ajouterInventaire("Potion d'Énergie")
    ajouterInventaire("Ceinture du Gladiateur")
    ajouterInventaire("Potion de Résistance")
    ajouterInventaire("Bottes de Lévitation")
    ajouterInventaire("Cape de Résistance au Feu")
    ajouterInventaire("Épée Enflammée")
    ajouterInventaire("Casque d'Immunité")
    ajouterInventaire("Gantelets de Force")
    ajouterInventaire("Bouclier Mystique")
    ajouterInventaire("Potion de Puissance")
    ajouterInventaire("Talisman de Vitesse")
    ajouterInventaire("Lance de Glace")
    ajouterInventaire("Cape de l'Ombre")
    ajouterInventaire("Ceinture de Vitalité")
    ajouterInventaire("Bouclier Solaire")
    
    ajouterJoueur(
        "DragonSlayer", "Guerrier", 35,
        [{"_id": 1}, {"_id": 7}],
        [{"_id": 1, "quantite": 1}, {"_id": 2, "quantite": 1}, {"_id": 14, "quantite": 2}],
        "2024-11-01"
    )
    ajouterJoueur(
        "MysticMage", "Mage", 40,
        [{"_id": 4}, {"_id": 13}],
        [{"_id": 4, "quantite": 5}, {"_id": 13, "quantite": 1}, {"_id": 20, "quantite": 1}],
        "2024-10-30"
    )
    ajouterJoueur(
        "ShadowStalker", "Assassin", 28,
        [{"_id": 8}, {"_id": 11}],
        [{"_id": 9, "quantite": 1}, {"_id": 8, "quantite": 1}, {"_id": 11, "quantite": 2}],
        "2024-10-29"
    )
    ajouterJoueur(
        "HolyPriest", "Prêtre", 33,
        [{"_id": 10}, {"_id": 16}],
        [{"_id": 3, "quantite": 10}, {"_id": 7, "quantite": 1}, {"_id": 14, "quantite": 1}],
        "2024-11-02"
    )
    ajouterJoueur(
        "ThunderKing", "Guerrier", 37,
        [{"_id": 3}, {"_id": 9}],
        [{"_id": 5, "quantite": 1}, {"_id": 17, "quantite": 1}, {"_id": 6, "quantite": 3}],
        "2024-10-28"
    )
    ajouterJoueur(
        "FireWizard", "Mage", 45,
        [{"_id": 6}, {"_id": 20}],
        [{"_id": 4, "quantite": 7}, {"_id": 21, "quantite": 1}, {"_id": 13, "quantite": 1}],
        "2024-11-03"
    )
    ajouterJoueur(
        "SilentArrow", "Archer", 29,
        [{"_id": 5}, {"_id": 18}],
        [{"_id": 5, "quantite": 1}, {"_id": 26, "quantite": 2}, {"_id": 10, "quantite": 1}],
        "2024-11-01"
    )
    ajouterJoueur(
        "IceQueen", "Mage", 42,
        [{"_id": 4}, {"_id": 19}],
        [{"_id": 27, "quantite": 1}, {"_id": 24, "quantite": 1}, {"_id": 15, "quantite": 1}],
        "2024-10-31"
    )
    ajouterJoueur(
        "StormChaser", "Éclaireur", 38,
        [{"_id": 2}, {"_id": 12}],
        [{"_id": 19, "quantite": 1}, {"_id": 9, "quantite": 1}, {"_id": 26, "quantite": 1}],
        "2024-10-27"
    )
    ajouterJoueur(
        "IronFist", "Guerrier", 50,
        [{"_id": 1}, {"_id": 15}],
        [{"_id": 12, "quantite": 1}, {"_id": 23, "quantite": 1}, {"_id": 2, "quantite": 2}],
        "2024-11-04"
    )

    # Update data
    addNiveau(1, 3)

def ajouterCompetence(nom, description):
    db = get_database()
    collection = db['Compétences']
    competence = {
        '_id': collection.count_documents({}) + 1,
        'nom': nom,
        'description': description
    }
    collection.insert_one(competence)

def ajouterInventaire(nom):
    db = get_database()
    collection = db['Inventaire']
    inventaire = {
        '_id': collection.count_documents({}) + 1,
        'nom': nom
    }
    collection.insert_one(inventaire)
    
def ajouterJoueur(pseudo, classe, niveau, competences, inventaire, date_connexion):
    db = get_database()
    collection = db['Joueurs']
    joueur = {
        'pseudo': pseudo,
        'classe': classe,
        'niveau': niveau,
        'competences': competences,
        'inventaire': inventaire,
        'date_connexion': date_connexion
    }
    collection.insert_one(joueur)

def getJoueur(player_id):
    db = get_database()
    collection = db['Joueurs']
    return collection.find_one({'player_id': player_id})

def updateJoueur(_id, pseudo, classe, niveau, competences, inventaire, date_connexion):
    db = get_database()
    collection = db['Joueurs']
    collection.update_one({'_id': _id}, {'$set': {'pseudo': pseudo, 'classe': classe, 'niveau': niveau, 'competences': competences, 'inventaire': inventaire, 'date_connexion': date_connexion}})

def deleteJoueur(_id):
    db = get_database()
    collection = db['Joueurs']
    collection.delete_one({'_id': _id})

def addNiveau(_id, niveau):
    db = get_database()
    collection = db['Joueurs']
    collection.update_one({'_id': _id}, {'$set': {'niveau': niveau}})

def addCompetence(_id, competence):
    db = get_database()
    collection = db['Joueurs']
    joueur = getJoueur(_id)
    competences = joueur['competences']
    competences.append(competence)
    collection.update_one({'_id': _id}, {'$set': {'competences': competences}})

def addInventaire(_id, item):
    db = get_database()
    collection = db['Joueurs']
    joueur = getJoueur(_id)
    inventaire = joueur['inventaire']
    inventaire.append(item)
    collection.update_one({'_id': _id}, {'$set': {'inventaire': inventaire}})
    
def removeInventaire(_id, item):
    db = get_database()
    collection = db['Joueurs']
    joueur = getJoueur(_id)
    inventaire = joueur['inventaire']
    inventaire.remove(item)
    collection.update_one({'_id': _id}, {'$set': {'inventaire': inventaire}})



if __name__ == "__main__":
    main()