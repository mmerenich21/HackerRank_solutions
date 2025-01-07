#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'restaurant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER b
#

## MM: I haven't seen my approach in the comments yet and figured it may help out anyone else trying to wrap their head around it.
## Alternative to the GCD approach (well documented in the dicussion), I mentally wanted to find the largest square that was divisible by both l and b.
## It's not the most efficient, but it's how I saw the solution:

def restaurant(l, b):
    squares = [x**2 for x in range(1, 1001)]
    mult = l*b
    final_squares = mult

    l_divisors = [i for i in range(1, l + 1) if l % i == 0]
    b_divisors = [i for i in range(1, b + 1) if b % i == 0]
    
    if l == b:
        print("scenario 0")
        final_squares = 1
    else:
        mult_divisors = [i for i in range(1, mult + 1) if mult % i == 0]

        for mult_div in mult_divisors:
            if mult_div in squares:
                if (mult_div**(1/2) in l_divisors) and (mult_div**(1/2) in b_divisors):
                    final_squares = mult / mult_div
    
    return int(final_squares)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = restaurant(l, b)

        fptr.write(str(result) + '\n')

    fptr.close()
