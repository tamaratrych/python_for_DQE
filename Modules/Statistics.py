import re
import csv
from collections import Counter

file_for_word_statistics = "words.csv"
file_for_letter_statistics = "letters.csv"

class Prepare_csv:
    def split_text(self):
        words = re.sub(r"[^\w\s']", '', self.string)
        return words.split()

    def counter(self, any_list):
        word_counts = Counter(any_list)
        return word_counts

    def list_of_letters(self, words):
        letters = [letter for word in words for letter in word]
        return letters

    def exclude_lowercase_letters(self):
        uppercase_letters = [letter for letter in self.all_letters if letter.isupper()]
        return uppercase_letters

    def __init__(self, string):
        self.string = string
        self.all_words = self.split_text()
        self.all_letters = self.list_of_letters(self.all_words)
        self.word_cnt = self.counter(list(map(str.lower, self.all_words)))
        self.letters_cnt = self.counter(list(map(str.lower, self.all_letters)))
        self.all_letters_cnt = len(self.all_letters)
        self.uppercase_latters_cnt = self.counter(self.exclude_lowercase_letters())
        self.save_word_statistics()
        self.save_letter_statistics()

    def prepare_data_to_statistics(self):
        data = []
        for letter, count in self.letters_cnt.items():
            uppercase_count = self.uppercase_latters_cnt.get(letter.upper(), 0)
            percentage = (count / self.all_letters_cnt) * 100
            data.append({
                "letter": letter,
                "count_all": count,
                "count_uppercase": uppercase_count,
                "percentage": round(percentage, 2)
            })

        return data

    def save_word_statistics(self):
        try:
            with open (file_for_word_statistics, "w", encoding="utf-8", newline="") as csvfile:
                writer = csv.writer(csvfile, delimiter='-')
                writer.writerows([[word, count] for word, count in self.word_cnt.items()])
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_letter_statistics(self):
        try:
            with open (file_for_letter_statistics, "w", encoding="utf-8", newline="") as csvfile:
                headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()
                writer.writerows(self.prepare_data_to_statistics())
        except Exception as e:
            print(f"An error occurred: {e}")

