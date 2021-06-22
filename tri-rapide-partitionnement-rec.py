# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:02:13 2021

@author: haihem
"""
def partition(L,debut,fin):
    pivot = L[fin]
    i = debut
    j = debut
    while j < fin:
        if L[j] <= pivot:
            L[i],L[j] = L[j],L[i]
            i += 1
        j += 1
    L[fin],L[i] = L[i],L[fin]
    return i
               
def tri_partition_recursif(L,debut,fin):
    if debut < fin:
        i = partition(L,debut,fin)
        tri_partition_recursif(L,debut,i-1)
        tri_partition_recursif(L,i+1,fin)
                   

#Voici la fonction de démarrage :

def tri_partition(liste):
    L = list(liste)
    tri_partition_recursif(L,0,len(L)-1)
    return L
                   

#Voici un exemple :

liste = []
for k in range(11):
    liste.append(random.randint(0,40))
liste_triee = tri_partition(liste)
                   

print(liste)
#--> [16, 23, 5, 23, 29, 9, 28, 13, 4, 27, 20]

print(liste_triee)