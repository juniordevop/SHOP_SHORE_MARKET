#V1

import mysql.connector
import pandas as pd

#from sqlalchemy import create_engine
#import pandas as pd

# Créez une connexion SQLAlchemy à votre base de données
#db_url = "mysql+mysqlconnector://username:password@hostname:port/database_name"
#engine = create_engine(db_url)

#conn = mysql.connector.connect(
    #host="localhost",
    #user="root",
    #password="Dama02",
    #database="projet_boutique"#)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Siti.Bex@1ntelci@",
    database="projet_boutique")

#conn = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")

# Variables globales
tb_produit_2 = None
table_choisie1=None
table_choisie1=None
choix_produit=None
choix_quantite=None
produit_selectionne=None
panier_achat = {}
host="localhost"
user="root"
password="Dama02"
database="projet_boutique"
boutique=table_choisie1

CB= "SELECT * FROM bank_group"
tb_banque = pd.read_sql(CB, conn)
valid_sql= "SET AUTOCOMMIT=0" # Pour validation manuelle des requêtes SQL


tb_banque_2=   tb_banque.set_index('num_compte')
#conn.close()
#print(CB)
#conn.close()

#Validez la transaction
conn.commit()


def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dama02",
            database="projet_boutique"
        )
        return conn
    except mysql.connector.Error as err:
        print("Erreur de connexion à la base de données :", err)
        return None

def valider_paiement(conn, nouveau_solde_client, nouveau_solde_boutique, id_payeur):
    conn.close()
    #global conn
    global host, user, password, database, table_choisie1, panier_achat
#import mysql.connector
    conn = mysql.connector.connect(
        host="localhost",
        user=user,
        password=password,
        database=database
    )
    #conn.close()
    connect_to_database()
    try:
        cursor = conn.cursor()
        conn.start_transaction()
        print(panier_achat)
        # Mettez à jour le solde du client
        update_solde_client = "UPDATE bank_group SET solde = %s WHERE num_compte = %s"
        value = (int(nouveau_solde_client), id_payeur)
        cursor.execute(update_solde_client, value)

        # Mettez à jour le solde de la boutique
        update_solde_boutique = "UPDATE bank_group SET solde = %s WHERE nom = %s"
        value = (int(nouveau_solde_boutique), table_choisie1)
        cursor.execute(update_solde_boutique, value)
        
        mettre_a_jour_stock_apres_achat(conn, table_choisie1, choix_produit, choix_quantite)
        # Mettez à jour le stock de la boutique
        #for id_produit, choix_quantite in panier_achat.items():
            #update_stock_boutique = "UPDATE {table_choisie1} SET stock = stock - %s WHERE code_p = %s"
            #value = (int(choix_quantite), id_produit)
            #cursor.execute(update_stock_boutique, value)

        print("Opérations réussies. Transaction validée.")
        print("Vous avez payé votre facture retour au menu principale. ")
        afficher_options()
    except Exception as e:
        conn.rollback()
        print("Erreur : Transaction annulée. Erreur :", str(e))
    finally:
        conn.commit()

        
#def mettre_a_jour_stock_apres_achat(conn, table_choisie1, choix_produit, choix_quantite):
    #try:
        #cursor = conn.cursor()
        # Utilisez des paramètres pour insérer le nom de la table et le code du produit de manière sécurisée dans la requête SQL
        #query = f"UPDATE {table_choisie1} SET stock = stock - %s WHERE Code_p in (%s",)
        #cursor.execute(query, (choix_quantite, choix_produit))
        #conn.commit()
        #cursor.close()
        #print("Stock mis à jour avec succès dans la boutique.")
    #except mysql.connector.Error as err:
        #print("Erreur lors de la mise à jour du stock :", err)


