# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:49:42 2021

@author: haihem
"""

def matching_words(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())
     
    return sorted(list(set1^set2)), sorted(list(set1&set2)) # ^ A.symmetric_difference(B), & A.intersection(B)
 
sentence1 = "le blog 'ledatascientist' est le blog français de référence en data science"
sentence2 = "parmi tous les blogs de data science j'aime 'ledatascientist'"
 
print(matching_words(sentence1, sentence2))