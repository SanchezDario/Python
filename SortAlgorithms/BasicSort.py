from algo1 import *
from linkedlist import *

class LinkedList:
    head = None

l = LinkedList()
add(l,1)
add(l,13)
add(l,23)
add(l,34)
add(l,45)
add(l,62)
add(l,64)
add(l,78)
add(l,99)

imprimirLista(l)

#BubbleSort(l)
#SelectionSort(l)
InsertionSort(l)

imprimirLista(l)

def imprimirLista(l):
    long = length(l)
    current = l.head
    print("")
    for i in range(long):
        print(current.value,end=" ")
        current = current.nextNode
    print("")

def BubbleSort(l):
    long = length(l)
    current = l.head
    dcurrent = l.head.nextNode
    c = long-1
    for i in range(long-1):
        for j in range(c):
            if current.value > dcurrent.value:
                v1 = current.value
                v2 = dcurrent.value
                current.value = v2
                dcurrent.value = v1
            current = current.nextNode
            dcurrent = dcurrent.nextNode
        c = c-1
        current = l.head
        dcurrent = l.head.nextNode
    return l


def SelectionSort(l):
    long = length(l)
    current = l.head
    dcurrent = l.head.nextNode
    fcurrent = l.head.nextNode
    ecurrent = l.head
    v = current.value
    c = 1
    b = 0
    for i in range(long-2):
        for j in range(c,long):
            if dcurrent.value < v:
                v = dcurrent.value
                b += 1
            dcurrent = dcurrent.nextNode
        if b > 0:
            tope = search(l,v)
            for k in range(tope-1):
                ecurrent = ecurrent.nextNode
            ecurrent.value = current.value
            current.value = v
        ecurrent = l.head
        fcurrent = fcurrent.nextNode
        dcurrent = fcurrent
        v = fcurrent.value
        b = 0
        c += 1
    return l


def InsertionSort(l):
    long = length(l)
    current = l.head
    dcurrent = l.head.nextNode
    c = 1
    for i in range(long-1):
        for j in range(c-1):
            if current.value > dcurrent.value:
                v1 = current.value
                v2 = dcurrent.value
                current.value = v2
                dcurrent.value = v1
            current = current.nextNode
        c+=1
        dcurrent = dcurrent.nextNode
        current = l.head
    return l