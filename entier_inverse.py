# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 00:40:15 2021

@author: haihem
"""

def reverse_int(integer):
    sign = integer // abs(integer) # signe de l'entier (+ ou -)
    return int(str(abs(integer))[::-1])*sign
 
# Afficher les résultats de notre fonction pour 2020 et -9430
print(reverse_int(2020))
print(reverse_int(-9430))

print(reverse_int(6523))
print(reverse_int(-6523))