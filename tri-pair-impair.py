# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:47:41 2021

@author: haihem
"""

def even_odd_sort( numberList):
  odd = list() #impair
  even = list() #pair
  for number in numberList :
    if (number % 2) == 0:
      #pair
      even.append(number)
    else:
      odd.append(number)
  even.sort()
  odd.sort(reverse=True)
  return even + odd
 
numbers = [93, 24, 38, 1, 96, 87, 100]
print(even_odd_sort(numbers))