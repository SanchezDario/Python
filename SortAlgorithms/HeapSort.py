from linkedlist import *

class Bheap:
    bheaplist = LinkedList()

# Verifica si los hijos son menor y acomoda
def shiftUp(Li,poSon):
	while poSon // 2 > 0:   # Se detiene cuando llega a la cabeza
		poFather = poSon // 2
		
		valFather = access(Li,poFather)
		valSon = access(Li,poSon)
		if valFather < valSon:
			update(Li,valSon,poFather)
			update(Li,valFather,poSon)
		poSon = poFather

# Verifica si el padre es mayores y acomoda 	
def shiftDown(L,poFather,currentsize = None):
    if currentsize == None:	#Tamaño de la lista , se puede especificar tamaño 
        currentsize = length(BH.bheaplist)  - 1
    while (poFather * 2) <= currentsize:
        poSon = maxChild(L,poFather,currentsize)
        valFather = access(L,poFather)
        valSon = access(L,poSon)
        if valFather < valSon:
        	update(L,valSon,poFather)
        	update(L,valFather,poSon)
        poFather = poSon

# Devuelve el hijo mas grande
def maxChild(BH,i,currentsize):
    if i * 2 + 1 > currentsize:
        return i * 2
    else:
        if access(BH,i * 2) > access(BH,i * 2 + 1):
            return i * 2 
        else:
            return i * 2 + 1

# Inserta un nodo en la ultima pocicion y reacomoda el hwap  
def insertBH(BH,k):
    pos = length(BH.bheaplist)
    if pos == 0:
        add(H.bheaplist,0)
        pos = pos + 1
    insert(BH.bheaplist,k,pos)
    currentsize = length(BH.bheaplist) - 1
    shiftUp(BH.bheaplist,currentsize)

# Heapyfica una lista 
def heapify(BH,L):
    i = length(L) // 2
    BH.bheaplist.head = L.head 
    add(BH.bheaplist,0)
    while i > 0 :
        shiftDown(BH.bheaplist,i)
        i = i - 1

# HeapMax intercambia el prime valor por el ultimo y acomoda el heap
def hepMax(BH,currentsize):
	valUl = access(BH,currentsize)
	valPr = access(BH,1)
	update(BH,valPr,currentsize)
	update(BH,valUl,1)
	shiftDown(BH,1,currentsize - 1)

# HeapSort
def HeapSort(BH,L):
	heapify(BH,L)