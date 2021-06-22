# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:56:06 2021

@author: haihem
"""

annee = int(input("Entrez l annee a verifier:"))

if(annee%4==0 and annee%100!=0 or annee%400==0):
    print("L'annee est une annee bissextile!")
else:
    print("L'annee n'est pas une annee bissextile!")