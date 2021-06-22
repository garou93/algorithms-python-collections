# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:42:07 2021

@author: haihem
"""

import string
 
some_string="Maitre Corbeau, sur un arbre perché, tenait en son bec un fromage."
 
# vire la pontuation
some_string = ''.join   ((
                        char for char in some_string
                        if char not in string.punctuation
                        ))
 
maxi = 0
wordMax = ''
for word in some_string.split():
    if len(word) > maxi:
        wordMax = word
        maxi = len(word)
 
print(wordMax)