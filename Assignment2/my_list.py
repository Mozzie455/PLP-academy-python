#!/usr/bin/python3

# Create an empty list
my_list = []

#Add values using append function
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position
my_list.insert(1,15)

# Use extend functionto add another list
my_list.extend( [50, 60, 70])

# Remove the last element
my_list.pop(-1)

# Sort in ascending order
my_list.sort()

# Find and print the index of the value 30
print(my_list.index(30))

#print(my_list)