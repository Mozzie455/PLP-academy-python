#!/usr/bin/python3

'''Objective: To learn how to take user input in Python'''


"""A program that asks the user for their name, age, and location and then prints out a personalized message.

    Example:
    >>> from user_input import user_input
    >>> user_input("Makau",25,"Macha")    
    'Hello Makau, you are 25 years old and live in Macha'

    Args:
        name (str): The name used to identify the user
        age (int): The age of the identified user
        location (str): The location of the user
    
    
    Return:
        print out a personalized message    
"""
name = str(input("Input your name: "))
age = int(input("Please input your age: "))
location = str(input("Please input your location: "))
print(f"Hello {name}, you are {age} years old and live in {location}")

