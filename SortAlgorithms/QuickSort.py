from linkedlist import *

def partition(l,start,end):
	p = start
	for i in range(start,end):
		if access(l,i) < access(l,end):		
			mayor = access(l,p)		
			update(l,access(l,i),p)
			update(l,mayor,i)		
			p += 1	
	mayor = access(l,p)
	update(l,access(l,end),p)
	update(l,mayor,end)	
	return p

def Quick_Sort_Recursive(l,start,end):
	if start < end:
		pos = partition(l,start,end)
		Quick_Sort_Recursive(l,start,p-1)
		Quick_Sort_Recursive(l,p+1,end)

def QuickSort(l):
	Quick_Sort_Recursive(l,0,length(l)-1)