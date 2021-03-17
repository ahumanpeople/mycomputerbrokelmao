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
	
		return self.arr[1]
	
	def minHeapify(self, i):
		
		l, r = self.arr[2*i], self.arr[(2*i)+1]
		if l <= self.heapSize:
			
			pass
		
	def extractMin(self):
	
		if self.heapSize >= 1:
			
			min = self.arr[1]
			self.arr[1] = self.arr[self.heapSize]
			self.heapSize -= 1
			self.minHeapify(1)
			return min
		
		else:
			
			print("Queue is empty.")
			return None
		
	def insert(self, x):
	
		self.heapSize += 1
		i, self.arr[self.heapSize] = self.heapSize, key
		while i > 1 and self.arr[math.floor(i/2)] > self.arr[i]:
		
			self.arr[i], self.arr[math.floor(i/2)] = self.arr[math.floor(i/2)], self.arr[i]
			i = math.floor(i/2)
