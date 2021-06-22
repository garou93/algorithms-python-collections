# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 14:58:34 2021

@author: haihem
"""

# Python3 implementation of the approach

# Function to return the maximum length
# of the required sub-array
def maxLength(arr, n):
	maxLen = 0

	# For the first consecutive
	# pair of elements
	i = 0
	j = i + 1

	# While a consecutive pair
	# can be selected
	while (j < n):

		# If current pair forms a
		# valid sub-array
		if (arr[i] != arr[j]):

			# 2 is the length of the
			# current sub-array
			maxLen = max(maxLen, 2)

			# To extend the sub-array both ways
			l = i - 1
			r = j + 1

			# While elements at indices l and r
			# are part of a valid sub-array
			while (l >= 0 and r < n and arr[l] == arr[i]
				and arr[r] == arr[j]):
				l-= 1
				r+= 1

			# Update the maximum length so far
			maxLen = max(maxLen, 2 * (r - j))

		# Select the next consecutive pair
		i+= 1
		j = i + 1

	# Return the maximum length
	return maxLen

# Driver code

arr =[1, 1, 1, 0, 0, 1, 1]
n = len(arr)

print(maxLength(arr, n))
