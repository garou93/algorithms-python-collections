# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 00:57:25 2021

@author: haihem
"""

# La fonction de calcul d'un nombre de Fibonacci
def fibonacci(n):
   if n < 0 :
     print("N doit être supérieur ou égal à 0")
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))
 
# La fonction de calcul des nombres de Fibonacci compris entre 2 entiers positifs
def print_fibo_number(int_a, int_b):
  n = 0
  valueList = []
  while fibonacci(n) <= max (int_a, int_b) :
    valueList.append(fibonacci(n))
    n+=1
  return [i for i in valueList if min(int_a, int_b) <= i <= max (int_a, int_b)]
 
print_fibo_number(10, 22)