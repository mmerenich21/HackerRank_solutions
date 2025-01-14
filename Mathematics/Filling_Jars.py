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
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY operations
#

## MM: 

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
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY operations
#

## MM: this first approach worked, but I needed to make this more effiecient

# def solve(n, operations):
#     jar_dict = {}
#     jar_list = [i for i in range(1, n+1)]
    
#     for num in jar_list:
#         jar_dict[num] = 0

#     # print(jar_dict)
    
#     for op in operations:
#         a, b, k = op
    
#         if a == b:
#             jar_dict[a] += k
    
#         else:
#             ## Create range of elements
#             inner_range = [i for i in range(a, b+1)]
#             # print(inner_range)
#             for num in inner_range:
#                 jar_dict[num] += k

#     sum_of_values = sum(jar_dict.values())

#     # Get the number of values
#     num_of_values = len(jar_dict)
    
#     # Calculate the average
#     average = int(math.floor(sum_of_values / num_of_values))
    
#     return(average)


## MM: the following code took away list creation and used a more efficient way to create/update dictionaries
## It was still not efficient enough - was there another way to do this?

# def fill_jar(n, operations):
#     jar_dict = {i:0 for i in range(1, n+1)}
#     # jar_list = [i for i in range(1, n+1)]
    
#     # for num in jar_list:
#     #     jar_dict[num] = 0
    
#     for op in operations_all:
#         a, b, k = op
    
#         if a == b:
#             jar_dict[a] += k
    
#         else:
#             ## Create range of elements
            
#             # inner_range = [i for i in range(a, b+1)]
#             # print(inner_range)
#             for num in range(a, b+1):
#                 jar_dict[num] += k

#     sum_of_values = sum(jar_dict.values())

#     # Get the number of values
#     num_of_values = len(jar_dict)
    
#     # Calculate the average
#     average = int(math.floor(sum_of_values / num_of_values))
    
#     return(average)


## MM: I realized that the indices of the jars and where we put the candies are not important
## We can just add the candies to the jars and then calculate the average
## Admittedly, I had to look at the discussion to get this insight


def solve(n, operations):
    total_rolling = 0

    for op in operations:
        a, b, k = op

        total_rolling+= ((b-a)+1)*k

        
    # Calculate the average
    average = int(math.floor(total_rolling / n))
    
    return(average)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    operations = []

    for _ in range(m):
        operations.append(list(map(int, input().rstrip().split())))

    result = solve(n, operations)

    fptr.write(str(result) + '\n')

    fptr.close()

