#!/usr/bin/python3

"""
TODO:Create a function that calculates final price after applying a discount
"""


def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_price = price - (price * discount_percent / 100)
        return discount_price
    else:
        return price


"""
TODO:Using the function, print the final price after applying the discount, or if no discount was applied, print the original price
"""
if __name__ == '__main__':
    # Prompt the user to enter the original price of the item
    price = float(input("Enter the original price of the item : "))

    # Prompt the user to enter the discount percentage
    discount_percent = float(input("Enter the discount_percentage : "))
    # Check if discount is greater than 0%
    if discount_percent > 0:
        # Calculate the final price after applying the discount
        price = calculate_discount(price, discount_percent)
        # Print the final price after applying the discount
        print(f"Final price after, {discount_percent}% discount : {price:.2f}")

    else:
        # If no discount was applied, print the original price
        print(f"No discount applied. Original price: {price:.2f}")
