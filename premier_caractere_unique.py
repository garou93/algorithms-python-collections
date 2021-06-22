# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:08:06 2021

@author: haihem
"""

import collections
 
def first_unique_character(word):
    word = word.lower() # Mettre le mot en minuscule
    # Construire une correspondance entre les lettres et leurs occurrences dans le mot
    count = collections.Counter(word) # retourne un dictionnaire
 
    for idx, ch in enumerate(count):
        if count[ch] == 1:
            return (ch, idx)
      
    return -1
 
print(first_unique_character('coronavirus'))
print(first_unique_character('Europe'))