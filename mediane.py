# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:51:26 2021

@author: haihem
"""

def median(list_):
    # On garde la longueur de la liste pour éviter de l'appeler à chaque fois
    length = len(list_)
    if length % 2 == 0:
        # Si 'length' est pair
        return (list_[int(length/2)] + list_[int((length - 1)/2)])/2
    # Sinon
    return list_[int(length/2)]
 
A = [1, 92, 25, 30, 12, 1]
print(median(A))