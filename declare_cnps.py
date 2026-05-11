from declaration_cnps import DeclarationCNPS   # ← "declaration_cnps" pas "connexion_cnps"

declaration_cnps = DeclarationCNPS(
    server   = "MON_SERVEUR",
    database = "PAIE_CNPS",
    username = "mon_utilisateur",
    password = "mon_mot_de_passe"
)

declaration_cnps.connecter()