#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'romanizer' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def romanizer(numbers):
    # Write your code here
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
           
    answer = ''
    for i in range(len(val)):
        while numbers >= val[i]:
            answer += roman[i]
            numbers -= val[i]
    return answer
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = romanizer(numbers)

    fptr.write(result + '\n')

    fptr.close()