#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    new = ''
    lex = list(map(chr, range(97, 123)))   
    lex2 = list(map(chr, range(65, 91)))   
    for i in s:
        if i.isalpha():
            if i in lex:
                for j in lex:
                    if j == i:
                        pos = lex.index(j)
                        if (pos + k) < len(lex):
                            new = new + lex[pos + k]
                        else:
                            extra = (pos + k) % len(lex)
                            new = new + lex[extra]
            elif i in lex2:
                for j in lex2:
                    if j == i:
                        pos = lex2.index(j)
                        if (pos + k) < len(lex2):
                            new = new + lex2[pos + k]
                        else:
                            extra = (pos + k) % len(lex2)
                            new = new + lex2[extra]
        else:
            new = new + i
    return new


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
