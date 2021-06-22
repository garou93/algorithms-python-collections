# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 21:10:38 2021

@author: haihem
"""

a = [3,8,3,5,9,1,104]
#plus grand tableau
#m=max(a)
print(max(a))

#indice plus grand
print([i for i, j in enumerate(a) if j == max(a)])

#cas nombre et string: toujours les lettres plus grands

def find_largest(numbers):
    # Your code goes here
    # Initialize maximum element
    n=7
    max = numbers[0]
        # Traverse array elements from second
    # and compare every element with 
    # current max
    for i in range(1, n):
        if numbers[i] > max:
            max = numbers[i]
    return max

numbers = [200,8,3,5,9,1,104]
print("---------------------------------------------------")
print(find_largest(numbers))