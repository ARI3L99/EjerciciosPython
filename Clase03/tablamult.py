#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 16:34:48 2021

@author: ariel
"""
n = 0
tablas = []
m = 0
for i in range(10):
    n = 0
    tabla = []
    for i in range(9):
        
        
        n += m
        tabla.append(n)
    tablas.append(tabla)
    m += +1
    
num=0
cero = 0
numeros = (0,1,2,3,4,5,6,7,8,9)

#Imprimir por pantalla las tablas del 0 al 9
print(f"{numeros[0]:>8}{numeros[1]:>6}{numeros[2]:>6}{numeros[3]:>6}{numeros[4]:>6}{numeros[5]:>6}{numeros[6]:>6}{numeros[7]:>6}{numeros[8]:>6}{numeros[9]:>6}")
print("-"*62)
for a, b, c, d, e, f, g,h,i in tablas:
    
    print(f"{num}: {cero:>5d} {a:>5d} {b:>5d} {c:>5d} {d:>5d} {e:>5d} {f:>5d} {g:>5d} {h:>5d} {i:>5d}")
    num+=1