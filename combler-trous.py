# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:40:22 2021

@author: haihem
"""

def fill_blanks(nums):
    valid = 0           
    res = []                 
    for i in nums: 
        if i is not None:    
            res.append(i)
            valid = i
        else:
            res.append(valid)
     
    return res
 
array1 = [1, None, 2, 3, None, None, 5, None]
array2 = [None, 7, 0, 0, 8, None, 10, None, None, None]
 
print(fill_blanks(array1))
print(fill_blanks(array2))