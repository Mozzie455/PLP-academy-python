#!/usr/bin/python3

"""
TODO:Create a function that has one parameter named num.
The function should return True if num is divisible by 10, and False otherwise.
Consider using modulo operator % to check for divisibility
"""


# Define the function
def divisible_by_ten(num):
    # Calculate the reminder of the input divided by 10
    reminder = num % 10
    # Check if the reminder is 0
    if reminder == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    # Prompt the user for the number
    num = int(input("Enter the number: "))
    # Check if num is a divisible by 10
    result = divisible_by_ten(num)
    print("Result:", result)
