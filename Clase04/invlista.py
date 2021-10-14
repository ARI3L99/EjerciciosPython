def invertir_lista(lista):
    i = len(lista)-1
    nuevaLista = []
    while i>=0:
        nuevaLista.append(lista[i])
        i-= 1
    return nuevaLista
print("lista normal", [1,2,3,4,5])
print("lista invertida :",invertir_lista([1,2,3,4,5]))
#[5, 4, 3, 2, 1]
print("lista normal", ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
print("lista invertida :",invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))
#['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']