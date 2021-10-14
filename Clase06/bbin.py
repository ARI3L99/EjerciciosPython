def donde_insertar(lista, x):
    pos = len(lista) # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if izq == medio and lista[der] != x:
        pos = izq
   
    return pos

...
...
...

def insertar(lista,x):
    pos = -1 # inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if izq == medio and lista[der] != x: #comprueba que izq sea igual a medio y lista[der] distinto a x
        pos = izq #pasa el valor de izq a pos
        if pos < len(lista): #si la posición es menor a la longitud de lista
            lista.insert(pos, x) #usará insert
    if pos == -1: # si la posición es igual a -1, por lo tanto no se encontró el valor y es mayor a los de la lista
        lista.append(x) #añadira un elemento usando append
    return lista