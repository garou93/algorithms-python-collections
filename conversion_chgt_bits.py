# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:58:07 2021

@author: haihem
"""

def count_flipped(a, b):
  xor = a^b # OU Exclusif
  xor_binary = str(bin(xor)) # Petit tweat pour convertir la valeur en binaire qu'on convertit en string
  return xor_binary.count('1') # On compte le nombre de bits à 1
 
count_flipped(8, 6)