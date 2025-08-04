#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    a,b,c=0,0,0
    for i in arr:
        if i>0:
            a=a+1
        elif i<0:
            b=b+1
        elif i==0:
            c=c+1
    print(a/len(arr))
    print(b/len(arr))
    print(c/len(arr))
        
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
