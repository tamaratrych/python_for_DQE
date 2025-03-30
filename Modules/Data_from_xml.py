import os
import xml.etree.ElementTree as ET
from Modules.Data_from_file import DataFromFile
from Modules.Basic_class_Publication import Publication
import Modules.Data_from_consol

DEFAULT_XML_FILE = 'my_xml_file.xml'
file_for_wrong_xml_data = 'wrong_xml_data.xml'

class DataFromXmlFile(DataFromFile):
    def read_xml(self):
        try:
            tree = ET.parse(self.txt)
            root = tree.getroot()
            return root
        except FileNotFoundError:
            print(f"Error: File '{self.txt}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def check_existing_file(self):
        if not os.path.exists(file_for_wrong_xml_data):
            root = ET.Element("wrong_publications")
            tree = ET.ElementTree(root)
            tree.write(file_for_wrong_xml_data, encoding="utf-8", xml_declaration=True)

    def __init__(self, txt=None):
        if txt is None:
            self.txt = os.path.join(os.path.dirname(__file__), DEFAULT_XML_FILE) # File by default
        else:
            self.txt = txt
        self.publications = self.read_xml()
        self.wrong_data = []
        self.title = ''
        self.pulication_text = ''
        self.city = ''
        self.expiration_date = ''
        self.square = ''
        self.address = ''
        self.price = ''
        self.check_existing_file()

    def parse_publication(self, any_publication):
        self.title = any_publication.find("title").text if any_publication.find("title") is not None and any_publication.find("title").text is not None else ''
        self.pulication_text = any_publication.find("pulication_text").text if any_publication.find("pulication_text") is not None and any_publication.find("pulication_text").text is not None else ''
        self.city = any_publication.find("city").text if any_publication.find("city") is not None and any_publication.find("city").text is not None else ''
        self.expiration_date = any_publication.find("expiration_date").text if any_publication.find("expiration_date") is not None and any_publication.find("expiration_date").text is not None else ''
        self.square = any_publication.find("square").text if any_publication.find("square") is not None and any_publication.find("square").text is not None else ''
        self.address = any_publication.find("address").text if any_publication.find("address") is not None and any_publication.find("address").text is not None else ''
        self.price = any_publication.find("price").text if any_publication.find("price") is not None and any_publication.find("price").text is not None else ''


if __name__ == "__main__":
    pass
