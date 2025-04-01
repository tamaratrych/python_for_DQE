from datetime import date
from Modules.Basic_class_Publication import Publication


class News(Publication):
    def __init__(self, pulication_text,  publication_city):
        super().__init__(pulication_text)
        self.publication_date_formated = self.publication_date.strftime("%m/%d/%Y %H:%M")
        self.title = "News -------------------------"
        self.city = publication_city
        self.spesial_info = f"{self.city},  {self.publication_date_formated}"
        self.table_name = 'news'
        self.condition = f"publication_text = '{self.pulication_text}' AND city = '{self.city}'"
        self.values = f"'{self.title}', '{self.pulication_text}', '{self.city}', '{self.publication_date_formated}'"

    @classmethod
    def create_from_input(cls):
        text = input('Type a text of your news\n')
        city = input('Type a text of a city\n')
        return cls(text, city)


class Ad(Publication):
    def __init__(self, pulication_text, expiration_date):
        super().__init__(pulication_text)
        self.expiration_date = expiration_date
        self.expiration_date_formated = self.expiration_date.strftime("%m/%d/%Y")
        self.days_left = self.expiration_date - self.publication_date.date()
        self.title = "Private Ad -------------------"
        self.spesial_info = f"Actual until {self.expiration_date_formated}, { self.days_left.days} days left"
        self.table_name = 'ads'
        self.condition = f"publication_text = '{self.pulication_text}' AND expiration_date = '{self.expiration_date_formated}'"
        self.values = f"'{self.title}', '{self.pulication_text}', '{self.expiration_date_formated}'"

    @classmethod
    def create_from_input(cls):
        text = input('Type a text of your advertisement\n')
        while True:
            try:
                day = input('Type expiration date of your advertisement. At first, day of the month (type a figure from 1 to 31)\n')
                month = input('Second, the month (type a figure from 1 to 12)\n')
                year = input('Finally, year (type four figures)\n')
                expiration_date = date(int(year), int(month), int(day))
                print('expiration_date: ', expiration_date, type(expiration_date))
                expiration_date = Publication.validate_date(expiration_date)
                print(f"Expiration date is set to: {expiration_date}")
                return cls(text, expiration_date)
            except ValueError as e:
                print("You entered a wrong date. Try again.")


class RentOfDay(Publication):
    def __init__(self, address, price, square):
        self.address = address
        self.price = price
        self.square = square
        pulication_text = f"Rent the flat of {self.square} m2 in {self.address} for {self.price} USD"
        super().__init__(pulication_text)
        self.title = "Rent of the day --------------"
        self.table_name = 'rent'
        self.condition = f"address = '{self.address}' AND square = {self.square} AND price  = {self.price}"
        self.values = f"'{self.title}', '{self.address}', {self.square}, {self.price}"

        self.spesial_info = 'best price' if int(price) < 500 else 'best condition'

    @classmethod
    def create_from_input(cls):
        address = input('Type address of a flat for rent:\n')
        while True:
            price = input('Type price (number) per month in dollars of a flat for rent:\n')
            try:
                price = int(price)
                break
            except:
                print("You entered a wrong price. Type only numbers.")
        while True:
            square = input('Type square (number) of a flat for rent:\n')
            try:
                square = int(square)
                break
            except:
                print("You entered a wrong square. Type only numbers.")
        return cls(address, price, square)


if __name__ == "__main__":
    pass
