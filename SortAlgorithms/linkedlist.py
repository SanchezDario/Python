class node:
  value = None
  nextNode = None

class LinkedList:
  head = None

#Agrega un nuevo nodo al principio de la lista
def add(L,element):
  nuevo = node()
  if L.head == None:
    L.head = nuevo
    nuevo.value = element
  else:
    nuevo.nextNode = L.head
    L.head = nuevo
    nuevo.value = element 

#Busca un elemento en la lista y devuelve la posicion
def search(L,element):
  current=L.head
  c=0
  position=0
  while current != None:
    if current.value == element:
      c +=1
      break
    else:
      position +=1
    current = current.nextNode
  if c > 0:
    return position
  else:
    return None

#Inserta un nodo con determinado valor en la lista
def insert(l,element,position):
  nuevo = node()
  current = l.head
  largo = length(l)
  if position <= largo: 
    if position == 0:
      nuevo.nextNode = l.head
      l.head = nuevo
      nuevo.value = element
      return position 
    else:
      for i in range (0,position-1):
        current = current.nextNode
      if current != None:
        nuevo.nextNode = current.nextNode
        current.nextNode = nuevo 
        nuevo.value = element
        return position
  else:
    return None         

#Elimina los nodos que contengan el elemento 
def delete(L,element):
  current = L.head
  position = 0
  c = 0
  while current != None:
    position += 1
    if current.value == element:
      c += 1
      break
    current = current.nextNode
  if c > 0:
    if position==1:
      L.head = L.head.nextNode
    else:
      current = L.head  
      for i in range (1,position-1):
        current = current.nextNode
      current.nextNode = current.nextNode.nextNode
      return position  
  else:
    return None 

#Devuelve la cantidad de nodos en la lista
def length(L):
  current=L.head
  c = 0
  while current != None:
    c += 1
    current = current.nextNode
  return c

#Access: Accede al valor del nodo solicitado
def access(L,position):
  largo = length(L)
  current = L.head
  if position < largo:
    for i in range (0,position):
      current = current.nextNode
    return current.value  
  else:
    return None

#Modifica el elemento del nodo indica 
def update(L,element,position):
  current = L.head
  largo = length(L)
  if position < largo:
    for i in range (0,position):
      current = current.nextNode
    current.value = element
    return position  
  else:
    return None
