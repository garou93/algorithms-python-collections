# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:48:20 2021

@author: haihem
"""

def check_palindrome(v): 
    reverse = v[::-1]  
  
    if (v == reverse): 
        return True
    return False
  
  
var = input(("Entrez une valeur: "))
if(check_palindrome(var)):
    print("L'entrée est un palindrome")
else:
    print("L'entrée n'est pas un palindrome")