def mettre_a_jour_stock_apres_achat(conn, table_choisie1, choix_produit, choix_quantite):
    global panier_achat
    try:
        cursor = conn.cursor()
        #for code_produit, achat in choix_produit:
            #quantite = achat['choix_quantite']
            #query = f"UPDATE {table_choisie1} SET stock = stock - %s WHERE Code_p = %s"
            #cursor.execute(query, (choix_quantite, code_produit))
            #conn.commit()
        #for id_produit, choix_quantite in panier_achat.items():
        for produit_id, quantite in panier_achat.items():
            print(panier_achat)
            update_stock_boutique = f"UPDATE {table_choisie1} SET stock = stock - %s WHERE code_p = %s"
            value = (int(quantite), produit_id)
            cursor.execute(update_stock_boutique
                           , value)
        conn.commit()
        #cursor.close()
        print("Stock mis à jour avec succès dans la boutique.")
        panier_achat.clear()
    except mysql.connector.Error as err:
        print("Erreur lors de la mise à jour du stock :", err)

        
        
def faire_un_achat(conn):
    global tb_produit_2, panier_achat
    montant_facture = 0

    while True:
        print(tb_produit_2)

        choix_produit_str = input("Saisir le numéro du produit pour l'ajouter à votre panier (1, 2, 3, etc.) ou 0 pour terminer : ")
        choix_produit = int(choix_produit_str)

        if choix_produit == 0:
            break

        if choix_produit_str == '':
            print("Saisie invalide. Veuillez entrer un numéro de produit valide.")
            continue

        if choix_produit not in tb_produit_2.index:
            print("Choix de produit invalide.")
            continue

        produit_selectionne = tb_produit_2.loc[choix_produit]

        choix_quantite = int(input(f"Saisir la quantité souhaitée (stock disponible : {produit_selectionne['stock']} pièces) : "))

        if choix_quantite > produit_selectionne['stock']:
            print("Quantité choisie supérieure au stock disponible.")
            continue

        prix_produit = produit_selectionne['prix'] * choix_quantite

        panier_achat[choix_produit] = choix_quantite
        tb_produit_2.loc[choix_produit, 'stock'] -= choix_quantite
        montant_facture += prix_produit

    print("Contenu complet du panier :")
    for produit_id, quantite in panier_achat.items():
        produit_selectionne = tb_produit_2.loc[produit_id]
        prix_total = produit_selectionne['prix'] * quantite
        print(f"ID Produit : {produit_id}, Nom : {produit_selectionne['Marque']}, Prix unitaire : {produit_selectionne['prix']} FCFA, Quantité : {quantite}, Prix total : {prix_total} FCFA")

    print(f"Le montant de votre facture est de {montant_facture} FCFA.")

    payer = input("Entrez 0 pour passer à la caisse ou 1 pour revenir au menu boutique : ")
    if payer == "0":
        passer_a_la_caisse(conn, panier_achat, montant_facture)
    elif payer == "1":
        return
    else:
        print('Option invalide. Veuillez choisir une option de paiement valide')

#def passer_a_la_caisse(conn, panier_achat, montant_facture):
    #global tb_produit_2, tb_banque_2, tb_produit_2 #id_boutique

    #paiement = 0
    #max_tentatives_mdp = 3
    #while paiement < 1:
        #choix_paiement = int(input(f"Souhaitez-vous régler votre facture de {montant_facture} FCFA ? Choisissez : oui = 1 / non = 0 : "))

        #if choix_paiement == 1:
            #id_payeur = int(input("Veuillez renseigner votre identifiant payeur : "))
            
            # ... (code pour vérifier l'authentification)
            #id_payeur=1

            #ancien_solde_client = tb_banque_2.loc[id_payeur, 'solde']
            #print ("ancien_solde_client")
            #if montant_facture == 0:
                #print("Vous n'avez pas de facture.")
                #print("Souhaitez-vous effectuer un autre achat ?")
                #paiement = 2
            #elif montant_facture > ancien_solde_client:
                #print("Votre solde est insuffisant.")
                #print("Merci de recharger votre compte.")
                #montant_facture = 0
            #else:
                #nouveau_solde_client = ancien_solde_client - montant_facture
                #ancien_solde_boutique = tb_banque_2.loc[id_boutique, 'solde']
                #nouveau_solde_boutique = ancien_solde_boutique + montant_facture
                #print(f"Vous avez payé votre facture qui s'élevait à : {montant_facture} FCFA")
                #print(f"Votre nouveau solde : {nouveau_solde_client} FCFA")
                #print(f"Le nouveau solde de la boutique : {nouveau_solde_boutique} FCFA")
                #paiement = 2
                #panier_achat.clear()
                #montant_facture = 0
                #break
        #elif choix_paiement == 0:
            #paiement = 2
            #print("Merci cher client pour votre passage" + "\n" + "À la prochaine !")
        #else:
            #paiement = 0
            #"print("Vous devez faire un choix valide entre 1 pour valider et 0 pour annuler")

    #print("Paiement effectué avec succès!")
    #valider_paiement(conn, nouveau_solde_client, nouveau_solde_boutique, id_boutique, id_payeur, panier_achat)
