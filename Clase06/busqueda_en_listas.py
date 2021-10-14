def buscar_u_elemento(lista,e):

    pos = -1  #se inicialiaza en -1 porque si no se encuentra el elemento se
              #queda en ese valor
    for i, z in enumerate(lista): #recorre la lista con un enumerador 
        if z == e:  #comprueba si se encuentra el valor
            pos = i #guarda la ultima posicion en la que se encontró
                    #no se usa break porque sino devolvería la primer posición
    return pos

def maximo(lista):
    m = lista[0] #se inicia como el primer elemento de la lista
    for e in lista: #recorre la lista
        if e > m: #si encuentra que el elemento actual es mayor que m
            m = e  #m se hace igual al elemento que era mayor
    return m

def busqueda_lineal_lordenada(lista, e):
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e: #si encontramos e
            pos = i #guarda la posición
            break #sale del ciclo 
        else:
            if z > e:   # si z es mayor que e
                break    # y salimos del ciclo
    return pos
    
'''
print(buscar_u_elemento([1,2,3,2,3,4], 5)) # -1
print(maximo([1,2,7,2,3,4])) # 7
print(maximo([1,2,3,4])) # 4
print(maximo([-5,4])) #4
print(maximo([-5,-4])) #-4
'''