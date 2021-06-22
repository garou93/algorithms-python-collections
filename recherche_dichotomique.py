# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:04:36 2021

@author: haihem
"""
#rech dicothomique, liste trièe
def dicho(list_, element):
    length = len(list_) # Longueur de la liste
    # Si la liste est vide, on retourne False
    if length == 0: 
        return False
    mid = int(length/2) # L'index de notre élément du milieu
    # Si l'élément recherché est celui du milieu, on le retourne directement
    if list_[mid] == element: 
        return list_[mid]
    # Si l'élément est inférieur, on recommence sur la partie gauche
    if element < list_[mid]: 
        return dicho(list_[:mid], element) 
    # Si l'élément est supérieur, on recommence sur la partie droite
    else: 
        return dicho(list_[mid+1:], element)
 
A = [1,2,3,5,8,9]
print(dicho(A, 5))
print(dicho(A, 10))