def passer_a_la_caisse(conn, panier_achat, montant_facture):
    global tb_produit_2, tb_banque_2, table_choisie1 # Il semble que vous ayez répété la déclaration de ces variables
    id_boutique=table_choisie1
    paiement = 0
    max_tentatives_mdp = 3
    while paiement < 1:
        choix_paiement = int(input(f"Souhaitez-vous régler votre facture de {montant_facture} FCFA ? Choisissez : oui = 1 / non = 0 : "))

        if choix_paiement == 1:
            id_payeur = int(input("Veuillez renseigner votre identifiant payeur : "))
             
            mdp_correct = tb_banque_2.loc[id_payeur, 'mdp']
            tentatives = 0  # Compteur de tentatives

            while tentatives < max_tentatives_mdp:
                mdp = int(input("Veuillez renseigner votre mot de passe : "))

            # Vérifier si le mot de passe est correct
                if mdp == mdp_correct:
                    
            #... (code pour vérifier l'authentification)
                    print("Contenu de tb_banque_2 :")
                    print(tb_banque_2)

                    print("Boutique choisie :")
                    print(table_choisie1)


                    ancien_solde_client = tb_banque_2.loc[id_payeur, 'solde']

                    if montant_facture == 0:
                        print("Vous n'avez pas de facture.")
                        print("Souhaitez-vous effectuer un autre achat ?")
                        paiement = 2
                    elif montant_facture > ancien_solde_client:
                        print("Votre solde est insuffisant.")
                        print("Merci de recharger votre compte.")
                        montant_facture = 0
                    else:
                        nouveau_solde_client = ancien_solde_client - montant_facture
                        #ancien_solde_boutique = tb_banque_2.loc[id_boutique, 'solde']
                        ancien_solde_boutique = tb_banque_2.loc[tb_banque_2['nom'] == table_choisie1, 'solde'].values[0]

                        #ancien_solde_boutique = tb_banque_2.loc[tb_banque_2['nom'] == str(table_choisie1), 'solde'] #.values[0]

                        nouveau_solde_boutique = ancien_solde_boutique + montant_facture
                        print(f"Vous avez payé votre facture qui s'élevait à : {montant_facture} FCFA")
                        print(f"Votre nouveau solde : {nouveau_solde_client} FCFA")
                        print(f"Le nouveau solde de la boutique : {nouveau_solde_boutique} FCFA")
                        valider_paiement(conn, nouveau_solde_client, nouveau_solde_boutique, id_payeur)
                        paiement = 2
                        #panier_achat.clear()
                        montant_facture = 0
                        break
                else:
                    print("Mot de passe incorrect.")
                    tentatives += 1
                    if tentatives < max_tentatives_mdp:
                        print("Il vous reste " + str(max_tentatives_mdp - tentatives) + " tentatives.")

        # Si le nombre maximum de tentatives est atteint, afficher un message et quitter
            if tentatives == max_tentatives_mdp:
                print("Nombre maximum de tentatives atteint. Veuillez contacter votre conseiller client.")
                break       
                        
        elif choix_paiement == 0:
            paiement = 2
            print("Merci cher client pour votre passage" + "\n" + "À la prochaine !")
        else:
            paiement = 0
            print("Vous devez faire un choix valide entre 1 pour valider et 0 pour annuler")

    print("Paiement effectué avec succès!")
    #valider_paiement(conn, nouveau_solde_client, nouveau_solde_boutique, id_boutique, id_payeur, panier_achat)

