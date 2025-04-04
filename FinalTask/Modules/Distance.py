import math

EarthRadius = 6371.0


class Distance:
    def __init__(self, city_from, city_to, latitude_from, longitude_from, latitude_to, longitude_to):
        self.city_from = city_from
        self.city_to = city_to
        self.latitude_from = math.radians(latitude_from)
        self.longitude_from = math.radians(longitude_from)
        self.latitude_to = math.radians(latitude_to)
        self.longitude_to = math.radians(longitude_to)

    def calculate_distance(self):
        dlat = self.latitude_to - self.latitude_from
        dlon = self.longitude_to - self.longitude_from

        a = math.sin(dlat / 2) ** 2 + math.cos(self.latitude_to) * math.cos(self.latitude_from) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = EarthRadius * c

        return distance


if __name__ == "__main__":
    pass

