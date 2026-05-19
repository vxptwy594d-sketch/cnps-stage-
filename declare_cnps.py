from typing import Dict, List


class DeclarationCNPS:
    def __init__(self):
        self.employees: List[Dict[str, str]] = []

    def lire_donnees(self) -> List[Dict[str, str]]:
        """Lit et valide les données des employés nécessaires à la déclaration CNPS."""
        donnees = [
            {
                "numero": "0000000001",
                "nom": "haniel",
                "prenom": "tchapmeni",
                "salaire": "1500.00",
                "date": "2026-10-27",
            },
            {
                "numero": "0000000002",
                "nom": "leonel",
                "prenom": "leo",
                "salaire": "1600.00",
                "date": "2026-10-27",
            },
        ]
        self._valider_donnees(donnees)
        self.employees = donnees
        return donnees

    def _valider_donnees(self, donnees: List[Dict[str, str]]) -> None:
        """Valide les champs obligatoires et le salaire."""
        for emp in donnees:
            if not emp.get("numero"):
                raise ValueError("Numéro CNPS manquant")

            try:
                salaire = float(emp.get("salaire", "0").replace(",", "."))
            except ValueError:
                raise ValueError("Salaire invalide") from None

            if salaire <= 0:
                raise ValueError("Salaire invalide")

            emp["salaire"] = f"{salaire:0>10.2f}"

    def ecrire_declaration(self, chemin_fichier: str) -> None:
        """Écrit le fichier de déclaration CNPS à partir des données chargées."""
        if not self.employees:
            raise ValueError("Aucune donnée d'employé. Appelez d'abord lire_donnees()")

        with open(chemin_fichier, "w", encoding="utf-8") as f:
            f.write("DIPE001          CNPS_DECLARATION\n")
            for emp in self.employees:
                ligne = (
                    f"{emp['numero']}"
                    f"{emp['nom']:<20}"
                    f"{emp['prenom']:<20}"
                    f"{emp['salaire']}"
                    f"{emp['date']}\n"
                )
                f.write(ligne)
            f.write("FIN_DECLARATION\n")


if __name__ == "__main__":
    declaration = DeclarationCNPS()
    declaration.lire_donnees()
    declaration.ecrire_declaration("declaration_cnps.txt")
    print("Fichier de déclaration CNPS créé avec succès.")