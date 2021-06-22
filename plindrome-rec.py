# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:50:08 2021

@author: haihem
"""

def check_palindrome(v):
    if len(v) < 1:
        return True
    else:
        if v[0] == v[-1]:
            return check_palindrome(v[1:-1])
        else:
            return False

var = input(("Entrez une valeur: "))
if(check_palindrome(var)):
    print("L'entrée est un palindrome")
else:
    print("L'entrée n'est pas un palindrome")