# Exemple d'utilisation :
    #passer_a_la_caisse(conn, panier_achat, montant_facture)


# Fonction pour se connecter à la base de données
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dama02",
            database="projet_boutique"
        )
        return conn
    except mysql.connector.Error as err:
        print("Erreur de connexion à la base de données :", err)
        return None

# Fonction pour ajouter un nouveau produit dans une table spécifique
def ajouter_produit(conn, Type, Marque, prix, stock):
    try:
        cursor = conn.cursor()
        insert = "INSERT INTO {} (Type, Marque, prix, stock) VALUES (%s, %s, %s, %s)".format(table_choisie) #  f"INSERT INTO %s (Type, Marque, prix, stock) VALUES (%s, %s, %s, %s)"
        values = (Type, Marque, prix, stock)
        cursor.execute(insert, values)
        conn.commit()
        print("Nouveau produit ajouté avec succès !")
    except mysql.connector.Error as err:
        print("Erreur lors de l'ajout du produit :", err)
        
#Fonction pour supprimer un produit
def supprimer_produit(conn, produit_id):
    try:
        cursor = conn.cursor()
        delete = "DELETE FROM {} WHERE Code_p = %s".format(table_choisie) #delete = f"DELETE FROM {table_choisie} WHERE Code_p = %s"
        values = (produit_id,)
        cursor.execute(delete, values)
        conn.commit()
        print("Produit retiré de la boutique avec succès !")
    except mysql.connector.Error as err:
        print("Erreur lors de la suppression du produit :", err)

# Fonction pour mettre à jour le stock d'un produit
def mettre_a_jour_stock(conn, produit_id, nouveau_stock):
    try:
        cursor = conn.cursor()
        update_stock = f"UPDATE {table_choisie}  SET stock = %s WHERE Code_p = %s"
        values = (nouveau_stock, produit_id)
        cursor.execute(update_stock, values)
        conn.commit()
        print("Stock du produit mis à jour avec succès !")
    except mysql.connector.Error as err:
        print("Erreur lors de la mise à jour du stock :", err)

# Fonction pour mettre à jour le prix d'un produit

def mettre_a_jour_prix(conn, produit_id, nouveau_prix):
    #table_update_price= table_choisie
    try:
        cursor = conn.cursor()
        update_price = f"UPDATE {table_choisie} SET prix = %s WHERE Code_p = %s"  #update_price = "UPDATE {table_choisie} SET prix = %s WHERE Code_p = %s" #.format(table_choisie)
        values = (nouveau_prix, produit_id)
        cursor.execute(update_price, values)
        conn.commit()
        print("Prix du produit mis à jour avec succès !")
    except mysql.connector.Error as err:
        print("Erreur lors de la mise à jour du prix :", err)



