#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'movingTiles' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER s1
#  3. INTEGER s2
#  4. INTEGER_ARRAY queries
#
## MM: This was considered an EASY problem, but I spent a lot of time on this.
## My first solution solved for a handful of inputs, but ultimately I had to look up the formula required to solve this.
## I've taken a lot of math courses, but I've never seen this formula before (or just completely forgot about it).


def movingTiles(l, s1, s2, queries):
    results_list = []
    
    for query in queries:
        t_sec = math.sqrt(2)/abs(s1-s2)*(l-math.sqrt(query))
        results_list.append(t_sec)
    
    return results_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    l = int(first_multiple_input[0])

    s1 = int(first_multiple_input[1])

    s2 = int(first_multiple_input[2])

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
