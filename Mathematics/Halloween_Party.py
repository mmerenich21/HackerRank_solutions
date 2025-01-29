#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'halloweenParty' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER k as parameter.
#

## MM: Initially, I created a list of all possible combinations of row x column where the sum of row/column was k, but it was not efficient (it produced the correct answer, but not without runtme errors for large k values).
## Then I realized the pattern of maximum area of the rectangle for a given k. If k is even, the maximum area is (k/2)^2. If k is odd, the maximum area is floor(k/2)*ceil(k/2).
## I implemented this pattern in the function below.
## TESTING GIT PUSH

def halloweenParty(k):
    max_sum = 0

    if k%2 == 0:
        max_sum = int((k/2)**2)
        return max_sum
    else:
        max_sum = int(math.floor(k/2)*math.ceil(k/2))
        return max_sum
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        k = int(input().strip())

        result = halloweenParty(k)

        fptr.write(str(result) + '\n')

    fptr.close()
