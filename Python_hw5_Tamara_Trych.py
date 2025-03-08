"""
Create a tool, which will do user generated news feed:
1.User select what data type he wants to add
2.Provide record type required data
3.Record is published on text file in special format



You need to implement:
1.News – text and city as input. Date is calculated during publishing.
2.Privat ad – text and expiration date as input. Day left is calculated during publishing.
3.Your unique one with unique publish rules.



Each new record should be added to the end of file. Commit file in git for review.
"""
from datetime import datetime, date
from abc import ABC, abstractmethod
import pandas as pd

class Publication:
    def __init__(self, pulication_text, publication_date):
        self.pulication_text = pulication_text
        self.publication_date = publication_date

    @abstractmethod
    def publish(self):
        pass


class News(Publication):
    def __init__(self, pulication_text,  publication_city, publication_date=datetime.now()):
        Publication.__init__(self, pulication_text, publication_date)
        self.city = publication_city
        self.publication_date_formated = self.publication_date.strftime("%m/%d/%Y %H:%M")

    def publish(self):
        with open("publication.txt", "a") as f:
            f.write("News -------------------------\n")
            f.write(self.pulication_text + '\n')
            f.write(f"{self.city},  {self.publication_date_formated}\n\n")


class Ad(Publication):
    def __init__(self, pulication_text, expiration_date, publication_date=datetime.now()):
        Publication.__init__(self, pulication_text, publication_date)
        self.expiration_date = expiration_date
        self.expiration_date_formated = self.expiration_date.strftime("%m/%d/%Y")
        self.days_left = self.expiration_date - self.publication_date.date()


    def publish(self):
        with open("publication.txt", "a") as f:
            f.write("Private Ad -------------------\n")
            f.write(self.pulication_text + '\n')
            f.write(f"Actual until {self.expiration_date_formated}, {pd.Timedelta(self.days_left).days} days left\n\n")


class RentOfDay(Publication):
    def __init__(self, address, price, square):
        self.pulication_text = f"Rent the flat of {square} m2 in {address} for {price} USD"
        self.rent_rate = 'best price' if int(price) < 500 else 'best condition'

    def publish(self):
        with open("publication.txt", "a") as f:
            f.write("Rent of the day --------------\n")
            f.write(self.pulication_text + '\n')
            f.write(self.rent_rate + '\n\n')


class Writer:
    counter = 5
    next_publication = ""
    while counter != "0":
        counter = input('Choose a type of publication:\n 1. To choose news type "1" and press Enter\n 2. To choose advertisement type "2" and press Enter\n 3. To choose RentOfDay type "3" and press Enter\n type another symbol and press Enter to Exit\n')
        if counter not in ("1", "2", "3"):
            print("You decide to finish publishing")
            break
        elif counter == "1":
            text = input('Type a text of your news\n')
            city = input('Type a text of a city\n')
            next_publication = News(text, city)
        elif counter == "2":
            text = input('Type a text of your advertisement\n')
            expiration_date = ""
            while True:
                day = input('Type expiration date of your advertisement. At first, day of the month (type a figure from 1 to 31)\n')
                month = input('Second, the month (type a figure from 1 to 12)\n')
                year = input('Finally, year (type four figures)\n')
                try:
                    expiration_date = date(int(year), int(month), int(day))
                    if expiration_date < date.today():
                        print("The date should be set in the future. Try again.")
                    else:
                        print(f"Expiration date is set to: {expiration_date}")
                        break
                except:
                    print("You enter wrong date. Try again.")
            next_publication = Ad(text, expiration_date)
        elif counter == "3":
            address = input('Type address of a flat for rent:\n')
            while True:
                price = input('Type price (number) per month in dollars of a flat for rent:\n')
                try:
                    int(price)
                    break
                except:
                    print("You enter wrong price. Type only number")
            while True:
                square = input('Type square (number) of a flat for rent:\n')
                try:
                    int(square)
                    break
                except:
                    print("You enter wrong square. Type only number")
            next_publication = RentOfDay(address, price, square)
        else:
            print("Please, make your choice")
        next_publication.publish()


if __name__ == "__main__":
    Writer()
