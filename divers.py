# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 21:43:21 2021

@author: haihem
"""

x='my name is abc'
print(x.split())


lst = [237, 72, -18, 237, 236, 237,-5, 5, -158, -273, -78, 492, 243]

fst=[-273, -273 ,-273 ,-273]
tab=[-15, -7, -9, -14, -12]
 
p=abs(min((abs(x), x) for x in lst)[1])

#print(p)

p1=abs(min((abs(x), x) for x in fst)[1])


#print(p1)


p2=abs(min((abs(x), x) for x in tab)[1])

print(p2)

print("lindex")
p22=min((abs(x), x) for x in tab)[1]
print([i for i, j in enumerate(tab) if j == p2])

#################
a = [3,8,3,5,9,1,4]
m = max(a)
print([i for i, j in enumerate(a) if j == m])


########################
#lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]
print(abs(lst[min(range(len(lst)), key = lambda i: abs(lst[i]-0))]))

clos=abs(lst[min(range(len(lst)), key = lambda i: abs(lst[i]-0))])
print(clos)
if clos in lst:
    
