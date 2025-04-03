import pyodbc

bd = 'cities.db'


class DBConnection:
    def __init__(self):
        self.connection = pyodbc.connect(f"Driver=SQLite3 ODBC Driver;Database={bd};String Types=Unicode")
        self.create_table()

    def create_table(self):
        with self.connection.cursor() as cursor:
            cursor.execute('CREATE TABLE IF NOT EXISTS cities (city TEXT NOT NULL, latitude REAL NOT NULL, longitude REAL NOT NULL)')

    def select(self, city_name):
        query = f"SELECT * FROM cities WHERE city  = ?"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (city_name,))
            result = cursor.fetchone()
            return result

    def insert(self, city_name, latitude, longitude):
        query = f"INSERT INTO cities (city, latitude, longitude) VALUES (?, ?, ?)"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (city_name, latitude, longitude,))
            self.connection.commit()

if __name__ == "__main__":
    pass