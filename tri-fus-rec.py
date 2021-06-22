# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:55:17 2021

@author: haihem
"""

def tri_fusion_recursif(L):
    n = len(L)
    if n > 1:
        p = int(n/2)
        L1 = L[0:p]
        L2 = L[p:n]
        tri_fusion_recursif(L1)
        tri_fusion_recursif(L2)
        L[:] = fusion(L1,L2)
    
def tri_fusion(L):
    M = list(L)
    tri_fusion_recursif(M)
    return M
                  

liste = []
for k in range(11):
    liste.append(random.randint(0,20))
liste_triee = tri_fusion(liste)
print(liste)
#--> [6, 13, 8, 15, 1, 3, 3, 5, 10, 3, 6]

print(liste_triee)
#--> [1, 3, 3, 3, 5, 6, 6, 8, 10, 13, 15]