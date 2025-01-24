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
# The function accepts INTEGER n as parameter.
#

## MM: I understand the sum of each digit
## What I don't understand is how to efficiently find the prime factors of a large number
## This I needed to look up - we are utilizing a brute force algo based on Euler's method
## The below code is what I created to understand what's going on here:

## CODE THAT EXPLAINS ALGO AT WORK ##
#####################################

# def prime_factors(n):
    # i = 2
    # factors = []
    # while i * i <= n:
    #   print("Test: "+str(n)+" divided by "+str(i))
    #   if n % i:
    #     print("This doesn't work, because "+str(n)+" divided by "+str(i)+" is "+str(n/i))
    #     i += 1
    #     # print(str(i)+" is not a factor, because "str(n)+" divided by "+str(i)+" is "+str(n/i))

    #   else:
    #     # print(i)
    #     n //= i
    #     print(str(i)+" IS a factor")
    #     print("New n is: "+str(n))
    #     factors.append(i)
    # if n > 1:
    #     factors.append(n)
    # return factors


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    
    return factors



def solve(n):
    prime_list = prime_factors(n)
    
    prime_digits = []
    num_digits = []

    for num in prime_list:
        for digit in str(num):
            prime_digits.append(int(digit))

    for digit in str(n):
        num_digits.append(int(digit))


    sum_pd = sum(prime_digits)
    sum_nd = sum(num_digits)

    # print(sum_pd)
    # print(sum_nd)

    if sum_nd == sum_pd:
        return 1
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = solve(n)

    fptr.write(str(result) + '\n')

    fptr.close()

