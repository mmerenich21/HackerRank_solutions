#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeGrid' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER r
#  2. INTEGER c
#

## MM: I wrote this one out by hand to see the pattern
## First I noticed that columns were always going to add 2, pending the column number
## I figured out odd rows first, then knew evens only added 1 from the same logic

def strangeGrid(r, c):
    c_final = (c-1)*2
    
    ## If even:
    if r%2 == 0:
        r_final = ((r-2)*5)+1

    ## Else odd:
    else:
        r_final = (r-1)*5
        
    return r_final+c_final

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()