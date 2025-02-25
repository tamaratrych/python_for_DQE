"""
Write a code, which will:

1. create a list of random number of dicts (from 2 to 10)

dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
2. get previously generated list of dicts and create one common dict:

if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
Each line of code should be commented with description.

Commit script to git repository and provide link as home task result.
"""

from random import randint, choice
import string
from collections import defaultdict


# Create a list of random number of dicts
dict_list = [] # Create an empty list
all_keys = []
for i in range(randint(2, 10)): # Run the cycle a random number of times (min 2 times, max 10 times)
    random_letters = set(''.join(choice(string.ascii_lowercase) for _ in range(randint(2, 10)))) # Create a string from 2-10 letters and transform to det to be sure that there are no duplicates
    new_dict = {random_letter:randint(0,100) for random_letter in random_letters} # Create a dictionary in which the keys are the letters from the previous step
    all_keys.extend(list(new_dict)) # Collect keys (for a next task)
    dict_list.append(new_dict) # Add the dictionary to the list
# print(dict_list)

# Create one dict from dicts created in previous step
all_keys_set = set(all_keys) # Delete duplicates of keys
num_values_dict = dict.fromkeys(all_keys_set, 0) # create dict with keys from all keys (min value - 0)

# Count a number of keys in the dictionaries (group by key)
for i in dict_list: # Go through every dictionary
    for j in i.keys(): # Take every key
        num_values_dict[j] += 1 # and increase the value of the corresponding key in the dictionary "result_dict" by one

all_values_dict = defaultdict(list) # Create a new dict
for i in dict_list: # Go through every dict in the list
    for j in i.keys():
        all_values_dict[j].append(i[j]) # values of created dict are the list of all values of this key

result_dict = {} # Create an empty dict
for i in all_values_dict.keys():
    result_dict[i] = max(all_values_dict[i]) # Values is the maximum value for this key

# It remains to specify the dictionary number with the maximum value
x = 1 # Enter a variable that indicates the ordinal number of the dictionary in the list
for i in dict_list: # Go through each dictionary
    for j in i.keys():
        if num_values_dict[j] != 1: # If such a key occurs in more than one dictionary, then
            if result_dict[j] == i[j]: # Check if the maximum value is stored in this dictionary, if so, then
                del result_dict[j] # Delete a record with this key from the resulting dictionary
                new_key = str(j) + '_' + str(x) # Generate a new key
                result_dict[new_key] = i[j] # Add new generated key with value to the resulting dictionary
                num_values_dict[j] = 1 # Since a dictionary has been found that stores the maximum value, in order not to process this value anymore (even if there is the same value in another dictionary under this key), then it is forced to specify that there is one value with this key
    x += 1 # Increase the dictionary counter by one

# print(result_dict)





