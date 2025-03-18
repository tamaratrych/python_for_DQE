import os
import re
from datetime import datetime, date
from Text_normalizer import capitalize_text
from Basic_class_Publication import Publication
import Data_from_consol

DEFAULT_FILE = '../my_file.txt'
file_for_wrong_data = '../wrong_data.txt'
keywords_for_parse = {
    'News_for_publish:': ('Pulication_text:', 'City_for_publish:'),
    'Private_Ad:': ('Pulication_text:', 'Expiration_date:'),
    'Rent_of_the_day:': ('Pulication_text:', 'Square:', 'Address:', 'Price:')
}

class DataFromFile(Publication):
    def read_txt(self):
        try:
            with open(self.txt, "r", encoding="utf-8") as f:
                txt_from_file = f.read()
            return txt_from_file
        except FileNotFoundError:
            print(f"Error: File '{self.txt}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def parse_txt(self, text, keywords):
        pattern = '|'.join(re.escape(keyword) for keyword in keywords)
        publications = re.split(f"({pattern})", text)
        result = []
        for i in range(1, len(publications), 2):
            key = publications[i].strip()
            value = publications[i + 1].strip() if i + 1 < len(publications) else ""
            result.append({key: value})

        return result

    def __init__(self, txt=None):
        if txt is None:
            self.txt = os.path.join(os.path.dirname(__file__), DEFAULT_FILE) # File by default
        else:
            self.txt = txt
        self.txt_from_file = self.read_txt()
        self.publications = self.parse_txt(self.txt_from_file, keywords_for_parse) if self.txt_from_file != None else None
        self.wrong_data = [self.txt_from_file] if self.publications == [] else []

    def parse_publication(self, any_publication):
        for k, v in any_publication[0]:
            text_with_title = f"Pulication_text: {v}"
            keywards = keywords_for_parse[k]
            values = self.parse_txt(text_with_title, keywards) # We get a list with dicts
            value = {}
            for d in values:
                value.update(d)
            value['Pulication_text:'] = capitalize_text(value['Pulication_text:'])
            result = {k: value}

        return result

    def parse_date(self, any_date_as_string):
        if '.' in any_date_as_string:
            day, month, year = map(int, any_date_as_string.split('.'))
        elif '/' in any_date_as_string:
            day, month, year = map(int, any_date_as_string.split('/'))
        else:
            return None

        return date(year, month, day)

    def delete_file(self):
        try:
            os.remove(self.txt)
            print(f"File '{self.txt}' has been deleted.")
        except FileNotFoundError:
            print(f"File '{self.txt}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_wrong_data_in_file(self):
        add_new_line = [line + "\n" for line in self.wrong_data]
        try:
            with open(file_for_wrong_data, "a", encoding="utf-8") as f:
                f.writelines(add_new_line)
        except Exception as e:
            print(f"An error occurred: {e}")
            print(f"Wrong data can't be saved in {file_for_wrong_data}")


if __name__ == "__main__":
    pass
