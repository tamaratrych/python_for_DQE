import sys
from Modules import DB_Client
from Modules import Distance

class Runner:
    def __init__(self, txt=None):
        self.run()

    def save_in_db(self, distance):
        db = DB_Client.DBConnection()
        db.insert(distance.city_from, distance.city_to, distance.latitude_from, distance.longitude_from, distance.latitude_to, distance.longitude_to)
        db.connection.close()

    def run(self):
        print('Distance between two cities')
        city_from = input('Type a name of the first city\n').strip().lower()
        latitude_from = ''
        longitude_from = ''
        connection = DB_Client.DBConnection()
        data_city_from = connection.select(city_from)
        if data_city_from:
            latitude_from = data_city_from[1]
            longitude_from = data_city_from[2]
        else:
            while True:
                latitude_from = input(f'Type latitude of {city_from} and press Enter\n')
                try:
                    latitude_from = float(latitude_from)
                    if latitude_from >= -90 and latitude_from <= 90:
                        break
                    else:
                        print("Latitude must be between -90 and 90. Try again.")
                except:
                    print("You entered a wrong latitude. Type only numbers between -90 and 90.")
            while True:
                longitude_from = input(f'Type longitude of {city_from} and press Enter\n')
                try:
                    longitude_from = float(longitude_from)
                    if longitude_from >= -180 and longitude_from <= 180:
                        connection.insert(city_from, latitude_from, longitude_from)
                        break
                    else:
                        print("Longitude must be between -180 and 180. Try again.")
                except:
                    print("You entered a wrong longitude. Type only numbers.")

        city_to = input('Type a name of the second city\n').strip().lower()
        latitude_to = ''
        longitude_to = ''
        data_city_to = connection.select(city_to)
        if data_city_to:
            latitude_to = data_city_to[1]
            longitude_to = data_city_to[2]
        else:
            while True:
                latitude_to = input(f'Type latitude of {city_to} and press Enter\n')
                try:
                    latitude_to = float(latitude_to)
                    if latitude_to >= -90 and latitude_to <= 90:
                        break
                    else:
                        print("Latitude must be between -90 and 90. Try again.")
                except:
                    print("You entered a wrong latitude. Type only numbers.")
            while True:
                longitude_to = input(f'Type longitude of {city_to} and press Enter\n')
                try:
                    longitude_to = float(longitude_to)
                    if longitude_to >= -180 and longitude_to <= 180:
                        connection.insert(city_to, latitude_to, longitude_to)
                        break
                    else:
                        print("Longitude must be between -180 and 180. Try again.")
                except:
                    print("You entered a wrong longitude. Type only numbers.")

        distance = Distance.Distance(city_from, city_to, latitude_from, longitude_from, latitude_to, longitude_to).calculate_distance()
        distance = round(distance, 2)
        city_from = city_from.capitalize()
        city_to = city_to.capitalize()

        print(f'Distance between {city_from} and {city_to} is {distance}km.')



if __name__ == "__main__":
    Runner()