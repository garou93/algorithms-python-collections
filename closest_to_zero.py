# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 21:24:28 2021

@author: haihem
"""
import sys
import math
from contextlib import redirect_stdout


def compute_closest_to_zero(ts):
    l=len(ts)
    if l == 0:
        return 0
    if l > 0 and l <= 1000:  
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
        a=abs(ts[min(range(len(ts)), key = lambda i: abs(ts[i]-0))])
        if a in ts:
            return a
        else :
            return -a
    


# Ignore and do not change the code below
def main():
    # pylint: disable = C, W
    n = int(input())
    ts = [int(i) for i in input().split()]
    with redirect_stdout(sys.stderr):
        solution = compute_closest_to_zero(ts)
    print(solution)


if __name__ == "__main__":
    main()
