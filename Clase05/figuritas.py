import random
import numpy as np


def crear_album(figus_total): #crea un album con N cantidad de figuritas
    album= np.zeros(figus_total) #se rellena de 0
    return album #retorna el album vacio

def album_incompleto(album): #comprueba que el album este incompleto
    if 0 in album: #comprueba si hay 0 en album
        incompleto = True #retorna true cuando hay 0
    else: 
        incompleto = False #sino retorna false
    return incompleto #devuelve el valor false or true

def comprar_figus(figus_total): #simula comprar figuritas de a 1 
    x = random.randint(1,figus_total) #asigna un valor aleatorio dentro del rango
    return x #retorna el valor que salio

def cuantas_figus(figus_totales): #comprueba cuantas figuritas se debieron comprar para completarlo
    album = crear_album(figus_total) #crea un album vacio 
    count = 0 #contador que se usa para ver cuantas compras se necesitaron
    while(album_incompleto(album)): #bucle que comprueba si esta incompleto
        x = comprar_figus(figus_total) #obtiene un valor al azar
        album[x-1] = 1 #asigna un 1 en la posicion que salio el valor
        count+= 1 # incrementa el contador
    return count # retorna el contador

def experimento_figus(n_repeticiones, figus_total): #simula N veces el llenado del album
    l = [cuantas_figus(figus_total) for x in range(n_repeticiones)] #llena una lista con la cantidad asignada
    prom = np.mean(l) #saca el promedio de cartas compradas para llenar el album
    return prom #retorna el promedio

...
...
...

def comprar_paquete(figus_total,figus_paquete): #simula comprar paquetes de figuras
    paquete = np.random.randint(1,figus_total+1,(figus_paquete)) #llena un array de figuritas
    return paquete #retorna el paquete

def cuantos_paquetes(figus_total,figus_paquete): #comprueba cuantos paquetes se necesitan para llenarlo
    album = crear_album(figus_total) #crea un album vacio con tamaño N
    count = 0 #inicio un contador
    while(album_incompleto(album)): #bucle que comprueba que el album no este completo
        paquete = comprar_paquete(figus_total, figus_paquete) #crea un paquete llamando a la funcion
        for i in paquete-1: #recorre el paquete
            album[i] = 1 #coloca un 1 en la posicion de las figus que salieron
        count+=1 #incrementa contador
    return count #retorna contador
  
def experimento_paquetes(n_repeticiones,figus_total,figus_paquete):  #simula N veces el llenado del album
    l = [cuantos_paquetes(figus_total, figus_paquete) for x in range(n_repeticiones)] 
    #crea una lista con la cantidad de paquetes que se necesitaron para llenar N cantidad de albumes
    prom = np.mean(l) #calcula el promedio de paquetes que se necesitaron
    return prom #retorna el promedio

figus_total = 670 #variable para definir el tamaño del album
n_repeticiones = 100 #cantidad de veces que se repide el llenado
figus_paquete = 5 #tamaño de los paquetes


#Grafico 1
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for i in paquete-1: 
            album[i] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

import matplotlib.pyplot as plt

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()


#Grafico 2
l = [cuantos_paquetes(figus_total, figus_paquete) for x in range(n_repeticiones)] 
n_paquetes_hasta_llenar= np.array(l)
menores_igual = []
for x in l:
    if x < 1150: #el más cercano a 90%
        menores_igual.append(x)
x = len(menores_igual) / len(l)        

print(x) 
print(menores_igual)

plt.hist(l,bins=25)
plt.show()


