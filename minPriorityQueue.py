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
		# initializes the list that will contain the heap as well as the heapSize variable
		self.arr = [None]
		self.heapSize = 0
		
	def size(self):
		# returns heapSize
		return self.heapSize
		
	def getMin(self):
		# returns the minimum value, or the root of the heap
		return self.arr[0]
	
	def minHeapify(self, i):
		# set l as i's left child, r as i's right child, and smallest as i
		l, r, smallest = 2*i, (2*i)+1, i
		# if l is in the heap and its value is smaller than i's, then l is the smallest
		if l <= self.heapSize and self.arr[l] < self.arr[i]: smallest = l
		# if r is in the heap and its value is smaller than i's, then r is the smallest
		elif r <= self.heapSize and self.arr[r] < self.arr[i]: smallest = r
		# if the smallest isn't i, but rather one of its children
		if smallest != i:
			# swap the smallest child with i and then continue to min heapify the smallest's subtree
			self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
			self.minHeapify(smallest)
		
	def extractMin(self):
		# if there is a heap
		if self.heapSize >= 1:
			# set the minimum to the minimum variable
			minimum = self.arr[0]
			# set the minimum position equal to the largest value in the heap
			self.arr[0] = self.arr[self.heapSize - 1]
			# shrink the heap by one
			self.heapSize -= 1
			# and then heapify the entire heap, and return the extracted minimum value
			self.minHeapify(0)
			return minimum
		# if there isn't a heap
		else:
			# notify the user and return None
			print("Queue is empty.")
			return None
		
	def insert(self, x):
	    # set i equal to the heapSize, and then increment the heap
	    i = self.heapSize
	    self.heapSize += 1
	    # adds the new key to the heap, removing the None placeholder or elements not in the heap but in the list if needed
	    if self.arr[0] == None: self.arr[0] = x
		elif len(self.arr) >= i: self.arr[i - 1] = x
	    else: self.arr.append(x)
	    # while i is bigger than (or equal to) 1 and i's parent is bigger than i
	    while i >= 1 and self.arr[int(math.floor(i/2))] > self.arr[i]:
	        # swap i and its parent's positions, and then make i equal its parent
	        self.arr[i], self.arr[int(math.floor(i/2))] = self.arr[int(math.floor(i/2))], self.arr[i]
	        i = int(math.floor(i/2))
			
	def __str__(self):
		# makes separate list, since all of the list might not be all of the heap
		printList = []
		for i in range(self.heapSize):
		    # adds elements to the new list while they're still part of the heap
		    printList.append(self.arr[i])
		# then return the separate list
		return str(printList)
			
testQueue = MinPriorityQueue()
testQueue.insert(6)
testQueue.insert(7)
testQueue.insert(15)
testQueue.insert(12)
testQueue.insert(10)
testQueue.insert(17)
print(testQueue)
print("Heap Size: " + str(testQueue.size()))
print("Min Value: " + str(testQueue.getMin()) + "\n")
testQueue.extractMin()
print(testQueue)
print("Heap Size: " + str(testQueue.size()))
print("Min Value: " + str(testQueue.getMin()) + "\n")
testQueue.extractMin()
print(testQueue)
print("Heap Size: " + str(testQueue.size()))
print("Min Value: " + str(testQueue.getMin()) + "\n")
testQueue.extractMin()
print(testQueue)
print("Heap Size: " + str(testQueue.size()))
print("Min Value: " + str(testQueue.getMin()) + "\n")
testQueue.extractMin()
print(testQueue)
print("Heap Size: " + str(testQueue.size()))
print("Min Value: " + str(testQueue.getMin()) + "\n")
testQueue.extractMin()
print(testQueue)
print("Heap Size: " + str(testQueue.size()))
print("Min Value: " + str(testQueue.getMin()) + "\n")
testQueue.extractMin()
print(testQueue)
print("Heap Size: " + str(testQueue.size()))
print("Min Value: " + str(testQueue.getMin()) + "\n")
testQueue.extractMin()
print(testQueue)
print("Heap Size: " + str(testQueue.size()))
print("Min Value: " + str(testQueue.getMin()))
