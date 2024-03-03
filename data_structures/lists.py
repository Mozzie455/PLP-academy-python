#!/usr/bin/python3

"""Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list."""

# Accept user input to create a list of integers
user_input = input("Enter a list of integers separate by commas : ")
# Split the input using commas
user_list = user_input.split(',')
#Determine the length of the list
user_list_len = len(user_list)
# Initialize both count and total to zero
count = 0
total = 0

while count < user_list_len:
    # Convert string to integer
    user_list[count] = int(user_list[count].strip())
    # Add the values of the array
    total += user_list[count]
    count += 1
print(f"The sum of the integers in the list is: {total}")

