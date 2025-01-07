#!/bin/python3

import math
import os
import random
import re
import sys
import array

#
# Complete the 'findPoint' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER px
#  2. INTEGER py
#  3. INTEGER qx
#  4. INTEGER qy
#

def findPoint(px, py, qx, qy):
    # MM: what are the scenarios you need to account for? (pos, neg)
    # Start with taking the difference, then figure out how to apply it
    
    x_diff = qx-px
    y_diff = qy-py
    
    rx = qx+x_diff
    ry = qy+y_diff
    
    final_r = array.array('i', [rx, ry])
    
    return final_r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        px = int(first_multiple_input[0])

        py = int(first_multiple_input[1])

        qx = int(first_multiple_input[2])

        qy = int(first_multiple_input[3])

        result = findPoint(px, py, qx, qy)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
