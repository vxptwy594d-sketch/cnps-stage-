


class DeclarationCNPS:
    def __init__(self):
        self.employees = []
    
    # Module 1 : Lecture des données
    def lire_donnees(self):
        """
        Lit les données des employés nécessaires à la déclaration CNPS
        Retourne une liste de dictionnaires avec les informations des employés
        """
        donnees = [
            {
                "numero": "0000000001",
                "nom": "Dupont",
                "prenom": "Jean",
                "salaire": "0001500.00",
                "date": "2026-10-27"
            },
            {
                "numero": "0000000002",
                "nom": "Martin",
                "prenom": "Marie",
                "salaire": "0001600.00",
                "date": "2026-10-27"
            }
        ]
        
        # Validation des données
        for emp in donnees:
            if not emp.get("numero"):
                raise ValueError("Numéro CNPS manquant")
            if emp.get("salaire", 0) <= 0:
                raise ValueError("Salaire invalide")
        
        self.employees = donnees
        return donnees
    
    # Module 2 : Génération du fichier de déclaration
    def generer_fichier(self, chemin_fichier="declaration_cnps.txt"):
        """
        Génère le fichier texte de déclaration mensuelle CNPS
        
        :param chemin_fichier: chemin du fichier à créer
        """
        if not self.employees:
            raise ValueError("Aucune donnée d'employé. Appelez d'abord lire_donnees()")
        
        try:
            with open(chemin_fichier, "w", encoding="utf-8") as f:
                # En-tête du fichier
                f.write("DIPE001          CNPS_DECLARATION\n")
                
                # Données des employés
                for emp in self.employees:
                    ligne = (
                        f"{emp['numero']}"
                        f"{emp['nom']:<20}"
                        f"{emp['prenom']:<20}"
                        f"{emp['salaire']}{emp['date']}\n"
                    )
                    f.write(ligne)
                
                # Fin de fichier
                f.write("FIN_DECLARATION\n")
            
            print(f"✅ Fichier créé avec succès : {chemin_fichier}")
            return True
        except IOError as e:
            raise IOError(f"Erreur lors de la création du fichier : {str(e)}")