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
		
		l, r, smallest = 2*i, (2*i)+1, i
		
		if l <= self.heapSize and A[l] < A[i]: smallest = l
		elif r <= self.heapSize and A[r] < A[i]: smallest = r
			
		if smallest != i:
			
			A[i], A[smallest] = A[smallest], A[i]
			self.minHeapify(smallest)
		
	def extractMin(self):
	
		if self.heapSize >= 1:
			
			minimum = self.arr[1]
			self.arr[1] = self.arr[self.heapSize]
			self.heapSize -= 1
			self.minHeapify(1)
			return minimum
		
		else:
			
			print("Queue is empty.")
			return None
		
	def insert(self, x):
	
		self.heapSize += 1
		i, self.arr[self.heapSize] = self.heapSize, key
		while i > 1 and self.arr[math.floor(i/2)] > self.arr[i]:
		
			self.arr[i], self.arr[math.floor(i/2)] = self.arr[math.floor(i/2)], self.arr[i]
			i = math.floor(i/2)
			
	def __str__(self):
		
		return self.arr
			
testQueue = MinPriorityQueue()
testQueue.insert(6)
testQueue.insert(7)
testQueue.insert(12)
testQueue.insert(10)
testQueue.insert(17)
testQueue.insert(15)
print(testQueue)
