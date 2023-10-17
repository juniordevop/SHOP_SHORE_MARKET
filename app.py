# installer flask > pip install flask
# cls pour effacer le terminal / réactiver l'env
# installer un fichier qui va permettre de se connecter à mysql
# > pip install mysql-connector-python

# import de bibs flask
# flask pour l'API
# request pour poser des questions
# jsnon pour récupérer des infos
# jsonify pour retourner des réponse au format json
from flask import Flask, request, json, jsonify


# importer les fonction du fichier libs

from libs import *
from manage_db import *

# variable test
my_sc = "Faites vos achats"
# l'API doit être basée sur une application
# créer l'application rest

app = Flask(__name__)

# utliliser l'application pour créer une route pour le client
# @app pour appelr l'application
@app.route("/api/bonjour")

# la route doit déclencher une fonction qui va réaliser une action
# fonction qui ira chercher la methode bonjour

def bonjour():
    # definir l'action de la fonction
    # activer la fonction direbonjour()
    msg = direbonjour()

    # il faut retourner la réponse au client
    return msg

# route ki permet de dire bonjour avec un prenom
# Qu'avec la méthode GET opur accéder à la route
#> http://192.168.1.107:3003/api/bonjourprenom/?prenom=pierre
#> http://192.168.1.107:3003/api/bonjourprenom/?prenom=pierre&nom=jean
@app.route("/api/bonjourprenom/", methods = ["GET"])
def bonjourprenom():
    # récupérer la donnée prénom de l'URL
    data_prenom = request.args.get("prenom", default="", type=str)
    data_nom = request.args.get("nom", default="", type=str)
    # definir l'action de la fonction
    # activer la fonction direbonjour()
    msg = direbonjour(prenom=data_prenom, nom = data_nom)

    # retourner le résultat au client
    return msg

# appeler la fonction getdbinfo avec l'API
# from manage_db import * / import des fonctions créées dans manage_db.py
# création de la route que l'utilisateur doit utliser
# http://192.168.1.107:3003/api/infodb
@app.route("/api/infodb/", methods = ["GET"])
# mettre la fonction qui doit être appelée
def infodb():
    msg = getdbinfo(config = config) # le premier config est le param de la fonction et le secong est celui des accès de connection
    return jsonify(msg) # pour retourner le résultat au format jsnon au lieu du format text

# appeler la fonction getallclients avec l'API
# from manage_db import * / import des fonctions créées dans manage_db.py
# création de la route que l'utilisateur doit utliser
# http://192.168.1.107:3003/api/getclients
@app.route("/api/cmdclientsbg/", methods = ["GET"])
# mettre la fonction qui doit être appelée
def cmdclientsbg():
    msg = rqclientsbg(config = config) # le premier config est le param de la fonction et le secong est celui des accès de connection
    return jsonify(msg) # pour retourner le résultat au format jsnon au lieu du format text

# appeler la fonction findclients avec l'API
# from manage_db import * / import des fonctions créées dans manage_db.py
# création de la route que l'utilisateur doit utliser
# http://192.168.1.107:3003/api/findbyname?name=Diallo
@app.route("/api/cmdtrouveidclient/", methods = ["GET"])
# mettre la fonction qui doit être appelée
def cmdtrouveidclient():
    idclient = request.args.get("idclient", default=0, type=int)
    msg = rqtrouveidclient(config = config, idclient = idclient) # le premier config est le param de la fonction et le secong est celui des accès de connection
    return jsonify(msg) # pour retourner le résultat au format jsnon au lieu du format text

# appeler la fonction getallclients avec l'API
# from manage_db import * / import des fonctions créées dans manage_db.py
# création de la route que l'utilisateur doit utliser
# http://192.168.1.107:3003/api/getclients
@app.route("/api/cmdproduitscm/", methods = ["GET"])
# mettre la fonction qui doit être appelée
def cmdproduitscm():
    msg = rqproduitscm(config = config) # le premier config est le param de la fonction et le secong est celui des accès de connection
    return jsonify(msg) # pour retourner le résultat au format jsnon au lieu du format text

# appeler la fonction findclients avec l'API
# from manage_db import * / import des fonctions créées dans manage_db.py
# création de la route que l'utilisateur doit utliser
# http://192.168.1.107:3003/api/findbyname?name=Diallo
@app.route("/api/cmdtrouveidproduitcm/", methods = ["GET"])
# mettre la fonction qui doit être appelée
def cmdtrouveidproduitcm():
    idproduitcm = request.args.get("idproduitcm", default=0, type=int)
    msg = rqtrouveidproduitcm(config = config, idproduitcm = idproduitcm) # le premier config est le param de la fonction et le secong est celui des accès de connection
    return jsonify(msg) # pour retourner le résultat au format jsnon au lieu du format text


# appeler la fonction findclients avec l'API
# from manage_db import * / import des fonctions créées dans manage_db.py
# création de la route avec POST que l'utilisateur doit utliser
# parametres (json): num_compte, Type_compte, prenom, nom, mdp, solde
# route: /api/addclient
# http://192.168.1.107:3003/api/addclient
@app.route("/api/cmdajoutclientbg/", methods = ["POST"])
# mettre la fonction qui doit être appelée
def cmdajoutclientbg():
    # récupérer les données envoyées par le client paramètres
    # data = {"nom":"NDIAYE", "prenom":"alou", "num_compte" :26, "Type_compte":"particulier","solde" : 2000000,"mdp":1818}
    infoclient = json.loads(request.data)
    msg = rqajoutclientbg(config = config, data = infoclient) # le premier config est le param de la fonction et le secong est celui des accès de connection
    return jsonify(msg) # pour retourner le résultat au format jsnon au lieu du format text

