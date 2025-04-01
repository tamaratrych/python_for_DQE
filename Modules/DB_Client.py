import pyodbc

bd = 'publication_sqlite.db'
schemas = {
    "news": "title TEXT, publication_text TEXT, city TEXT, publication_date TEXT",
    "ads": "title TEXT, publication_text TEXT, expiration_date TEXT",
    "rent": "title TEXT, address TEXT, square INTEGER, price REAL"
}

columns = {
    "news": "title, publication_text, city, publication_date",
    "ads": "title, publication_text, expiration_date",
    "rent": "title, address, square, price"
}

class DBConnection:
    def __init__(self):
        self.connection = pyodbc.connect(f"Driver=SQLite3 ODBC Driver;Database={bd};String Types=Unicode")

    def check_table_existence(self, table_name):
        with self.connection.cursor() as cursor:
            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
            result = cursor.fetchone()
            return result is not None

    def create_table(self, table_name):
        if not self.check_table_existence(table_name):
            with self.connection.cursor() as cursor:
                cursor.execute(f"CREATE TABLE {table_name} ({schemas[table_name]});")

    def select(self, table_name, condition):
        with self.connection.cursor() as cursor:
            cursor.execute(f'SELECT * FROM {table_name} WHERE {condition}')
            result = cursor.fetchone()
            return result is None

    def insert(self, table_name, condition, values):
        if self.select(table_name, condition):
            with self.connection.cursor() as cursor:
                cursor.execute(f'INSERT INTO {table_name} ({columns[table_name]}) VALUES ({values})')
                self.connection.commit()