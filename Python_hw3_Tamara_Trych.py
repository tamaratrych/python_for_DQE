import re


my_text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

substring = 'add it to the END OF this Paragraph.' # Save a part o text after which we need to insert any sentence
index = my_text.index(substring) + len(substring) # Find the place where we insert a new sentence as sum of the start of substring and length of this substring

str_parts = [] # Divide the string into sentences. Save every sentence in this list
for i in re.findall('[^\.]*?[\.!\?]\s*', my_text): # Patern: Start - any number of symbols except "." End - one of the symbol ".", "!" or "?" and any white spaces
    str_parts.append(i.capitalize()) # Make the first letter in capital case and others - small letters

new_str = ''.join(str_parts) # Join formated parts to one string

last_words = [] # Create a list to store last words of the sentences
for i in re.findall('[^\.\s]*?[\.!\?]\s*', my_text): # Patern: Start - any number of symbols except "." and white spaces. End - one of the symbol ".", "!" or "?" and any white spaces
    i = i.strip().lower().strip('.') # Delete white spaces around the word -> Make all symbols in small case -> Delete "." fronm the begining and end of the word
    if i: # Gather all words except empty space ''
        last_words.append(i)

new_sentence = ' '.join(last_words).capitalize() # Join all last words through white space -> Make the first letter in capital case
new_sentence = ''.join([new_sentence, '.']) # Add symbol '.' at the end of the generated sentence
new_sentence = ''.join([' ', new_sentence]) # Add symbol ' ' at the start of the generated sentence

new_str = "{}{}{}".format(new_str[:index], new_sentence, new_str[index:]) # Insert a new sentence to the particular place (by calculated index)

new_str = new_str.replace(' iz ', ' is ') # Fix mistakes: the verb is written as iz
print(new_str)

space_num = 0
for i in new_str: # Go through every symbol and if it's a white space increment space_num
    space_num = space_num + 1 if re.search('\s', i) else space_num

print('\nNumber of whitespace characters in this text -', space_num)