# appeler la fonction findclients avec l'API
# from manage_db import * / import des fonctions créées dans manage_db.py
# création de la route avec POST que l'utilisateur doit utliser
# parametres (json): num_compte, Type_compte, prenom, nom, mdp, solde
# route: /api/addclient
# http://192.168.1.107:3003/api/addclient
@app.route("/api/cmdajoutproduitcm/", methods = ["POST"])
# mettre la fonction qui doit être appelée
def cmdajoutproduitcm():
    # récupérer les données envoyées par le client paramètres
    # data = {"nom":"NDIAYE", "prenom":"alou", "num_compte" :26, "Type_compte":"particulier","solde" : 2000000,"mdp":1818}
    infoproduit = json.loads(request.data)
    msg = rqajoutproduitcm(config = config, data = infoproduit) # le premier config est le param de la fonction et le secong est celui des accès de connection
    return jsonify(msg) # pour retourner le résultat au format jsnon au lieu du format text

# appeler la fonction rqupdateclientbg avec l'API
# from manage_db import * / import des fonctions créées dans manage_db.py
# création de la route avec POST que l'utilisateur doit utliser
# parametres (json): num_compte, Type_compte, prenom, nom, mdp, solde
# route: /api/addclient
# http://192.168.1.107:3003/api/cmdupdateclientbg
@app.route("/api/cmdupdateclientbg/", methods = ["POST"])
# mettre la fonction qui doit être appelée
def cmdupdateclientbg():
    # récupérer les données envoyées par le client paramètres
    # data = {"nom":"NDIAYE", "prenom":"alou", "num_compte" :26, "Type_compte":"particulier","solde" : 2000000,"mdp":1818}
    infoclient = json.loads(request.data)
    msg = rqupdateclientbg(config = config, data = infoclient) # le premier config est le param de la fonction et le secong est celui des accès de connection
    return jsonify(msg) # pour retourner le résultat au format jsnon au lieu du format text


# appeler la fonction removeclient avec l'API
# from manage_db import * / import des fonctions créées dans manage_db.py
# création de la route que l'utilisateur doit utliser
# http://192.168.1.107:3003/api/cmddeleteidclient?idclient=2525
@app.route("/api/cmddeleteidclient/", methods = ["DELETE"])
# mettre la fonction qui doit être appelée
def cmddeleteidclient():
    idclient = request.args.get("idclient", default=0, type=int)
    msg = rqdeleteidclient(config = config, idclient = idclient) # le premier config est le param de la fonction et le secong est celui des accès de connection
    return jsonify(msg) # pour retourner le résultat au format jsnon au lieu du format text

# appeler la fonction rqupdateclientbg avec l'API
# from manage_db import * / import des fonctions créées dans manage_db.py
# création de la route avec POST que l'utilisateur doit utliser
# parametres (json): num_compte, Type_compte, prenom, nom, mdp, solde
# route: /api/addclient
# http://192.168.1.107:3003/api/cmdupdateclientbg
@app.route("/api/cmdupdateproduitcm/", methods = ["POST"])
# mettre la fonction qui doit être appelée
def cmdupdateproduitcm():
    # récupérer les données envoyées par le client paramètres
    # data = {"nom":"NDIAYE", "prenom":"alou", "num_compte" :26, "Type_compte":"particulier","solde" : 2000000,"mdp":1818}
    infoproduit = json.loads(request.data)
    msg = rqupdateproduitcm(config = config, data = infoproduit) # le premier config est le param de la fonction et le secong est celui des accès de connection
    return jsonify(msg) # pour retourner le résultat au format jsnon au lieu du format text


# appeler la fonction removeclient avec l'API
# from manage_db import * / import des fonctions créées dans manage_db.py
# création de la route que l'utilisateur doit utliser
# http://192.168.1.107:3003/api/cmddeleteidclient?idclient=2525
@app.route("/api/cmddeleteidproduitcm/", methods = ["DELETE"])
# mettre la fonction qui doit être appelée
def cmddeleteidproduitcm():
    idproduitcm = request.args.get("idproduitcm", default=0, type=int)
    msg = rqdeleteidproduitcm(config = config, idproduitcm = idproduitcm) # le premier config est le param de la fonction et le secong est celui des accès de connection
    return jsonify(msg) # pour retourner le résultat au format jsnon au lieu du format text


# lancer l'application
if __name__ == "__main__":
    # de quelle manière
    #app.run(host=ip8fixe ou '0.0.0.0', port=xxx, montrer l'erreur)
    app.run(host='0.0.0.0', port=3003, debug=True)

    # lancer le serveur par le fichier
    #> python .\app.py
    #> py app.py
        # le serveur a démarré sur 2 adresses
        #* Running on http://127.0.0.1:3003
        #* Running on http://192.168.1.107:3003
    # pour accéder à une route
    #> http://192.168.1.107:3003/api/bonjour



