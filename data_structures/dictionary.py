#!/usr/bin/python3

"""Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console."""

# Create an empty dictionary to store person's information
personal_info = {}

#Ask user for input 
personal_info['name'] = input("Enter the person's name: ")
personal_info['age'] = input("Enter the person's age: ")
personal_info['favorate_color'] = input("Enter the person's favorate_color: ")

#Print the person's information in a dictionary
print(f"Person's information: ")
for key, value in personal_info.items():
    print(f"{key}:{value}")

