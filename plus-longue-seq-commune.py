# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 02:00:33 2021

@author: haihem
"""

def lcs(word1, word2):
    i = 0
    so_far = ""
    current = ""
    # On parcours la première chaine de caractères
    while i < len(word1): 
        # Si le i-ème caractère est dans 'word2' ...
        if word1[i] in word2: 
            current = word1[i]
            # ... on teste qu'avec les caractères qui suivent,
            # le ils forment une chaine qui apparait aussi dans word2
            for j in range(i+1, len(word1)): 
                if word1[i:j] in word2: 
                    current = word1[i:j]
                else:
                    # Quand on atteind un caractère qui, avec les caractères
                    # précédents ne forment pas une chaine qui est dans word2,
                    # on continue d'itérer sur word1 à partir de ce caractère
                    i = j - 1
                    break
            # Si la dernière chaine detectée est plus longue que la plus
            # longue chaine qui était detectée jusque là, on actualise
            # cette dernière
            if len(current)> len(so_far): 
                so_far = current
            if len(so_far) > len(word1)-i:
                # Si la séquence la plus longue trouvée jusque là est plus
                # longue que la suite de word1, on peut sortir de la boucle
                # ça ne sert à rien de continuer vu que 'so_far' est 
                # forcément la plus grande chaine en commun
                break
        else:
            # Si le i-ème caractère de 'word1' n'est pas dans 'word2'
            # on passe au suivant
            i += 1
         
    return so_far
 
A = 'ledatascientist'; B = 'dicodata'; C = 'datascience';  D = 'okihqgahye'
print(lcs(A,C))
print(lcs(A,B))
print(lcs(A,D))