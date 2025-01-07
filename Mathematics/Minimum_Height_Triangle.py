#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lowestTriangle' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER trianglebase
#  2. INTEGER area
#

def lowestTriangle(trianglebase, area):
    # area = (0.5)(base)(height)
    h_floor = math.floor((2*area)/trianglebase)
    h_ceil = math.ceil((2*area)/trianglebase)
    
    if (0.5)*(h_floor)*trianglebase >= area:
        return h_floor
    else:
        return h_ceil

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    trianglebase = int(first_multiple_input[0])

    area = int(first_multiple_input[1])

    height = lowestTriangle(trianglebase, area)

    fptr.write(str(height) + '\n')

    fptr.close()
