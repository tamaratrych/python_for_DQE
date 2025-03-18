from datetime import datetime, date

file_for_publications = "../publication.txt"

class Publication:
    def __init__(self, pulication_text):
        self.pulication_text = pulication_text
        self.publication_date = datetime.now()
        self.title = ''
        self.spesial_info = ''

    def publish(self):
        try:
            with open(file_for_publications, "a", encoding="utf-8") as f:
                f.write(self.title + '\n')
                f.write(self.pulication_text + '\n')
                f.write(self.spesial_info + '\n\n')
        except Exception as e:
            print(f"An error occurred: {e}")

    @classmethod
    def validate_date(cls, expiration_date):
        try:
            if expiration_date < date.today():
                raise ValueError("The date should be set in the future.")
                return expiration_date
            else:
                return None
        except ValueError as e:
            raise ValueError(f"Invalid date: {e}")
