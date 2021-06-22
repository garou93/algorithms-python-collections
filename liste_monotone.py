# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:29:33 2021

@author: haihem
"""

def monotonic_array(nums): 
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) 
            or
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)))
 
A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]
 
print(monotonic_array(A)) 
print(monotonic_array(B)) 
print(monotonic_array(C)) 