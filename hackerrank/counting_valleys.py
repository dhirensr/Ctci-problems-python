#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    result=0
    mountain_steps=0
    valley_steps=0
    for i in s:
        if(i=='U'):
            result+=1
        if(i=="D"):
            result-=1
        if(result>0):
            mountain_steps+=1
        if(result <0):
            valley_steps+=1
    print(valley_steps)
    return 0

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
