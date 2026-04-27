import sqlite3
from typing import List, Dict, Any, Optional

class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn: Optional[sqlite3.Connection] = None

    def connect(self) -> sqlite3.Connection:
        """
        Établit une connexion à la base de données SQLite et configure
        la lecture des résultats sous forme de dictionnaire.
        """
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
        return self.conn

    def read_monthly_declarations(
        self,
        table_name: str = "declarations_mensuelles",
        columns: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """
        Lit les données des déclarations mensuelles depuis la table indiquée.
        """
        conn = self.connect()
        cursor = conn.cursor()
        cols = ", ".join(columns) if columns else "*"
        query = f"SELECT {cols} FROM {table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]