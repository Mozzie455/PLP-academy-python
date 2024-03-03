#!/usr/bin/python3

"""Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters."""

# Accept user input to create a list
list1 = input("Enter words separated by a comma: ")

# Split the input and remove the white spaces
list_strings = [s.strip() for s in list1.split(',')]

#Create a list that only the words that have an odd number of characters
new_list = [word for word in list_strings if len(word) % 2 != 0] 

# Print the results
print(f"The words are: {new_list}")