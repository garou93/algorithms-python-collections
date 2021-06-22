# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:00:01 2021

@author: haihem
"""

def partition(L):
    n = len(L)
    pivot = L[n-1]
    i = 0
    j = 0
    while j < n-1:
        if L[j] <= pivot:
            L[i],L[j] = L[j],L[i]
            i += 1
        j += 1
    L[n-1],L[i] = L[i],L[n-1]
                

# tesssssssssssst

liste = []
for k in range(11):
    liste.append(random.randint(0,40)) 
                

print(liste)
#--> [40, 19, 4, 35, 1, 7, 23, 0, 38, 22, 12]

partition(liste)

print(liste)