# Fonction principale pour afficher les options vendeur pour une table spécifique
def afficher_options_vendeur(conn, table):
    while True:
        print("\nOptions Vendeur :")
        print("1. Ajouter un nouveau produit")
        print("2. Mettre à jour le stock d'un produit")
        print("3. Mettre à jour le prix d'un produit")
        print("4. Retirer un produit des rayons")
        print("5. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            Type = input("Type du nouveau produit : ")
            Marque = input("Marque du nouveau produit : ")
            prix = int(input("Prix du nouveau produit : "))
            stock = int(input("Stock du nouveau produit : "))
            ajouter_produit(conn, Type, Marque, prix, stock)
        elif choix == "2":
            produit_id = int(input("ID du produit à mettre à jour : "))
            nouveau_stock = int(input("Nouveau stock : "))
            mettre_a_jour_stock(conn, produit_id, nouveau_stock)
        elif choix == "3":
            produit_id = int(input("ID du produit à mettre à jour : "))
            nouveau_prix = int(input("Nouveau prix : "))
            mettre_a_jour_prix(conn, produit_id, nouveau_prix)
        elif choix == "4":
            produit_id = int(input("ID du produit à supprimer : "))
            supprimer_produit(conn, produit_id)
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

 #fonction pour charger la boutique pour un acheteur    

def charger_boutique(conn, table_choisie1):
    global tb_produit_2
    try:
        cursor = conn.cursor()
        liste_produit = f"SELECT * FROM {table_choisie1}"  # Sélectionner tous les produits de la table articles
        tb_produit = pd.read_sql(liste_produit, conn) # Requête de transaction pour query
        tb_produit_2 = tb_produit.set_index('Code_p')
        print(tb_produit_2)
        faire_un_achat(conn)
    except mysql.connector.Error as err:
        print("Erreur lors de la suppression du produit :", err)

# Fonction principale
def afficher_options():
    print("\033[1mMENU PRINCIPAL :\033[0m")
    #print("MENU PRINICIPALE :")
    print("1. En tant que vendeur")
    print("2. En tant qu'acheteur")
    print("3. Quitter")
    choix = input("Choisissez une option : ")
    return choix

if __name__ == "__main__":
    conn = connect_to_database()
    if conn:
        while True:
            choix = afficher_options()

            if choix == "1":
                print("Bienvenue dans l'interface vendeur.")
                tables_boutiques = ["Chic_Mode", "Diop_Technologie", "Mon_Electromenage"]  
                while True:
                    for i, table in enumerate(tables_boutiques, start=1):
                        print(f"{i}. {table}")
                    choix_table = input("Choisissez une boutique : ")
                    if choix_table.isdigit() and 1 <= int(choix_table) <= len(tables_boutiques):
                        table_choisie = tables_boutiques[int(choix_table) - 1]
                        
                        # Demander le mot de passe
                        mot_de_passe_saisi = int(input("Entrez le mot de passe : "))

                        # Vérification des informations d'authentification dans la table des comptes bancaires
                        cursor = conn.cursor()
                        query = "SELECT mdp FROM bank_group WHERE nom = %s"
                        cursor.execute(query, (table_choisie,))
                        result = cursor.fetchone()

                        if result is not None and mot_de_passe_saisi == result[0]:
                            # Les informations d'authentification sont correctes, permettez l'accès à la table boutique
                            afficher_options_vendeur(conn, table_choisie)
                            break  # Sortir de la boucle après un accès réussi
                        else:
                            # Informations d'authentification incorrectes, refuser l'accès
                            print("Informations d'authentification incorrectes. Accès refusé.")
                    else:
                        print("Boutique invalide. Veuillez réessayer.")

            elif choix == "2":
                print("Bienvenue dans l'interface acheteur.")
                tables_boutiques = ["Chic_Mode", "Diop_Technologie", "Mon_Electromenage"]  
                while True:
                    for i, table in enumerate(tables_boutiques, start=1):
                        print(f"{i}. {table}")
                    choix_table = input("Choisissez une boutique (ou tapez '0' pour quitter) : ")
        
                    if choix_table.isdigit() and 1 <= int(choix_table) <= len(tables_boutiques):
                        table_choisie1 = str(tables_boutiques[int(choix_table) - 1])
                        connect_to_database()
                        charger_boutique(conn, table_choisie1)
                           

                    elif choix_table.lower() == '0':
                        print("0")
                        break
                        afficher_option()
                    else:
                        print("Choix invalide. Veillez choisir une boutique.")

          
           
                        
                
                # Ajoutez ici la logique pour l'interface acheteur
            elif choix == "3":
                print("Au revoir !")
                break
            else:
                #choix = afficher_options()
                print("Option invalide. Veuillez réessayer.")

        #conn.close()
