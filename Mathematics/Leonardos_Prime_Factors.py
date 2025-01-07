#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

## MM: so we tried the bottoms-up approach, but it's not computationally friendly or feasible
## I don't think it's cheating to list the primes, as we used the first approach to identify them
## So let's use this list to figure out:
## A) what's the highest combo multiplying prime numbers that fits within the n range
## B) produce rules that just check whether the number falls between these intervals, and assign the max value accordingly

def primeCount(n):
    prev_count = 1
    final_count = 0
    
    primes_dict = {
        1: 2,
        2: 6,
        3: 30,
        4: 210,
        5: 2310,
        6: 30030,
        7: 510510,
        8: 9699690,
        9: 223092870,
        10: 6469693230,
        11: 200560490130,
        12: 7420738134810,
        13: 304250263527210,
        14: 13082761331670030,
        15: 614889782588491410,
        16: 32589158477190044730
    }     
            
    for k, v in primes_dict.items():
        if (n == 0) or (n == 1):
            final_count = 0
            return final_count
            
        elif n < v:
            final_count = prev_count
            return final_count
            
        elif n == v:
            final_count = k
            return final_count
        
        else:
            prev_count = k
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
