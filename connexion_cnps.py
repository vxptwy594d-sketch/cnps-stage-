


class DeclarationCNPS:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
    
    def connecter(self):
        ...
    

    def lecture_des_donnees(self):
        ...
    
    def creation_du_fichier_de_declaration(self):
        ...

declaration_cnps.lecture_des_donnees()

# declaration_cnps.creation_du_fichier_de_declaration()
class DeclarationsCNPS:

    # Module 1 : lecture simple
    def lire_donnees(self):
        return [
            {"matricule": "EMP001", "brut": 450000},
            {"matricule": "EMP002", "brut": 300000}
        ]


    # Module 2 : génération du fichier
    def generer_fichier(self, chemin):
        donnees = self.lire_donnees()

        with open(chemin, "w") as f:
            for d in donnees:
                ligne = d["matricule"] + " " + str(d["brut"])
                f.write(ligne + "\n")


# utilisation
cnps = DeclarationsCNPS()
cnps.generer_fichier("fichier.txt")
print("Fichier créé")
