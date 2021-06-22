# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:37:50 2021

@author: haihem
"""

def insertionSort(arr , asc=True):
  for i in range(1, len(arr)): 
    key = arr[i] 
    j = i-1
    while j >= 0 and key < arr[j] : 
      arr[j + 1] = arr[j] 
      j -= 1
      arr[j + 1] = key
  if not asc:
    arr.reverse()
 
arr = [12, 11, 13, 5, 6] 
insertionSort(arr, True) 
for i in range(len(arr)): 
    print ("% d" % arr[i])