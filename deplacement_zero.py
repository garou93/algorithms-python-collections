# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:34:52 2021

@author: haihem
"""

def move_zeroes(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0) # supprimer le premier zéro de la liste
            nums.append(0) # ajouter 0 à la fin de la liste
 
    return nums
 
array1 = [0, 1, 0, 3, 12]
array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]
 
print(move_zeroes(array1))
print(move_zeroes(array2))