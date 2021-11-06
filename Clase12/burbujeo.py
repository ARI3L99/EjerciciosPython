#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 02:22:48 2021

@author: ariel
"""

def ord_burbujeo(lista):
    '''
    Recibe una lista numerica y la ordena
    '''
    n = 0
    pasos = 0
    for j in range(len(lista)-1):
     pasos+=1
     for i in range(len(lista)-1):
         n+=1
         print("DEBUG: ",n,pasos, lista)
         if lista[i + 1] < lista[i]: 
             lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista
'''
Tiene complejidad de (n-1)**2
porque tiene que recorrer la longitud -1  de la lista 2 veces 
hace n-1 pasos y (n-1)**2 comprobasiones
'''


def ordenar_burbuja(lista):
    '''
    encontre esta forma de hacerlo mas eficiente la cual en el mejor caso hace solo
    n comprobasiones y no supe calcular la cantidad de comprobaciones pero son muchas menos
    
    '''
    desorden = True
    iteracion = 0
    n = 0
    pasos= 0
    while desorden == True:
        desorden = False
        iteracion = iteracion + 1
        pasos+=1
        for i in range(0, len(lista) - iteracion):
            n+=1
            
            if lista[i] > lista[i + 1]:
                desorden = True
                # Intercambiamos los dos elementos
                lista[i], lista[i + 1] = \
                lista[i + 1],lista[i]
    print("DEBUG: ",n,pasos, lista)