#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:51:18 2021

@author: ariel
"""

def bbinaria_rec(lista, e):
    """
     recibe una lista ordenada y un numero a buscar dentro de la lista
     devuelve true o false, en caso de encontrarlo o no
    """
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio]==e:
	          res = True
        else:
	          if e<lista[medio]:
	           res= bbinaria_rec(lista[:medio],e)
	          else:
	           res= bbinaria_rec(lista[medio+1:],e)
        # completar

    return res