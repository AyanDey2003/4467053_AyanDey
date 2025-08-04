#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    a,b=0,0
    for i in range(len(arr)-1):
        a=a+arr[i]
    for i in range(1,len(arr)):
        b=b+arr[i]
    print(a,b)
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
