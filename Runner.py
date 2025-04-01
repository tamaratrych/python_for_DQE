import sys
import xml.etree.ElementTree as ET
from Modules import Data_from_consol
from Modules import Data_from_file
from Modules import Data_from_json
from Modules import Data_from_xml
from Modules import Statistics
from Modules import Basic_class_Publication
from Modules import DB_Client



class_publication = {
    'News_for_publish:': Data_from_consol.News,
    'Private_Ad:': Data_from_consol.Ad,
    'Rent_of_the_day:': Data_from_consol.RentOfDay
}


class Writer:
    def __init__(self, txt=None):
        if len(sys.argv) > 1:
            self.mode = sys.argv[1]
            if len(sys.argv) > 2:
                self.txt = sys.argv[2]
            else:
                if self.mode == 'txt':
                    self.txt = Data_from_file.DEFAULT_FILE
                elif self.mode == 'json':
                    self.txt = Data_from_json.DEFAULT_JSON_FILE
                elif self.mode == 'xml':
                    self.txt = Data_from_xml.DEFAULT_XML_FILE
        else:
            self.mode = input('Choose a mode. Press "1" if you want to publish data from a txt file\nPress "2" if you want to publish data from a json file\nPress "3" if you want to publish data from a xml file  \nor type something other to choose consol mode\n')
            if self.mode == '1':
                self.mode = 'txt'
                self.txt = input('Choose a file. Press "1" if you want to publish data from the default txt file or type path to your file\n')
                if self.txt == '1':
                    self.txt = Data_from_file.DEFAULT_FILE
            elif self.mode == '2':
                self.mode = 'json'
                self.txt = input('Choose a file. Press "1" if you want to publish data from the default json file or type path to your file\n')
                if self.txt == '1':
                    self.txt = Data_from_json.DEFAULT_JSON_FILE
            elif self.mode == '3':
                self.mode = 'xml'
                self.txt = input('Choose a file. Press "1" if you want to publish data from the default xml file or type path to your file\n')
                if self.txt == '1':
                    self.txt = Data_from_xml.DEFAULT_XML_FILE
            else:
                self.mode = 'console'
                self.txt = None
        self.run()

    def save_in_db(self, publication):
        db = DB_Client.DBConnection()
        db.create_table(publication.table_name)
        db.insert(publication.table_name, publication.condition, publication.values)
        db.connection.close()


    def publish_from_console(self):
        table_name = ''
        condition = ''
        values = ''
        while True:
            counter = input(
                'Choose a type of publication:\n 1. To choose news type "1" and press Enter\n 2. To choose advertisement type "2" and press Enter\n 3. To choose RentOfDay type "3" and press Enter\n Type another symbol and press Enter to Exit\n')
            if counter == "1":
                publication = Data_from_consol.News.create_from_input()
            elif counter == "2":
                publication = Data_from_consol.Ad.create_from_input()
            elif counter == "3":
                publication = Data_from_consol.RentOfDay.create_from_input()
            else:
                print("You decide to finish publishing")
                break
            publication.publish()
            self.save_in_db(publication)

    def publish_from_file(self):
        publication = Data_from_file.DataFromFile(self.txt)
        if publication.publications != None:
            for article in publication.publications:
                data_not_published = article
                single_publication = publication.parse_publication(article)
                title = list(single_publication.keys())[0]
                if title in list(Data_from_file.keywords_for_parse.keys()):
                    article = list(publication.parse_publication(article).values())[0]
                    if title == 'News_for_publish:':
                        this_publication = Data_from_consol.News(article['Pulication_text:'], article['City_for_publish:'])
                        this_publication.publish()
                        self.save_in_db(this_publication)
                    elif title == 'Private_Ad:':
                        try:
                            expiration_date = publication.parse_date(article['Expiration_date:'])
                        except:
                            expiration_date = None
                        if expiration_date == None or publication.validate_date(expiration_date) == None:
                            publication.wrong_data.append(data_not_published)
                        else:
                            this_publication = Data_from_consol.Ad(article['Pulication_text:'], expiration_date)
                            this_publication.publish()
                            self.save_in_db(this_publication)
                    elif title == 'Rent_of_the_day:':
                        try:
                            square = int(article['Square:'])
                            price = int(article['Price:'])
                            this_publication = Data_from_consol.RentOfDay(article['Address:'], price, square)
                            this_publication.publish()
                            self.save_in_db(this_publication)
                        except:
                            publication.wrong_data.append(data_not_published)
                else:
                    publication.wrong_data.append(data_not_published)
            print(f'Data from {self.txt} is published to the {Basic_class_Publication.file_for_publications}')
        if publication.wrong_data == []:
            publication.delete_file()
        else:
            publication.save_wrong_data_in_file()
            print(f'Wrong data is saved in the {Data_from_file.file_for_wrong_data}')

    def publish_from_json(self):
        publication = Data_from_json.DataFromJsonFile(self.txt)
        if publication.publications:
            for article in publication.publications:
                data_not_published = article
                if article['title'] == 'News -------------------------' and article['pulication_text'] != '' and article['city'] != '':
                    this_publication = Data_from_consol.News(article['pulication_text'], article['city'])
                    this_publication.publish()
                    self.save_in_db(this_publication)
                elif article['title'] == 'Private Ad -------------------' and article['pulication_text'] != '':
                    try:
                        expiration_date = publication.parse_date(article['expiration_date'])
                    except:
                        expiration_date = None
                    if expiration_date == None or publication.validate_date(expiration_date) == None:
                        publication.wrong_data.append(data_not_published)
                    else:
                        this_publication = Data_from_consol.Ad(article['pulication_text'], expiration_date)
                        this_publication.publish()
                        self.save_in_db(this_publication)
                elif article['title'] == 'Rent of the day --------------' and article['address'] != '':
                    try:
                        square = int(article['square'])
                        price = int(article['price'])
                        this_publication = Data_from_consol.RentOfDay(article['address'], price, square)
                        this_publication.publish()
                        self.save_in_db(this_publication)
                    except:
                        publication.wrong_data.append(data_not_published)
                else:
                    publication.wrong_data.append(data_not_published)
            print(f'Data from {self.txt} is published to the {Basic_class_Publication.file_for_publications}')
        if publication.wrong_data == []:
            publication.delete_file()
        else:
            publication.save_wrong_data_in_file()
            print(f'Wrong data is saved in the {Data_from_json.file_for_wrong_json_data}')

    def publish_from_xml(self):
        publication = Data_from_xml.DataFromXmlFile(self.txt)
        if publication.publications:
            publication_cnt = 0
            wrong_publication_cnt = 0
            wrong_tree = ET.parse(Data_from_xml.file_for_wrong_xml_data)
            wrong_root = wrong_tree.getroot()
            for article in publication.publications.findall("publication"):
                publication.parse_publication(article)
                if publication.title == 'News' and publication.pulication_text != '' and publication.city != '':
                    this_publication = Data_from_consol.News(publication.pulication_text, publication.city)
                    this_publication.publish()
                    self.save_in_db(this_publication)
                    publication_cnt += 1
                elif publication.title == 'Private Ad' and publication.pulication_text != '':
                    try:
                        expiration_date = publication.parse_date(publication.expiration_date)
                    except:
                        expiration_date = ''
                    if expiration_date == '' or publication.validate_date(expiration_date) == None:
                        wrong_root.append(article)
                        wrong_publication_cnt += 1
                    else:
                        this_publication = Data_from_consol.Ad(publication.pulication_text, expiration_date)
                        this_publication.publish()
                        self.save_in_db(this_publication)
                        publication_cnt += 1
                elif publication.title == 'Rent of the day' and publication.address != '':
                    try:
                        square = int(publication.square)
                        price = int(publication.price)
                        this_publication = Data_from_consol.RentOfDay(publication.address, price, square)
                        this_publication.publish()
                        self.save_in_db(this_publication)
                        publication_cnt += 1
                    except:
                        wrong_root.append(article)
                        wrong_publication_cnt += 1
                else:
                    wrong_root.append(article)
                    wrong_publication_cnt += 1
            if publication_cnt > 0:
                print(f'Data from {self.txt} is published to the {Basic_class_Publication.file_for_publications}')
        if wrong_publication_cnt> 0:
            wrong_tree.write(Data_from_xml.file_for_wrong_xml_data, encoding="utf-8", xml_declaration=True)
            print(f'Wrong data is saved in the {Data_from_xml.file_for_wrong_xml_data}')
        if publication_cnt > 0 and wrong_publication_cnt == 0:
            publication.delete_file()

    def run(self):
        if self.mode == 'txt':
            from_file = Data_from_file.DataFromFile(self.txt)
            if from_file.txt_from_file == None:
                print("There's nothing to publish. The program has been completed")
                return None
            self.publish_from_file()
        elif self.mode == 'json':
            from_file = Data_from_json.DataFromJsonFile(self.txt)
            if from_file.publications == None:
                print("There's nothing to publish. The program has been completed")
                return None
            self.publish_from_json()
        elif self.mode == 'xml':
            from_file = Data_from_xml.DataFromXmlFile(self.txt)
            if from_file.publications == None:
                print("There's nothing to publish. The program has been completed")
                return None
            self.publish_from_xml()
        elif self.mode == 'console':
            self.publish_from_console()
        all_publications = Basic_class_Publication.Publication.read_publications()
        Statistics.Prepare_csv(all_publications)


if __name__ == "__main__":
    Writer()