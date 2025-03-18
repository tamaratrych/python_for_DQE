"""
Create a python script:

create list of 100 random numbers from 0 to 1000
sort list from min to max (without using sort())
calculate average for even and odd numbers
print both average result in console
Each line of code should be commented with description.

Commit script to git repository and provide link as home task result.
"""

from random import randint

# Create an empty list
random_list = []

# Fill the list with random numbers in a loop
for i in range(100): # Run the loop 100 times
    random_list.append(randint(0, 1000))  # Add a randomly generated number to the end of the list

# Sort the list
for i in range(99): # We do not take the last number into the cycle, because there is nothing to rearrange it with, it will already be the maximum
    min_value = min(random_list[i:]) # Find the minimum value from the list, starting from the unsorted position to the end
    min_index = random_list[i:].index(min_value) # Find the index of the value found in the previous step (in the unsorted part of the list)
    random_list[(min_index + i)] = random_list[i] # Place the first value of the unsorted range in the found position
    random_list[i] = min_value # Put the minimum value at the beginning of the unsorted range

# Calculate average for even and odd numbers
even_cnt = 0 # Create separate variables for count of even and odd numbers
odd_cnt = 0
even_sum = 0 # Create separate variables for sum of even and odd numbers
odd_sum = 0
for i in random_list: # For each number in the list
    if i % 2 == 1: # find out if it is an odd or an even number
        odd_cnt += 1 # If it is an odd number, add 1 to odd_cnt
        odd_sum += i # and add it to odd_sum
    else:
        even_cnt += 1 # If it is an even number, add 1 to even_cnt
        even_sum += i # and add it to even_sum


print("Average for even numbers: ", even_sum/even_cnt)
print("Average for odd numbers: ", odd_sum/odd_cnt)