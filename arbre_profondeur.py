# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:56:11 2021

@author: haihem
"""

# Créons une classe pour ajouter un noeud dans notre arbre
class newNode():
    # Constructeur de la classe
    def __init__(self, node):
        self.node = node
        self.left = self.right = None
 
# Fonction d'affichage de notre arbre
def print_tree(root):
    if root :
        print_tree(root.left)
        print(root.node, end=" ")
        print_tree(root.right)
 
def remove_leafs(root, k):
    # Fonction de suppression des feuilles dont la profondeur est inférieure à k
    def remove_leafs_from_short_depth(root, depth, k):
        # On vérifie que nous avons vraiment un newNode en entrée sinon on ne retourne rien.
        if root == None:
            return None
         
        # Nous parcourons notre arbre.
        # On descend de la racine aux nœuds descendants 
        root.left = remove_leafs_from_short_depth(root.left, depth+1, k)
        root.right = remove_leafs_from_short_depth(root.right, depth+1, k)
 
        if root.left == None and root.right == None and depth < k:
           return None
     
        return root
     
    # Notre fonction finale utilise la fonction remove_leafs_from_short_depth
    new_tree = remove_leafs_from_short_depth(root, 1, k)
    return new_tree
 
# expected_binary_tree = {1:[2, 3], 2:[4], 3:[5, 6], 4:[7, 8], 5:[9], 6:[], \
#                           7:[10], 8:[], 9:[11, 12], 10:[], 11:[], 12:[]}
 
# Construisons notre arbre ci-dessus
root = newNode(1)
root.left, root.right = newNode(2), newNode(3)
root.left.left = newNode(4)
root.right.left, root.right.right = newNode(5), newNode(6)
root.left.left.left, root.left.left.right = newNode(7), newNode(8)
root.right.left.right = newNode(9)
root.left.left.left.left = newNode(10)
root.right.left.right.left, root.right.left.right.right = newNode(11), newNode(12)
 
# Affichons notre arbre avant suppression
print("Notre arbre avant suppression")
print_tree(root)
print()
print('-'*100)
# Supprimons les feuilles de longueur inférieur à 4
new_tree = remove_leafs(root, 4)
# Affichons notre arbre après suppression
print("Nouvel arbre obtenu")
print_tree(new_tree)