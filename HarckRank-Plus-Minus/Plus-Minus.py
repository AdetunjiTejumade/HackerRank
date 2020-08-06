#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.


def plusMinus(arr):
    pos = []
    neg = []
    zero = []
    for i in arr:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
        else:
            zero.append(i)
    print(len(pos)/len(arr))
    print(len(neg)/len(arr))
    print(len(zero)/len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
