# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:29:09 2021

@author: haihem
"""

def gcd_extended(a, b):
    """
    Soit ax + by = gcd(a, b) avec a = 45 et b = 60.
    Pour calculer le gcd(a, b), on décompose a et b avec des nombres premiers :
            a = 3 * 3 * 5
            b = 2 * 2 * 3 * 5
    Ainsi, on aura :
            gcd(a, b) = 3 * 5 = 15
            x = -1
            y = 1
    """
 
    # Si l'un des deux entiers est nul, on retourne la valeur de l'autre, 0 et 1
    if a == 0:
        return b, 0, 1 # x = 0 et y = 1
     
    # On calcule par récursivité le gcd et les variables permettant de trouver x et y
    gcd, x1, y1 = gcd_extended(b%a, a)
 
    # On reconstitue x et y avec les valeurs produites par récursivité
    x = y1 - (b//a) * x1
    y = x1
 
    # On retourne enfin les solutions de notre équation ax + by = gcd(a, b)
    return gcd, x, y
 
print(gcd_extended(45, 60))