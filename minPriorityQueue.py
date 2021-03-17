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
		i, self.arr[self.heapSize] = self.heapSize, key
		while i > 1 and self.arr[math.floor(i/2)] > self.arr[i]:
		
			self.arr[i], self.arr[math.floor(i/2)] = self.arr[math.floor(i/2)], self.arr[i]
			i = math.floor(i/2)
