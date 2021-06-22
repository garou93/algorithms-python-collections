# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 15:09:13 2021

@author: haihem
"""
from __future__ import print_function

# Python implementation of the approach

# Utility function to print the contents
# of the ArrayList
def printArrayList(arrL):
	arrL.remove("")
	print(*arrL, sep = " ")

# Function to returns the arraylist which contains
# all the sub-sequences of str
def getSequence(Str):

	# If string is empty
	if(len(Str) == 0):

		# Return an empty arraylist
		empty = []
		empty.append("")
		return empty

	# Take first character of str
	ch = Str[0]

	# Take sub-string starting from the
	# second character
	subStr = Str[1:]

	# Recurvise call for all the sub-sequences
	# starting from the second character
	subSequences = getSequence(subStr)

	# Add first character from str in the beginning
	# of every character from the sub-sequences
	# and then store it into the resultant arraylist
	res = []

	for val in subSequences:
		res.append(val)
		res.append(ch + val)

	# Return the resultant arraylist
	return res

# Driver code
Str = "geek"
printArrayList(getSequence(Str))
