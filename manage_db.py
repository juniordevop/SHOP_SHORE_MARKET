# FICHIERS DE FONCTIONS

# se connecter à la base de donnée mysql
import mysql.connector as mc

# dictionnaire de paramètres d'accès
# obligation d'utiliser des simples cotes
config = {
    'host': 'localhost',
    'user':'root',
    'password': 'Siti.Bex@1ntelci@',
    "database": "projet_boutique"
}

# utiliser les parametres 
# se connecter et retourner la version de la bd

# la fonction récupère les param
def getdbinfo(config):
    # req sql
    req = "SELECT version()"
    # connection et exécution de la req
    # utiliser access_db pour démarrer la connection à la BD
    with mc.connect(**config) as access_db:
        with access_db.cursor() as curs:
            # utiliser le curseur pour exécuter la requette
            curs.execute(req)
            resultats = curs.fetchone() # fetchone pour retourner 1 seule ligne sinon fetchall
            return{'resultats' : resultats[0]} # retourner le résultat en json avec {clé : valeur}
                                                # [0] pour ne pas afficher le résultat entre crochets
        return{'resultats' : ""} # faire un second return avec valeur vide si le premier n'a pas marché

# étape 1 créer la fonction qui retourne tous les clients
def rqclientsbg (config):
    req = "SELECT num_compte, Type_compte, prenom, nom, mdp, solde \
        FROM bank_group"
    # connection et exécution de la req
    # utiliser access_db pour démarrer la connection à la BD
    with mc.connect(**config) as access_db:
        with access_db.cursor() as curs:
            # utiliser le curseur pour exécuter la requette
            curs.execute(req)
            resultats = curs.fetchall() # fetchone pour retourner 1 seule ligne sinon fetchall
            return{'resultats' : resultats} # retourner le résultat en json avec {clé : valeur}
                                                # [0] pour ne pas afficher le résultat entre crochets
        return{'resultats' : ""} # faire un second return avec valeur vide si le premier n'a pas marché   
    
# étape 1 créer la fonction qui retrouve le client par son nom
def rqtrouveidclient (config, idclient):
    req = "SELECT num_compte, Type_compte, prenom, nom, mdp, solde \
        FROM bank_group \
        WHERE lower(num_compte) like %s"
    params = (idclient, )
    # connection et exécution de la req
    # utiliser access_db pour démarrer la connection à la BD
    with mc.connect(**config) as access_db:
        with access_db.cursor() as curs:
            # utiliser le curseur pour exécuter la requette
            curs.execute(req,params)
            resultats = curs.fetchall() # fetchone pour retourner 1 seule ligne sinon fetchall
            return{'resultats' : resultats} # retourner le résultat en json avec {clé : valeur}
                                                # [0] pour ne pas afficher le résultat entre crochets
        return{'resultats' : ""} # faire un second return avec valeur vide si le premier n'a pas marché  

# étape 1 créer la fonction qui retourne tous les clients
def rqproduitscm (config):
    req = "SELECT Code_p, Type, Marque, prix, stock \
        FROM chic_mode"
    # connection et exécution de la req
    # utiliser access_db pour démarrer la connection à la BD
    with mc.connect(**config) as access_db:
        with access_db.cursor() as curs:
            # utiliser le curseur pour exécuter la requette
            curs.execute(req)
            resultats = curs.fetchall() # fetchone pour retourner 1 seule ligne sinon fetchall
            return{'resultats' : resultats} # retourner le résultat en json avec {clé : valeur}
                                                # [0] pour ne pas afficher le résultat entre crochets
        return{'resultats' : ""} # faire un second return avec valeur vide si le premier n'a pas marché   
    
# étape 1 créer la fonction qui retrouve le client par son nom
def rqtrouveidproduitcm (config, idproduitcm):
    req = "SELECT Code_p, Type, Marque, prix, stock \
        FROM chic_mode \
        WHERE Code_p like %s"
    params = (idproduitcm, )
    # connection et exécution de la req
    # utiliser access_db pour démarrer la connection à la BD
    with mc.connect(**config) as access_db:
        with access_db.cursor() as curs:
            # utiliser le curseur pour exécuter la requette
            curs.execute(req,params)
            resultats = curs.fetchall() # fetchone pour retourner 1 seule ligne sinon fetchall
            return{'resultats' : resultats} # retourner le résultat en json avec {clé : valeur}
                                                # [0] pour ne pas afficher le résultat entre crochets
        return{'resultats' : ""} # faire un second return avec valeur vide si le premier n'a pas marché 


# étape 1 créer la fonction qui ajoute un nouveau client
def rqajoutclientbg (config, data): # data = {"nom":"NDIAYE", "prenom":"alou", "num_compte" :26, "Type_compte":"particulier","solde" : 2000000,"mdp":1818}
    req = "INSERT INTO bank_group(num_compte, Type_compte, prenom, nom, mdp, solde) \
        VALUES (%s,%s,%s,%s,%s,%s)"
    params = [
        (data["num_compte"],data["Type_compte"],data["prenom"],data["nom"],data["mdp"],data["solde"])
    ]
    # connection et exécution de la req
    # utiliser access_db pour démarrer la connection à la BD
    with mc.connect(**config) as access_db:
        with access_db.cursor() as curs:
            # utiliser le curseur pour exécuter la requette
            curs.executemany(req,params) # executemany pour plusieurs lignes à éxécuter
            access_db.commit() # pour valider les transactions
            return{'nb_ligne' : curs.rowcount} # retourner le résultat en json avec {clé : valeur}
                                                # [0] pour ne pas afficher le résultat entre crochets
        return{'nb_ligne' : 0} # faire un second return avec valeur vide si le premier n'a pas marché 
    
