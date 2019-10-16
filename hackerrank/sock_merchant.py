#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pair_dict={}
    result=0
    for i in set(ar):
        pair_dict[i]=0
    for i in ar:
        pair_dict[i]+=1
        if(pair_dict[i]==2):
            pair_dict[i]=0
            result+=1
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
