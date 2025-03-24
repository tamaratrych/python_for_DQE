import sys
from Modules import Data_from_consol
from Modules import Data_from_file
from Modules import Statistics
from Modules import Basic_class_Publication


class_publication = {
    'News_for_publish:': Data_from_consol.News,
    'Private_Ad:': Data_from_consol.Ad,
    'Rent_of_the_day:': Data_from_consol.RentOfDay
}


class Writer:
    def __init__(self, txt=None):
        if len(sys.argv) > 1:
            self.mode = 'file'
            self.txt = sys.argv[1]
        else:
            self.mode = input('Choose a mode. Press "1" if you want to publish data from a file or type something other to choose consol mode\n')
            if self.mode == '1':
                self.mode = 'file'
                self.txt = input('Choose a file. Press "1" if you want to publish data from the default file or type path to your file\n')
                if self.txt == '1':
                    self.txt = Data_from_file.DEFAULT_FILE
            else:
                self.mode = 'console'
                self.txt = None
        self.run()

    def publish_from_console(self):
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
      #      all_publications = publication.read_publications()
       #     Statistics.Prepare_csv(all_publications)

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
                        Data_from_consol.News(article['Pulication_text:'], article['City_for_publish:']).publish()
                    elif title == 'Private_Ad:':
                        try:
                            expiration_date = publication.parse_date(article['Expiration_date:'])
                        except:
                            expiration_date = None
                        if expiration_date == None or publication.validate_date(expiration_date) == None:
                            publication.wrong_data.append(data_not_published)
                        else:
                            Data_from_consol.Ad(article['Pulication_text:'], expiration_date).publish()
                    elif title == 'Rent_of_the_day:':
                        try:
                            square = int(article['Square:'])
                            price = int(article['Price:'])
                            Data_from_consol.RentOfDay(article['Address:'], price, square).publish()
                        except:
                            publication.wrong_data.append(data_not_published)
                    else:
                        publication.wrong_data.append(data_not_published)
                else:
                    publication.wrong_data.append(data_not_published)
     #   all_publications = publication.read_publications()
      #  Statistics.Prepare_csv(all_publications)

        if publication.wrong_data == []:
            publication.delete_file()
        else:
            publication.save_wrong_data_in_file()

    def run(self):
        if self.mode == 'file':
            from_file = Data_from_file.DataFromFile(self.txt)
            if from_file.txt_from_file == None:
                print("There's nothing to publish. The program has been completed")
                return None
            self.publish_from_file()
        elif self.mode == 'console':
            self.publish_from_console()
        all_publications = Basic_class_Publication.Publication.read_publications()
        Statistics.Prepare_csv(all_publications)


if __name__ == "__main__":
    Writer()