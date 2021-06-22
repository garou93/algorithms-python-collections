# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:50:08 2021

@author: haihem
"""

import random


def tri_insertion(A):
    N = len(A)
    for i in range(1,N):
        print(A)
        cle = A[i]
        j = i-1
        while j>=0 and A[j] > cle:
            A[j+1] = A[j] # decalage
            j = j-1
        A[j+1] = cle


liste = []
for k in range(10):
    liste.append(random.randint(0,20))
tri_insertion(liste)


print(liste)


#print(liste_triee)