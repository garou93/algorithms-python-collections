# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:54:03 2021

@author: haihem
"""

def prime_numbers(integer):
    prime_nums = []
    for num in range(integer):
        if num > 1: # tous les nombres premiers sont supérieurs strictement à 1
            for i in range(2, num):
                if (num % i) == 0: # le reste de la division d'un nombre premier par un nombre inférieur à lui est toujours différent de 0
                    break
            else:
                prime_nums.append(num)
 
    return prime_nums
 
print(prime_numbers(10))
print(prime_numbers(21))