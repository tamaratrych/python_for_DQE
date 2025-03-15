"""
Expand previous Homework 5 with additional class, which allow to provide records by text file:
1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed
4.Apply case normalization functionality from Homework 3/4
"""
import os
import sys
from datetime import datetime, date
from Python_hw4_Tamara_Trych import capitalize_text

DEFAULT_FILE = 'my_file.txt'

class Publication:
    def __init__(self, pulication_text):
        self.pulication_text = pulication_text
        self.publication_date = datetime.now()
        self.title = ''
        self.spesial_info = ''

    def publish(self):
        try:
            with open("publication.txt", "a", encoding="utf-8") as f:
                f.write(self.title + '\n')
                f.write(self.pulication_text + '\n')
                f.write(self.spesial_info + '\n\n')
        except Exception as e:
            print(f"An error occurred: {e}")


class News(Publication):
    def __init__(self, pulication_text,  publication_city):
        super().__init__(pulication_text)
        self.publication_date_formated = self.publication_date.strftime("%m/%d/%Y %H:%M")
        self.title = "News -------------------------"
        self.spesial_info = f"{publication_city},  {self.publication_date_formated}"

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

    @classmethod
    def create_from_input(cls):
        text = input('Type a text of your advertisement\n')
        while True:
            day = input(
                'Type expiration date of your advertisement. At first, day of the month (type a figure from 1 to 31)\n')
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
                print("You entered a wrong date. Try again.")
        return cls(text, expiration_date)


class RentOfDay(Publication):
    def __init__(self, address, price, square):
        pulication_text = f"Rent the flat of {square} m2 in {address} for {price} USD"
        super().__init__(pulication_text)
        self.title = "Rent of the day --------------"
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


class DataFromFile():
    def parse_txt(self):
        txt_for_publish = ''
        try:
            with open(self.txt, "r", encoding="utf-8") as f:
                txt_for_publish = f.read()
            txt_for_publish = capitalize_text(txt_for_publish)
            return txt_for_publish
        except FileNotFoundError:
            print(f"Error: File '{self.txt}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    def __init__(self, txt=None):
        if txt is None:
            self.txt = os.path.join(os.path.dirname(__file__), DEFAULT_FILE) # File by default
        else:
            self.txt = txt
        self.txt_for_publish = self.parse_txt()

    def publish(self):
        if self.txt_for_publish:
            with open("publication.txt", "a", encoding="utf-8") as f:
                f.write(self.txt_for_publish)
        else:
            print("No data to publish.")


class Writer:
    def __init__(self, txt=None):
        if len(sys.argv) > 1:
            self.mode = 'file'
            self.txt = sys.argv[1]
        else:
            self.mode = input('Choose a mode. Press "1" if you want to publish data from the default file or type something other to chosse cinsol mode\n')
            if self.mode == '1':
                self.mode = 'file'
                self.txt = DEFAULT_FILE
            else:
                self.mode = 'console'
                self.txt = None
        self.run()

    def publish_from_console(self):
        while True:
            counter = input(
                'Choose a type of publication:\n 1. To choose news type "1" and press Enter\n 2. To choose advertisement type "2" and press Enter\n 3. To choose RentOfDay type "3" and press Enter\n Type another symbol and press Enter to Exit\n')
            if counter == "1":
                publication = News.create_from_input()
            elif counter == "2":
                publication = Ad.create_from_input()
            elif counter == "3":
                publication = RentOfDay.create_from_input()
            else:
                print("You decide to finish publishing")
                break
            publication.publish()

    def run(self):
        if self.mode == 'file':
            from_file = DataFromFile(self.txt)
            from_file.publish()
        elif self.mode == 'console':
            self.publish_from_console()

if __name__ == "__main__":
    Writer()
