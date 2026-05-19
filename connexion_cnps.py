
import pyodbc
from typing import Any, Optional


def connect_db(
    server: str,
    database: str,
    username: str,
    password: str,
    driver: str = "{ODBC Driver 17 for SQL Server}",
) -> pyodbc.Connection:
    
    connection_string = (
        f"DRIVER={driver};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
    )
    return pyodbc.connect(connection_string)


class DatabaseManager:
    def __init__(
        self,
        server: str,
        database: str,
        username: str,
        password: str,
        
    ):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.driver = driver
        self.conn: Optional[pyodbc.Connection] = None
        self.cursor: Optional[pyodbc.Cursor] = None

    def connect(self) -> pyodbc.Connection:
        """Ouvre la connexion et crée un curseur."""
        if self.conn is None:
            self.conn = connect_db(
                server=self.server,
                database=self.database,
                username=self.username,
                password=self.password,
                driver=self.driver,
            )
            self.cursor = self.conn.cursor()
        return self.conn

    def execute_query(self, query: str, params: Optional[tuple] = None) -> Optional[Any]:
        """Exécute une requête SQL et retourne les résultats."""
        self.connect()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)

        try:
            return self.cursor.fetchall()
        except pyodbc.ProgrammingError:
            return None

    def close(self) -> None:
        """Ferme le curseur et la connexion."""
        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None
        if self.conn is not None:
            self.conn.close()
            self.conn = None


if __name__ == "__main__":
    print("Utilisez connect_db() ou DatabaseManager pour la connexion à la base de données.") 