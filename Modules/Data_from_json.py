import os
import json
from Modules.Data_from_file import DataFromFile
from Modules.Basic_class_Publication import Publication
import Modules.Data_from_consol

DEFAULT_JSON_FILE = 'my_json_file.json'
file_for_wrong_json_data = 'wrong_json_data.json'

json_template = {
    "title": "",
    "pulication_text": "",
    "city": "",
    "expiration_date": "01.01.0001",
    "square": 0,
    "address": "",
    "price": 0}

class DataFromJsonFile(DataFromFile):
    def read_json(self):
        try:
            with open(self.txt, "r", encoding="utf-8") as f:
                txt_from_file = json.load(f)
     #           print(txt_from_file)
            return txt_from_file
        except FileNotFoundError:
            print(f"Error: File '{self.txt}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def __init__(self, txt=None):
        if txt is None:
            self.txt = os.path.join(os.path.dirname(__file__), DEFAULT_JSON_FILE) # File by default
        else:
            self.txt = txt
        self.publications = self.read_json()
        self.wrong_data = []

    def save_wrong_data_in_file(self):
        try:
            json.dump(self.wrong_data, open(file_for_wrong_json_data, "a", encoding="utf-8"))

        except Exception as e:
            print(f"An error occurred: {e}")
            print(f"Wrong data can't be saved in {file_for_wrong_json_data}")


if __name__ == "__main__":
    pass
