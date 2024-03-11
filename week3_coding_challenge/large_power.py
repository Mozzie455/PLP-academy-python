#!/usr/bin/python3

"""
TODO:Create a function that takes two parameters named base and exponent.
If base raised to exponent is greater than 5000 return True, else return False
"""


# Define the function
def large_power(base, exponent):
    # Calculate the result of base to the power of exponent
    result = base ** exponent
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False


if __name__ == '__main__':
    # Prompt the user to input the base
    base = int(input("Enter the base value: "))
    # Prompt the user to input the exponent
    exponent = int(input("Enter the exponent: "))
    result = large_power(base, exponent)
    print("Result:", result)
