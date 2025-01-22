#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER y1
#  3. INTEGER x2
#  4. INTEGER y2
#

## MM: I want to first find the slope of the line between the two points.
## This is given by (y2-y1)/(x2-x1).
## I want to loop through all possibilities of the x and y coordinates of the point between the two points, but I fear this will be too computationally expensive.
## Before I checked on this online, I saw there was a pattern in the examples given, as it related to the difference between the x and y coordinates of the two points.
## If we compared the differences, the number of points between the two points was 1 less than the differences themselves if the differences were equal
## I the first example though, the differences were not equal, but the number of points between the two points was 1 less than the differences when x2-x1 was divided into y2-y1.
## In the end, I found that the number of points between the two points was the greatest common divisor of the differences between the x and y coordinates of the two points.

## I looked up how to efficiently find the greatest common divisor of two numbers, and found the Euclidean algorithm.
## This is much easier than doing this manually, so I implemented this below.

def solve(x1, y1, x2, y2):

    # Find the diffs first
    y_diff = abs(y2-y1)
    x_diff = abs(x2-x1)
    
    # Key for the Euclidean algorithm is to find the max and min of the two numbers, as the max must be divided by the min first
    a = max(y_diff, x_diff)
    b = min(y_diff, x_diff)
    
    while b:
        a, b = b, a % b
    
    return a - 1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        x1 = int(first_multiple_input[0])

        y1 = int(first_multiple_input[1])

        x2 = int(first_multiple_input[2])

        y2 = int(first_multiple_input[3])

        result = solve(x1, y1, x2, y2)

        fptr.write(str(result) + '\n')

    fptr.close()
