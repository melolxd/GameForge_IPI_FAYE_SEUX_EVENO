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
    
    ajouterCompetenceToCompetence("Bouclier Magique", 15)
    ajouterCompetenceToCompetence("Frappe de Foudre", 12)
    ajouterCompetenceToCompetence("Coup Rapide", 5)
    ajouterCompetenceToCompetence("Soin", 8)
    ajouterCompetenceToCompetence("Cri de Guerre", 20)
    ajouterCompetenceToCompetence("Pluie de Flèches", 18)
    ajouterCompetenceToCompetence("Invisibilité", 25)
    ajouterCompetenceToCompetence("Téléportation", 30)
    ajouterCompetenceToCompetence("Rage du Berserker", 40)
    ajouterCompetenceToCompetence("Vague de Feu", 22)
    ajouterCompetenceToCompetence("Mur de Glace", 28)
    ajouterCompetenceToCompetence("Poison Mortel", 12)
    ajouterCompetenceToCompetence("Guérison de Masse", 50)
    ajouterCompetenceToCompetence("Éclair de Givre", 14)
    ajouterCompetenceToCompetence("Explosion Sismique", 45)
    ajouterCompetenceToCompetence("Bouclier Divin", 60)
    ajouterCompetenceToCompetence("Lame Sanguinaire", 20)
    ajouterCompetenceToCompetence("Barrière de Vent", 25)
    ajouterCompetenceToCompetence("Éclair du Phoenix", 55)
    # Insert data into Inventaire
    
    ajouterInventaireToInventaire("Épée du Brave")
    ajouterInventaireToInventaire("Bouclier de Fer")
    ajouterInventaireToInventaire("Potion de Soin")
    ajouterInventaireToInventaire("Potion de Mana")
    ajouterInventaireToInventaire("Arc Long")
    ajouterInventaireToInventaire("Amulette de Force")
    ajouterInventaireToInventaire("Anneau de Sagesse")
    ajouterInventaireToInventaire("Cape d'Invisibilité")
    ajouterInventaireToInventaire("Bottes de Vitesse")
    ajouterInventaireToInventaire("Casque de l'Inébranlable")
    ajouterInventaireToInventaire("Gants d'Assassin")
    ajouterInventaireToInventaire("Hache de Guerre")
    ajouterInventaireToInventaire("Bâton de Mage")
    ajouterInventaireToInventaire("Anneau de Régénération")
    ajouterInventaireToInventaire("Talisman de Protection")
    ajouterInventaireToInventaire("Potion d'Énergie")
    ajouterInventaireToInventaire("Ceinture du Gladiateur")
    ajouterInventaireToInventaire("Potion de Résistance")
    ajouterInventaireToInventaire("Bottes de Lévitation")
    ajouterInventaireToInventaire("Cape de Résistance au Feu")
    ajouterInventaireToInventaire("Épée Enflammée")
    ajouterInventaireToInventaire("Casque d'Immunité")
    ajouterInventaireToInventaire("Gantelets de Force")
    ajouterInventaireToInventaire("Bouclier Mystique")
    ajouterInventaireToInventaire("Potion de Puissance")
    ajouterInventaireToInventaire("Talisman de Vitesse")
    ajouterInventaireToInventaire("Lance de Glace")
    ajouterInventaireToInventaire("Cape de l'Ombre")
    ajouterInventaireToInventaire("Ceinture de Vitalité")
    ajouterInventaireToInventaire("Bouclier Solaire")
    
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

    # Other functions
    ajouterNiveau('IronFist', 3)
    
    ajouterCompetenceToCompetence("Frappe de l'Ours", 10)
    
    ajouterCompetenceToJoueur('IronFist', {'_id': 16})
    
    ajouterInventaireToInventaire("Épée de l'Ours")
    
    ajouterInventaireToJoueur('IronFist', {'_id': 12})
    
    updateDateConnexion('IronFist', '2024-11-05')
    
    supprimerInventaireFromJoueur('StormChaser', {'_id': 9})
    
    deleteJoueur('ThunderKing')
    


def getCompetencesFromCompetences(competences):
    db = get_database()
    collection = db['Compétences']
    return collection.find_one({'_id': competences['_id']})

def getCompetencesFromJoueur(pseudo, competences):
    db = get_database()
    collection = db['Joueurs']
    return collection.find_one({'pseudo': pseudo, 'competences': competences})

def ajouterCompetenceToCompetence(nom, description):
    db = get_database()
    collection = db['Compétences']
    competence = {
        '_id': collection.count_documents({}) + 1,
        'nom': nom,
        'description': description
    }
    collection.insert_one(competence)
    print('compétence ajoutée')
    
def ajouterCompetenceToJoueur(pseudo, competence):
    db = get_database()
    if getJoueurByPseudo(pseudo) is not None:
        if getCompetencesFromCompetences(competence) is not None:
            if getCompetencesFromJoueur(pseudo, competence) is None:
                collection = db['Joueurs']
                joueur = getJoueurByPseudo(pseudo)
                competences = joueur['competences']
                competences.append(competence)
                collection.update_one({'pseudo': pseudo}, {'$set': {'competences': competences}})
                print('compétence ajoutée au joueur')
            else:
                print('Compétence déjà acquise')
        else:
            print('Compétence introuvable')
    else:
        print('Joueur introuvable')



