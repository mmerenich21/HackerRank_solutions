#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'canConstruct' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY a as parameter.
#

## MM: Iniitially I thought of looping through all combinations of the numbers and checking if the sum is divisible by 3. But that would be a very inefficient solution.
## Trying to learn from some of the other problems, I figured there was a rule to check if a larger number was divisible by 3.
## Turns out, this is true (and made the problem much easier). If the sum of the digits of a number is divisible by 3, then the number itself is divisible by 3.

def canConstruct(a):
    # Return "Yes" or "No" denoting whether you can construct the required number.
    
    int_list = []
    
    for ele in a:
        for num in str(ele):
            int_list.append(int(num))
            
    if sum(int_list)%3 == 0:
        return "Yes"
    else:
        return "No"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = canConstruct(a)

        fptr.write(result + '\n')

    fptr.close()
