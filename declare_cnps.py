class CNPSGenerator:
    def __init__(self):
        self.connection = None

    def connect_to_db(self, dsn, user, password):
        # Simulation de connexion ODBC (pas de vraie base de données)
        # En réalité, utiliser pyodbc ou similaire
        # self.connection = pyodbc.connect(f'DSN={dsn};UID={user};PWD={password}')
        print("Connexion simulée à la base de données.")
        self.connection = "simulated_connection"

    def generate_declaration_file(self, employees_data, output_file_path):
        """
        Génère le fichier de déclaration mensuelle CNPS (DIPE magnétique).

        :param employees_data: Liste de dictionnaires avec les données des employés
        :param output_file_path: Chemin du fichier de sortie
        """
        with open(output_file_path, 'w', encoding='utf-8') as file:
            # En-tête du fichier (exemple basé sur spécifications supposées)
            header = "DIPE001" + " " * 10 + "CNPS_DECLARATION" + "\n"
            file.write(header)

            for employee in employees_data:
                # Format supposé : ID_EMPLOYE NOM PRENOM SALAIRE DATE
                # Ajuster selon les vraies spécifications CNPS
                line = f"{employee['id']:010d}{employee['nom']:20}{employee['prenom']:20}{employee['salaire']:010.2f}{employee['date']:10}\n"
                file.write(line)

            # Pied de page
            footer = "FIN_DECLARATION" + "\n"
            file.write(footer)

        print(f"Fichier généré : {output_file_path}")

# Exemple d'utilisation
if __name__ == "__main__":
    generator = CNPSGenerator()
    generator.connect_to_db("DSN_EXAMPLE", "user", "password")

    # Données simulées des employés
    employees = [
        {"id": 1, "nom": "Dupont", "prenom": "Jean", "salaire": 1500.00, "date": "2026-10-27"},
        {"id": 2, "nom": "Martin", "prenom": "Marie", "salaire": 1600.00, "date": "2026-10-27"},
    ]


    generator.generate_declaration_file(employees, "declaration_cnps.txt")