# étape 1 créer la fonction qui ajoute un nouveau client
def rqajoutproduitcm (config, data): # data = {"nom":"NDIAYE", "prenom":"alou", "num_compte" :26, "Type_compte":"particulier","solde" : 2000000,"mdp":1818}
    req = "INSERT INTO chic_mode(Code_p, Type, Marque, prix, stock) \
        VALUES (%s,%s,%s,%s,%s)"
    params = [
        (data["Code_p"],data["Type"],data["Marque"],data["prix"],data["stock"])
    ]
    # connection et exécution de la req
    # utiliser access_db pour démarrer la connection à la BD
    with mc.connect(**config) as access_db:
        with access_db.cursor() as curs:
            # utiliser le curseur pour exécuter la requette
            curs.executemany(req,params) # executemany pour plusieurs lignes à éxécuter
            access_db.commit() # pour valider les transactions
            return{'nb_ligne' : curs.rowcount} # retourner le résultat en json avec {clé : valeur}
                                                # [0] pour ne pas afficher le résultat entre crochets
        return{'nb_ligne' : 0} # faire un second return avec valeur vide si le premier n'a pas marché 

"""----exemple UPDATE
	UPDATE projet_boutique.bank_group
	SET num_compte = %s, Type_compte = %s, prenom = %s, nom = %s, mdp = %s, solde = %s
	WHERE num_compte = %s;"""
# UPDATE projet_boutique.bank_group
# SET num_compte = 1442, Type_compte = "particulier", prenom = "Maria", nom = "NDIAYE" , mdp = 607, solde = 50
# WHERE num_compte = 1442;

# étape 1 créer la fonction qui ajoute un nouveau client
def rqupdateclientbg (config, data): # data = {"nom":"NDIAYE", "prenom":"alou", "num_compte" :26, "Type_compte":"particulier","solde" : 2000000,"mdp":1818}
    req = "UPDATE projet_boutique.bank_group \
        SET num_compte = %s, Type_compte = %s, prenom = %s, nom = %s, mdp = %s, solde = %s \
        WHERE num_compte = %s"
    params = [
        (data["num_compte"],data["Type_compte"],data["prenom"],data["nom"],data["mdp"],data["solde"],data["num_compte"])
    ]
    # connection et exécution de la req
    # utiliser access_db pour démarrer la connection à la BD
    with mc.connect(**config) as access_db:
        with access_db.cursor() as curs:
            # utiliser le curseur pour exécuter la requette
            curs.executemany(req,params) # executemany pour plusieurs lignes à éxécuter
            access_db.commit() # pour valider les transactions
            return{'nb_ligne' : curs.rowcount} # retourner le résultat en json avec {clé : valeur}
                                                # [0] pour ne pas afficher le résultat entre crochets
        return{'nb_ligne' : 0} # faire un second return avec valeur vide si le premier n'a pas marché 
    
"""DELETE FROM TB_COMMERCIAUX;
WHERE id_agent = %s;"""
# DELETE FROM projet_boutique.bank_group
# WHERE num_compte = 1442;

# étape 1 créer la fonction qui supprime client
def rqdeleteidclient (config, idclient):
    req = "DELETE FROM projet_boutique.bank_group \
        WHERE num_compte = %s"
    params = (idclient, )
    # connection et exécution de la req
    # utiliser access_db pour démarrer la connection à la BD
    with mc.connect(**config) as access_db:
        with access_db.cursor() as curs:
            # utiliser le curseur pour exécuter la requette
            curs.execute(req,params)
            access_db.commit()
            

# étape 1 créer la fonction qui ajoute un nouveau client
def rqupdateproduitcm (config, data): # data = {"nom":"NDIAYE", "prenom":"alou", "num_compte" :26, "Type_compte":"particulier","solde" : 2000000,"mdp":1818}
    req = "UPDATE projet_boutique.chic_mode \
        SET Code_p = %s, Type = %s, Marque = %s, prix = %s, stock = %s \
        WHERE Code_p = %s"
    params = [
        (data["Code_p"],data["Type"],data["Marque"],data["prix"],data["stock"],data["Code_p"])
    ]
    # connection et exécution de la req
    # utiliser access_db pour démarrer la connection à la BD
    with mc.connect(**config) as access_db:
        with access_db.cursor() as curs:
            # utiliser le curseur pour exécuter la requette
            curs.executemany(req,params) # executemany pour plusieurs lignes à éxécuter
            access_db.commit() # pour valider les transactions
            return{'nb_ligne' : curs.rowcount} # retourner le résultat en json avec {clé : valeur}
                                                # [0] pour ne pas afficher le résultat entre crochets
        return{'nb_ligne' : 0} # faire un second return avec valeur vide si le premier n'a pas marché 
    
"""DELETE FROM TB_COMMERCIAUX;
WHERE id_agent = %s;"""
# DELETE FROM projet_boutique.bank_group
# WHERE num_compte = 1442;

# étape 1 créer la fonction qui supprime client
def rqdeleteidproduitcm (config, idproduitcm):
    req = "DELETE FROM projet_boutique.chic_mode \
        WHERE Code_p = %s"
    params = (idproduitcm, )
    # connection et exécution de la req
    # utiliser access_db pour démarrer la connection à la BD
    with mc.connect(**config) as access_db:
        with access_db.cursor() as curs:
            # utiliser le curseur pour exécuter la requette
            curs.execute(req,params)
            access_db.commit()
            



