#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 22:06:50 2021

@author: ariel
"""

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()


def caminos(cant_caminos,N):
    '''
    se le pasan la cantidad de caminos y el numero de largo 
    devuelve una lista con los caminos que le sean solicitados
    '''
    l = []
    for i in range(cant_caminos):
        l.append(randomwalk(N))
    return l

def mas_se_aleja(lista):
    '''
    
    se le pasa una lista y el nro de largo 
    recorre las listas dentro de la lista y toma el mayor en valor absoluto
    guarda la lista donde encontro el mayor y la retorna

    '''
    mayor = 0
    for i in range(len(lista)):
        
        for j in range(len(lista[i])):  
            if abs(lista[i][j]) > mayor:
                mayor = abs(lista[i][j])
                mas_aleja = lista[i]
    return mas_aleja
            
def menos_se_aleja(lista):
    '''
    

    recibe una lista que contenga listas
    saca el promedio para saber cual es la que menos se alejo en general
    y retorna la lista que menos se alejo del principio

    '''
    #no se si entendi bien este y si habia que hacerlo con el promedio o como
    menor = 1000000
    prom = 0
    for i in range(len(lista)):
        prom = abs(sum(lista[i])/len(lista[i]))
        if prom < menor:
                menor = prom
                menos_aleja = lista[i]
    
    return menos_aleja
    
    


def f_principal(cant_caminos,N):
    '''
    
    Se le pasan dos valores, la cantidad de caminatas al azar y el largo de las caminatas
    crea un grafico con la cantidad de caminatas que se le pida
    crea otro con el camino que mas se alejo del origen
    y crea un ultimo con el que menos se alejo del origen
    
    '''
    
    plt.subplot(2,1,1)
    r = caminos(cant_caminos,N)
    for i in range(cant_caminos):
        plt.plot(r[i])
    plt.title(f"{cant_caminos} caminatas al azar")
    plt.xlabel("Tiempo")
    plt.ylabel("distancia la origen")

    plt.subplot(2,2,3)
    plt.plot(mas_se_aleja(r))
    plt.title("Caminata que más se aleja")
    plt.xlabel("Tiempo")
    plt.ylabel("distancia la origen")
        
        
        
    plt.subplot(2,2,4)
    plt.plot(menos_se_aleja(r))
    plt.title("Caminata que menos se aleja")
    plt.xlabel("Tiempo")
    plt.ylabel("distancia la origen")
    plt.show()
    
    
if __name__ == "__main__":
    import sys
    f_principal(sys.argv)

    