"""
File: minPriorityQueue.py
Author: Jose Barrios
Resources:
	- https://www.w3schools.com/python/python_reference.asp
	- https://www.w3schools.com/python/ref_list_index.asp
"""

import minPriorityQueue

def extractSetNumMaxVals(self, mpqInstance, k):
	
	# makes extraction list from the MPQ list
	extract = mpqInstance.getList()
	# makes insertion list with k spots and a minimum variable
	insert, minimum = [], None
	# for every item in the heap
	for i in range(mpqInstance.getSize()):
		# if there's still more elements to be added into insert based on the k given
		if len(insert) > k:
			# adds the i value from extract into insert
			insert.append(extract[i])
		# else, if the insert list just filled up and this is the first value compared instead of added
		elif len(insert) == k:
			# get the smallest value in insert
			minimum = min(insert)
			# if the minimum is smaller than the current i value in extract
			if minimum < extract[i]:
				# get the index of the minimum, and replace the minimum with the current i value
				insert[insert.index(minimum)] = extract[i]
				# and find the new minimum
				minimum = min(insert)
		# else, if there's already a minimum to compare this i value with
		else:
			# if the minimum is smaller than the current i value in extract
			if minimum < extract[i]:
				# get the index of the minimum, and replace the minimum with the current i value
				insert[insert.index(minimum)] = extract[i]
				# and find the new minimum
				minimum = min(insert)
	# then return max values derived
	return insert
