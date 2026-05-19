
class DeclarationCNPS:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
    
    def connecter(self):
        print(f"Connexion {self.server}/{self.database} avec {self.username}")
    
    def deconnecter(self):
        print(f"Déconnexion {self.server}/{self.database}")