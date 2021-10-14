def propagar(lista): #la función debe propagar los 1 siempre que haya 0 al lado
                    #e ignorar los -1
   
    j = 0
    while j < len(lista): # recorre la lista
        
        if lista[j] == 1: #busca algun 1
            i = j #iguala i a la posición que quedó j
            e = j #iguala e a la posición de j
            while i >= 0: #while que recorre la lista a partir de la posición
                          #donde se encontraba el 1 hacia atras 
                if lista[i] == 0: #comprueba que la posición actual sea 0
                    lista[i] = 1 #si se encuentra con un 0 lo convierte en 1
                if lista[i] != 0 and lista[i] != 1: 
                    #comprueba si se encuentra con algo distinto a 0 o 1
                    break #si es así se corta el bucle
                i-=1
            while e < len(lista): #while que recorre la lista hacia adelante
                if lista[e] == 0: #comprueba que se encuentre un 0 en la posición
                    lista[e] = 1 #convierte el 0 en 1
                if lista[e] != 0 and lista[e] != 1: 
                    #comprueba si se encuentra con algo distinto a 0 o 1
                    break #termina el bucle
                e+=1
        j+=1
    return lista #retorna la lista modificada

print(propagar([ 0, 0, 0, 1, 0, 0])) 
#[1, 1, 1, 1, 1, 1]
print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])) 
#[0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]