#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 05:01:36 2021

@author: ariel
"""

import random
import matplotlib.pyplot as plt
import time
import timeit as tt
import numpy as np
def generar_lista(N):
    lista = [random.randint(1, 1000) for i in range(N)]
    return lista
...
...
...
...
#ordenamiento por seleccion
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p= buscar_max(lista, 0, n)
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]

        # reducir el segmento en 1
        n = n - 1

    return lista

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    pos_max = a
    for i in range(a + 1, b + 1):
        
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

...
...
...
...

#Ordenamiento por insercion
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
          reubicar(lista, i + 1)

    return lista

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    
    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
    

...
...
...
...

#Ordenamiento por burbujeo   
def ord_burbujeo(lista):
    desorden = True
    iteracion = 0
    while desorden == True:
        desorden = False
        iteracion = iteracion + 1
        for i in range(0, len(lista) - iteracion):
            
            if lista[i] > lista[i + 1]:
                desorden = True
                # Intercambiamos los dos elementos
                lista[i], lista[i + 1] = \
                lista[i + 1],lista[i]
    
    return lista

...
...
...
...

#ordenamiento por mezcla
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva= merge(izq, der)
         
    return lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    
  
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado




def experimento_timeit(Nmax):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica el número de veces que repite el ordenamiento para cada lista.
    """
    listas = []
    for N in range(1, Nmax):
        listas.append(generar_lista(N))
    tiempos_seleccion = []
    tiempos_insercion = []
    tiempos_burbujeo = []
    tiempos_merge = []
    global lista

    for lista in listas:

        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempos_seleccion.append(tt.timeit('ord_seleccion(lista.copy())', number = 1, globals = globals()))
        tiempos_insercion.append(tt.timeit('ord_insercion(lista.copy())', number = 1, globals = globals()))
        tiempos_burbujeo.append(tt.timeit('ord_burbujeo(lista.copy())', number = 1, globals = globals()))
        tiempos_merge.append(tt.timeit('merge_sort(lista.copy())', number = 1, globals = globals()))
        # guardo el resultado
    tiempos_seleccion = np.array(tiempos_seleccion)
    tiempos_insercion = np.array(tiempos_insercion)
    tiempos_burbujeo = np.array(tiempos_burbujeo)
    tiempos_merge = np.array(tiempos_merge)
    # paso los tiempos a arrays
    

    return tiempos_seleccion,tiempos_insercion,tiempos_burbujeo,tiempos_merge


tiempos_seleccion,tiempos_insercion,tiempos_burbujeo,tiempos_merge = experimento_timeit(200)
plt.plot(tiempos_seleccion,"b",tiempos_insercion,"r",tiempos_burbujeo,"g",tiempos_merge, "cyan")
plt.ylabel('Tiempo')
plt.xlabel('Cantidad de elementos')
plt.title('Comparacion de tiempos de metodos de ordenamiento')
plt.show()
