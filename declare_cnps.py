from connexion_cnps import DeclarationCNPS

# Créer et connecter
db = DeclarationCNPS(
    server="MON_SERVEUR",
    database="PAIE_CNPS",
    username="mon_utilisateur",
    password="mon_mot_de_passe"
)


