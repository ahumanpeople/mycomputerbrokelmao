"""
File: minPriorityQueue.py
Author: Jose Barrios

Resources:

    - https://www.w3schools.com/python/python_reference.asp

"""

import math
import sys

""" - - - - - - - - - - - - Exercise 2 - - - - - - - - - - - - """

class MinPriorityQueue:
	
	def __init__(self):
		
		self.arr = []
		self.heapSize = 0
		
	def size(self):
		
		return self.heapSize
		
	def getMin(self):
	
		pass
		
	def extractMin(self):
	
		pass
		
	def insert(self, x):
	
		self.heapSize += 1
		self.arr[self.heapSize] = int(sys.maxsize)
		i = self.heapSize
		if x <= A[i]:
			
			A[i] = key
			while i > 1 and A[math.floor(i/2)] > A[i]:
		
				A[i], A[math.floor(i/2)] = A[math.floor(i/2)], A[i]
				i = math.floor(i/2)
