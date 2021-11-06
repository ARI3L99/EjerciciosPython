#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 17:31:07 2021

@author: ariel
"""
import random
import matplotlib.pyplot as plt

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
    cont = 0
    comparaciones = 0
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p,cont= buscar_max(lista, 0, n)
        comparaciones += cont 
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]

        # reducir el segmento en 1
        n = n - 1

    return comparaciones

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    contar = 0
    pos_max = a
    for i in range(a + 1, b + 1):
        contar+= 1
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max,contar

...
...
...
...

#Ordenamiento por insercion
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    comparaciones = 0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
          comparaciones += reubicar(lista, i + 1)

    return comparaciones

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    comparar = 0
    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        comparar+=1
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
    return comparar

...
...
...
...

#Ordenamiento por burbujeo   
def ord_burbujeo(lista):
    desorden = True
    iteracion = 0
    comparaciones = 0
    pasos= 0
    while desorden == True:
        desorden = False
        iteracion = iteracion + 1
        pasos+=1
        for i in range(0, len(lista) - iteracion):
            comparaciones+=1
            
            if lista[i] > lista[i + 1]:
                desorden = True
                # Intercambiamos los dos elementos
                lista[i], lista[i + 1] = \
                lista[i + 1],lista[i]
    
    return comparaciones

...
...
...
...

#ordenamiento por mezcla
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    contador = 0
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq ,n1= merge_sort(lista[:medio])
        der ,n2= merge_sort(lista[medio:])
        lista_nueva,n= merge(izq, der)
        contador += n+n1+n2 
    return lista_nueva,contador

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    
    n = 0
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        n += 1
        
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado,n
...
...
...
...
#experimento
def experimento(N,K):
    """
    recibe el largo de las listas y la cantidad de veces que se repetira
    devuelve los promedios de las comparaciones de las distintas funciones 
    """
    total_sel = 0
    total_ins = 0
    total_bur = 0
    for i in range(K):
        lista = generar_lista(N)
        lista_seleccion = lista.copy()
        lista_insercion = lista.copy()
        lista_burbujeo = lista.copy()
        seleccion = ord_seleccion(lista_seleccion)
        insercion = ord_insercion(lista_insercion)
        burbujeo = ord_burbujeo(lista_burbujeo)
        total_sel += seleccion  
        total_ins += insercion
        total_bur += burbujeo
    promedio_sel = float(total_sel / K)
    promedio_ins = float(total_ins / K)
    promedio_bur = float(total_bur / K)
    return promedio_sel,promedio_ins,promedio_bur

...
...
...
...

#experimento vector
def experimento_vectores(Nmax):
    """
    recibe la longitud maxima de las listas y se van creando listas de
    longitudes entre 1 y Nmax
    """
    N = 1
    comparaciones_seleccion =[]
    comparaciones_burbujeo= []
    comparaciones_insercion=[]
    comparaciones_mezcla=[]
    aux = []
    while N <= Nmax:
        lista = generar_lista(N)
        lista_sel = lista.copy()
        lista_bur = lista.copy()
        lista_ins = lista.copy()
        lista_mez = lista.copy()
        N+=1
        comparaciones_seleccion.append(ord_seleccion(lista_sel))
        comparaciones_burbujeo.append(ord_burbujeo(lista_bur))
        comparaciones_insercion.append(ord_insercion(lista_ins))
        aux,comp = merge_sort(lista_mez)
        comparaciones_mezcla.append(comp)
        
    return comparaciones_seleccion,comparaciones_insercion,comparaciones_burbujeo,comparaciones_mezcla
...
...
...
...
#grafico

seleccion,insercion,burbujeo,mezcla = experimento_vectores(100)
plt.plot(seleccion,"v",insercion,"b",burbujeo,"g",mezcla,"r")
plt.legend(('Comparaciones seleccion', 'Comparaciones insercion', 'Comparaciones burbujeo', 'comparaciones mezcla'),
           loc='upper left', shadow=True)
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")

plt.show()

