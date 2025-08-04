#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hr=int(s[0:2])
    half=s[8:10]
    if half=="PM":
        if hr==12:
            hr=str(hr)
        else:
            hr=hr+12
            hr=str(hr)

    else:
        if hr==12:
            hr=str("00")
        else:
            hr="0"+str(hr)
    print(hr+":"+s[3:5]+":"+s[6:8])

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
