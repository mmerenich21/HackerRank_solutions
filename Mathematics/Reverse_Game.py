#!/bin/python3

import math
import os
import random
import re
import sys


### THIS IS THE MORE EFFICIENT SOLUTION ###
# Things to review: combinatory mathematics, permutations, and the math behind the pattern

def reverse_game(n, k):
    if k < n // 2:
        return 2 * k + 1
    else:
        return 2 * (n - 1 - k)


if __name__ == '__main__':
    t = int(input().strip())
    
    for _ in range(t):
        n, k = map(int, input().strip().split())

        print(reverse_game(n, k))


     ### THIS SOLUTION WORKS, BUT IT'S NOT EFFICIENT ENOUGH FOR THE LARGER TEST CASES ###
                
        # ## First, get the initial list
        # ## I called this test_list2 in my test code
        # test_list2 = []

        # for i in range(0, n):
        #     test_list2.append(i)
        
        # ## Now solve
        # ## There was a pattern here - when I wrote out the pattern, we're always taking the first or last element, if we remove the element recorded the instance before
        # ## So I've looped through the original list, popped either the first or last (pending if the element is even or odd) and appended that element to final_list[]
        # final_list = []
        # initial_len = len(test_list2)
        # # print(initial_len)

        # for i in range(1, initial_len+1):
        #     # print(i)
        #     if i%2 == 0:
        #         # print(str(i)+" is even")
        #         # print(test_list2[0])
        #         final_list.append(test_list2.pop(0))
        #         # print(final_list)

        #     else:
        #         # print(str(i)+" is odd")
        #         # print(test_list2[-1])
        #         final_list.append(test_list2.pop())
        #         # print(final_list)

        # ## Final piece: we have the final list reversed all the way through
        # ## Now we just need the to find the index of the element K
        
        # index_ = final_list.index(k)
        
        # print(index_)