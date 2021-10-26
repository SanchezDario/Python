word = input("Escribe la palabra: ")
longg = len(word)
life = int(input("Numero de vidas: "))
hits = 0

v1 = []; v2 = []; v3 = []

#v3 es el vector para mostrar en pantalla
for i in range(longg):
    v3.append("_")
#print(l3)

#v1 es para la palabra
for i in word:
    v1.append(i)
#Por si hay espacios
for i in range(longg):
    if v1[i] == " ":
        hits+=1

while life > 0 and hits < longg:
    entry = input("Elige una letra: ")
    for i in range(longg):
        if v1[i] == entry:
            v2.append(entry)
            validator = True
            hits+=1
            v3[i] = entry
    if validator == False:
        life-=1
    validator = False
    print(v3)
    if hits == longg:
        print("Ganaste")
    elif life == 0:
        print("Perdiste")
    
        
        

