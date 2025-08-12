#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alph=lowercase_alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))
    s=s.lower()
    for i in alph:
        if s.count(i)==0:
            return "not pangram"
            break
        else:
            if i=="z":
                return "pangram"
                break
            continue
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
