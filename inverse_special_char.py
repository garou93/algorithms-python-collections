# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:18:50 2021

@author: haihem
"""

def inverse_special_char(word):
 
    word1 = [x for x in word] # Créons une liste des caractères de word
    index = -1
 
    # Parcourons à partir du dernier index jusqu'à l'index de milieu
    for i in range(len(word1)-1, int(len(word1)/2), -1):
        # Vérifier si notre caractère est alphanumérique ou non
        if word1[i].isalnum():
            temp = word1[i]
            while True:
                index += 1
                if word1[index].isalnum():
                    word1[i] = word1[index]
                    word1[index] = temp
                    break
     
    inverse_special_char = '' # Initialisons notre nouveau mot à vide
    # Construisons notre nouveau à partir de word1
    for char in word1:
        inverse_special_char += char # Concaténons chaque caractère de word1
     
    return inverse_special_char
 
word = "Alo*etui@l)ios82?"
# expected : "28s*oili@u)teolA?"
print(inverse_special_char(word))