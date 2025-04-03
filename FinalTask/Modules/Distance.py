from geopy.distance import geodesic


class Distance:
    def __init__(self, city_from, city_to, latitude_from, longitude_from, latitude_to, longitude_to):
        self.city_from = city_from
        self.city_to = city_to
        self.point_from = (latitude_from, longitude_from)
        self.point_to = (latitude_to, longitude_to)

    def calculate_distance(self):
        distance = geodesic(self.point_from, self.point_to).kilometers
        return distance


if __name__ == "__main__":
    pass

