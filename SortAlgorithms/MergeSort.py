from linkedlist import *

def mergeSort(l):
	mergeSortRecursive(l,0,length(l)-1)

def mergeSortRecursive(l,first,last):
	if first < last:
		middle = (first + last) // 2
		mergeSortRecursive(l,first,middle)
		mergeSortRecursive(l,middle+1,last)
		merge(l,first,middle+1,last+1)

def merge(l,first,middle,last):
	middleLeft = sub(l,first,middle)
	middleRight = sub(l,middle,last)
	i = 0
	j = 0
	for k in range(first,last):
		if not access(middleLeft, i):
			update(l,access(middleRight,j),k)
			j = j + 1
		elif not access(middleRight,j):
			update(l,access(middleLeft,i),k)
			i = i + 1
		elif access(middleLeft, i) <= access(middleRight,j):
			update(l,access(middleLeft,i),k)
			i = i + 1
		else:
			update(l,access(middleRight,j),k)
			j = j + 1

def sub(L,start,end):
	l2 = LinkedList()	#nueva lista
	currentNode = L.head
	if start <= length(L):
		for i in range(0, start):
			currentNode = currentNode.nextNode
		add(l2, currentNode.value)
	if end <= length(L):
		for j in range(start + 1, end):
			currentNode = currentNode.nextNode
			insert(l2, currentNode.value, length(l2))
	return l2




