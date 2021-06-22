# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:23:35 2021

@author: haihem
"""

import os
 
def find_files(filename, search_path):
    result = []
 
    # Marche de haut en bas depuis la racine
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
     
    return result
 
! mkdir dir1
! mkdir dir2
! mkdir dir1/dir1_sub1
! mkdir dir2/dir2_sub1
# Creation des fichiers examples
! touch dir1/dir1_sub1/example1
! touch dir2/example1
 
find_files("example1", "/content")