def getItemFromInventaireById(_id):
    db = get_database()
    collection = db['Inventaire']
    return collection.find_one({'_id': _id})

def getItemFromInventaireByNom(nom):
    db = get_database()
    collection = db['Inventaire']
    return collection.find_one({'nom': nom})

def getItemFromJoueur(pseudo, item):
    inventaire = getJoueurByPseudo(pseudo)['inventaire']
    for itemInventaire in inventaire:
        if item['_id'] == itemInventaire['_id']:
            return itemInventaire
    return None

def ajouterInventaireToInventaire(nom):
    if getItemFromInventaireByNom(nom) is None:
        db = get_database()
        collection = db['Inventaire']
        inventaire = {
            '_id': collection.count_documents({}) + 1,
            'nom': nom
        }
        collection.insert_one(inventaire)
        print('item ajouté')
    else:
        print('Item déjà existant')

def ajouterInventaireToJoueur(pseudo, item):
    db = get_database()
    if getJoueurByPseudo(pseudo) is not None:
        if getItemFromInventaireById(item['_id']) is not None:
            if getItemFromJoueur(pseudo, item) is None:
                collection = db['Joueurs']
                joueur = getJoueurByPseudo(pseudo)
                inventaire = joueur['inventaire']
                inventaire.append(item)
                collection.update_one({'pseudo': pseudo}, {'$set': {'inventaire': inventaire}})
                print('item ajouté au joueur')
            else:
                collection = db['Joueurs']
                joueur = getJoueurByPseudo(pseudo)
                inventaire = joueur['inventaire']
                itemInventaire = getItemFromJoueur(pseudo, item)
                itemInventaire['quantite'] += 1
                for i in range(len(inventaire)):
                    if inventaire[i]['_id'] == itemInventaire['_id']:
                        inventaire[i] = itemInventaire
                        break
                collection.update_one({'pseudo': pseudo}, {'$set': {'inventaire': inventaire}})
                print('quantité augmentée')
        else:
            print('Item introuvable')
    else:
        print('Joueur introuvable')

def supprimerInventaireFromJoueur(pseudo, item):
    db = get_database()
    if getJoueurByPseudo(pseudo) is not None:
        if getItemFromInventaireById(item['_id']) is not None:
            if getItemFromJoueur(pseudo, item) is not None:
                collection = db['Joueurs']
                joueur = getJoueurByPseudo(pseudo)
                inventaire = joueur['inventaire']
                itemInventaire = getItemFromJoueur(pseudo, item)
                if itemInventaire['quantite'] > 1:
                    itemInventaire['quantite'] -= 1
                    collection.update_one({'pseudo': pseudo}, {'$set': {'inventaire': itemInventaire}})
                else:
                    inventaire.remove(itemInventaire)
                    collection.update_one({'pseudo': pseudo}, {'$set': {'inventaire': inventaire}})
            else:
                print('Item non possédé')
        else:
            print('Item introuvable')
    else:
        print('Joueur introuvable')

    
def ajouterJoueur(pseudo, classe, niveau, competences, inventaire, date_connexion):
    if getJoueurByPseudo(pseudo) is not None:
        print('Joueur déjà existant')
        return None
    else:
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
    

def getJoueurByPseudo(pseudo):
    db = get_database()
    collection = db['Joueurs']
    return collection.find_one({'pseudo': pseudo})


def updateDateConnexion(pseudo, date_connexion):
    if getJoueurByPseudo(pseudo) is not None:
        db = get_database()
        collection = db['Joueurs']
        collection.update_one({'pseudo': pseudo}, {'$set': {'date_connexion': date_connexion}})
    else:
        print('Joueur introuvable')
    
def deleteJoueur(pseudo):
    if getJoueurByPseudo(pseudo) is None:
        print('Joueur introuvable')
        return None
    else:
        db = get_database()
        collection = db['Joueurs']
        collection.delete_one({'pseudo': pseudo})

def ajouterNiveau(pseudo, niveau):
    db = get_database()
    if getJoueurByPseudo(pseudo) is not None:
        collection = db['Joueurs']
        joueur = getJoueurByPseudo(pseudo)
        collection.update_one({'pseudo': pseudo}, {'$set': {'niveau': joueur['niveau'] + niveau}})
        print('niveau ajouté')
    else:
        print('Joueur introuvable')

        

    
def removeInventaire(pseudo, item):
    db = get_database()
    if getJoueurByPseudo(pseudo) is not None:
        collection = db['Joueurs']
        joueur = getJoueurByPseudo(pseudo)
        inventaire = joueur['inventaire']
        inventaire.remove(item)
        collection.update_one({'pseudo': pseudo}, {'$set': {'inventaire': inventaire}})
    else:
        print('Joueur introuvable')


if __name__ == "__main__":
    main()