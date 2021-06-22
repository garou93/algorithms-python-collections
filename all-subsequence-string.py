# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 15:03:21 2021

@author: haihem
"""
from __future__ import print_function
# Below is the implementation of the above approach
def printSubsequence(input, output):

	# Base Case
	# if the input is empty print the output string
	if len(input) == 0:
		print(output, end=" ")
		return
	
	# output is passed with including the
	# 1st characther of input string
	printSubsequence(input[1:], output+input[0])

	# output is passed without including the
	# 1st character of input string
	printSubsequence(input[1:], output)


# Driver code
# output is set to null before passing in
# as a parameter
output = ""
input = "abcd"

printSubsequence(input, output)

