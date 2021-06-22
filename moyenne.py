# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 13:47:08 2021

@author: haihem
"""

from functools import reduce
dotations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
def Moyenne(l):
	myn = reduce(lambda x, y: x + y, l) / len(l)
	return myn
moyenne = Moyenne(dotations)
print("La moyenne des dotations est :", moyenne)