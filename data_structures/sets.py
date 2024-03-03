#!/usr/bin/python3

"""Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets."""

# Accept user input to create two list of integers
list1_input = input("Enter integers separated by comma for the first set: ")
list2_input = input("Enter integers separated by comma for the second set: ")

#Split the input using commas and remove whitespaces
list1_strings = [s.strip() for s in list1_input.split(',')]
list2_strings = [s.strip() for s in list2_input.split(',')]

# Convert the input strings into integers
integers_list1 = [num for num in list1_strings if num.isdigit()]
integers_list2 = [num for num in list2_strings if num.isdigit()]

# Convert the lists to sets
set1 = set(integers_list1)
set2 = set(integers_list2)
# Create a new set containing only the common elements
set3 = set1.intersection(set2)

# Print the new set
print(f"The common element between the first and the second set are: {set3}")