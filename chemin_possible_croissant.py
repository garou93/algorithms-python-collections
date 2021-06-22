# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:32:25 2021

@author: haihem
"""

def growing_paths(array1, array2):
 
    # Trier les deux listes de façon croissante
    array1.sort()
    array2.sort()
 
    # Parcourir la première liste
    # et comparer chaque élément avec ceux de la seconde liste
    for number in array1:
        # Initialiser notre liste
        list_ = [number]
        # Si l'élément de la première liste est supérieur au plus grand élément
        # de la seconde liste, l'afficher et passer à l'élément suivant de la première liste
        if number > array2[-1]:
            print(list_)
            continue
        # Comparer l'élément avec chaque élément de la seconde liste
        for i in range(len(array2)):
            # Si l'élément de la seconde liste est plus petit que celui de la première
            # On passe à l'élément suivant de la seconde liste
            if array2[i] < number: continue
            # Si l'élément de la seconde liste est plus grand ou égale que celui de la première
            # On l'ajoute dans la liste et on l'affiche
            else:
                list_.append(array2[i])
                print(list_)
 
A, B = [9, 1, 23, 4], [10, 20, 7]
print(growing_paths(A, B))