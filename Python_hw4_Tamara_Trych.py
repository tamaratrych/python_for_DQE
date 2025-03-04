"""
 Refactor homeworks from module 2 and 3 using functional approach with decomposition
"""


from random import randint, choice
import string
from collections import defaultdict
import re


def generate_list_random_dict(): # Create a list of random number of dicts
    dict_list = [] # Create an empty list
    for i in range(randint(2, 10)): # Run the cycle a random number of times (min 2 times, max 10 times)
        random_letters = set(''.join(choice(string.ascii_lowercase) for _ in range(randint(2, 10)))) # Create a string from 2-10 letters and transform to det to be sure that there are no duplicates
        new_dict = {random_letter:randint(0,100) for random_letter in random_letters} # Create a dictionary in which the keys are the letters from the previous step
        dict_list.append(new_dict) # Add the dictionary to the list

    return dict_list

def fill_dict_with_values_from_another_dicts(any_dict_list):
    all_values_dict = defaultdict(list)  # Create a new dict
    for i in any_dict_list:  # Go through every dict in the list
        for j in i.keys():  #
            all_values_dict[j].append(i[j])  # values of created dict are the list of all values of this key

    return all_values_dict

def choose_max_dict_value(any_dict):
    result_dict = {}
    for i in any_dict.keys():
        result_dict[i] = max(any_dict[i])

    return result_dict

def combine_dicts_leave_max_value_for_same_key(any_dict_list):
    dict_with_all_values = fill_dict_with_values_from_another_dicts(any_dict_list)
    result_dict = choose_max_dict_value(dict_with_all_values)

    x = 1  # Enter a variable that indicates the ordinal number of the dictionary in the list
    for i in any_dict_list:  # Go through each dictionary
        for j in i.keys():
            if dict_with_all_values[j] != 1:  # If such a key occurs in more than one dictionary, then
                if result_dict[j] == i[j]:  # Check if the maximum value is stored in this dictionary, if so, then
                    del result_dict[j]  # Delete a record with this key from the resulting dictionary
                    new_key = str(j) + '_' + str(x)  # Generate a new key
                    result_dict[new_key] = i[j]  # Add new generated key with value to the resulting dictionary
                    dict_with_all_values[j] = 1  # Since a dictionary has been found that stores the maximum value, in order not to process this value anymore (even if there is the same value in another dictionary under this key), then it is forced to specify that there is one value with this key
        x += 1  # Increase the dictionary counter by one

    return result_dict


def capitalize_text(any_string):
    str_parts = [] # Divide the string into sentences. Save every sentence in this list
    for i in re.findall(r'[^\.]*?[\.!\?]\s*', any_string): # Patern: Start - any number of symbols except "." End - one of the symbol ".", "!" or "?" and any white spaces
        str_parts.append(i.capitalize()) # Make the first letter in capital case and others - small letters

    new_str = ''.join(str_parts) # Join formated parts to one string

    return new_str


def generate_sentence_from_last_words(any_string):
    last_words = [] # Create a list to store last words of the sentences
    for i in re.findall(r'[^\.\s]*?[\.!\?]\s*', any_string): # Patern: Start - any number of symbols except "." and white spaces. End - one of the symbol ".", "!" or "?" and any white spaces
        i = i.strip().lower().strip(r'[.!?]') # Delete white spaces around the word -> Make all symbols in small case -> Delete "." fron the begining and end of the word
        if i: # Gather all words except empty space ''
            last_words.append(i)

    new_sentence = ' '.join(last_words).capitalize() # Join all last words through white space -> Make the first letter in capital case
    new_sentence = ''.join([new_sentence, '.']) # Add symbol '.' at the end of the generated sentence
    new_sentence = ''.join([' ', new_sentence])  # Add symbol ' ' at the start of the generated sentence

    return new_sentence

def add_str_into_text(any_string, any_substring, new_substring):
    index = any_string.index(any_substring) + len(any_substring)  # Find the place where we insert a new sentence as sum of the start of substring and length of this substring
    new_str = "{}{}{}".format(any_string[:index], new_substring, any_string[index:])  # Insert a new sentence to the particular place (by calculated index)

    return new_str


def fix_mistakes(any_string):
    correct_str = any_string.replace(' iz ', ' is ')
    correct_str = correct_str.replace('\'iz ', '\'is ')

    return correct_str


def count_spaces(any_string):
    space_num = 0
    for i in any_string: # Go through every symbol and if it's a white space increment space_num
        space_num = space_num + 1 if re.search(r'\s', i) else space_num

    return space_num


def modificate_text(any_string, any_substring):
    new_sentence = generate_sentence_from_last_words(any_string)
    new_str = add_str_into_text(any_string, any_substring, new_sentence) # Add the new sentence to our string
    first_capital_letter = capitalize_text(new_str)
    normalized_str = fix_mistakes(first_capital_letter)

    return normalized_str


# hw2 1. create a list of random number of dicts (from 2 to 10)
list_random_dicts = generate_list_random_dict()
for i in list_random_dicts:
    print(i)

# hw2 2. get previously generated list of dicts and create one common dict
common_dict = combine_dicts_leave_max_value_for_same_key(list_random_dicts)
print(common_dict)

# hw 3
my_text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View... also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE?



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex! caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

phrase_for_index = 'add it to the END OF this Paragraph.'
my_normalized_text = modificate_text(my_text, phrase_for_index)
print(my_normalized_text)

space_num = count_spaces(my_normalized_text)
print('\nNumber of whitespace characters in this text -', space_num)
