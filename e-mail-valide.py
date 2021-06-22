# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:37:04 2021

@author: haihem
"""

from re import match
 
def is_email(email: str) -> str:
    # Écrivons l'expression régulière d'une adresse email selon RFC 5322
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
 
    # Vérifions que notre adresse email respecte ou non l'expression régulière
    valid_email = match(email_regex, email)
    if valid_email is None:
        return False
    else:
        return valid_email[0]
 
A = "prenom.nom@contact.fr"
B = "123prenom,nom@contact.org.fr"
print(is_email(A))
print(is_email(B))