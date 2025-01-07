#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    divisors = []

    for i in range (1, n+1):
        if n % i == 0:
            divisors.append(i)
            
    best_divisor = 0
    best_divisor_sum = 0

    for divisor in divisors:
        if len(str(divisor)) == 1:
            if divisor > best_divisor_sum:
                best_divisor = divisor
                best_divisor_sum = divisor

        else:
            digit_sum = 0
            length = len(str(divisor))
            for i in range(0, length):
                digit_sum += int(str(divisor)[i])

            if digit_sum == best_divisor_sum:
                if divisor < best_divisor:
                    best_divisor = divisor
                    best_divisor_sum = digit_sum

            elif digit_sum > best_divisor_sum:
                best_divisor = divisor
                best_divisor_sum = digit_sum
                
                
    print(best_divisor)
    
