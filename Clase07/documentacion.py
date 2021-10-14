#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 16:18:31 2021

@author: ariel
"""
def valor_absoluto(n):
    '''
    
    se le debe pasar un valor de tipo numerico positivo o negativo 
    y lo devolvera en valor absoluto
    ----------
    n : float,int

    Returns
    -------
    retorna un numero en valor absoluto

    '''
    if n >= 0:
        return n
    else:
        return -n
    
    
def suma_pares(l):
    '''
    

    Debe pasarse una lista con numeros y retornara la suma de los pares
    ----------
    l : una lista con numeros

    Returns
    -------
    res : suma de todos los pares que se encuentren en la lista

    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

def veces(a, b):
    '''
    

    se pasan dos valores numericos y se hará una multiplicacion sumando 
    b veces el valor de a 
    ----------
    a : float,int
    b : int (positivo)

    Returns
    -------
    res : retorna a multiplicado por b 

    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res


def collatz(n):
    '''
    se aplica la conjetura de collatz
    Se le pasa un valor numerico positivo, si es par se divide en 2
    si es impar se multiplica por 3 y se le suma 1 
    termina cuando queda en 1 para no entrar en el bucle cerrado de 4,2,1...
    ----------
    n : int positivo.

    Returns
    -------
    res : retorna la cantidad de veces que se repitio el ciclo

    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res

