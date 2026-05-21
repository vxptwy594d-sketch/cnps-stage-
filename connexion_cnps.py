import pyodbc
from typing import Any, Optional


class Database:
    def __init__(
        self,
        server: str,
        database: str,
        username: str,
        password: str,
        driver: str = "{ODBC Driver 17 for SQL Server}",
    ):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.driver = driver
        self.conn: Optional[pyodbc.Connection] = None
        self.cursor: Optional[pyodbc.Cursor] = None

    def connect_db(self) -> pyodbc.Connection:
        connection_string = (
            f"DRIVER={self.driver};"
            f"SERVER={self.server};"
            f"DATABASE={self.database};"
            f"UID={self.username};"
            f"PWD={self.password};"
        )
        return pyodbc.connect(connection_string)

    def connect(self) -> pyodbc.Connection:
        if self.conn is None:
            self.conn = self.connect_db()
            self.cursor = self.conn.cursor()
        return self.conn

    def execute_query(self, query: str, params: Optional[tuple] = None) -> Optional[Any]:
        self.connect()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)

        try:
            return self.cursor.fetchall()
        except:
            return None

    def close(self) -> None:
        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None
        if self.conn is not None:
            self.conn.close()
            self.conn = None


if __name__ == "__main__":
    print("Utilisez connect_db() ou DatabaseManager pour la connexion à la base de données.")