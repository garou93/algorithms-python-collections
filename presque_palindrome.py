# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:20:31 2021

@author: haihem
"""

def almost_palindromic(word):
    word = word.lower() # mettre le mot en minuscule
    for i in range(len(word)):
        t = word[:i] + word[i+1:]
        if t == t[::-1]:
            return (word[i], True, t) # retourne la lettre à supprimer, True et le palindrome trouvé
 
    return word == word[::-1] # retourne True ou False
 
print(almost_palindromic('katyak'))
print(almost_palindromic('Hannah'))