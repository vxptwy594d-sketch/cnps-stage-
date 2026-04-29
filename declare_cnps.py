from connexion_cnps import ConnexionODBC

# Créer et connecter
db = ConnexionODBC(
    server="MON_SERVEUR",
    database="PAIE_CNPS",
    username="mon_utilisateur",
    password="mon_mot_de_passe"
)

db.connecter()
cursor = db.get_cursor()

# Votre requête
cursor.execute("SELECT * FROM employes WHERE actif = 1")

# Parcourir les résultats
for row in cursor.fetchall():
    print(row)

db.deconnecter()