#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fileparse import parse_csv


def leer_camion(nombre_archivo): #Funcion que lee y guarda los datos dentro de una lista
   
    camion = parse_csv(nombre_archivo,types=[str,int,float]) #Llama al metod Parse
  
    return camion

...
...
...

def leer_precios(nombre_archivo): #Funcion que lee y guarda los datos en un diccionario
    precios = parse_csv(nombre_archivo,types=[str,float],has_headers = False) #Llama al metodo Parse
 
    return precios

...
...
...

def hacer_informe(camion,precios): #Función para crear un informe 3.13
    n = 0
    informe = []
    for i in camion:
         a = precios[n][1]
         b = camion[n]["precio"]
         cambio = a-b
         informe.append((camion[n]["nombre"],camion[n]["cajones"], b, cambio))
         n += 1  
    return informe

...
...
...

def imprimir_informe(informe):
    encabezados = ("Nombre", "Cajones", "Precio", "Cambio")
    print(f"{encabezados[0]:>10s} {encabezados[1]:>10s} {encabezados[2]:>10s} {encabezados[3]:>10s}")
    print("-"*10,"-"*10,"-"*10,"-"*10)
    for nombre, cajones, precio, cambio in informe: # Imprimir tabla con formato 3.14
        print(f"{nombre:>10s} {cajones:>10d} {'$' + str(precio):>10s} {cambio:>10.02f}") 
...
...
...

def informe_camion(nombre_archivo_camion,nombre_archivo_precios):
    camion= leer_camion(nombre_archivo_camion) #Leer los datos de camion.csv
    precios = leer_precios(nombre_archivo_precios) #Leer los datos de precios.csv
    informe = hacer_informe(camion,precios) #llama al metodo para crear un informe
    imprimir_informe(informe) #imprime el informe con formato

...
...
...
'''
informe_camion("../Data/camion.csv", "../Data/precios.csv")
files = ['../Data/camion.csv', '../Data/camion2.csv']
for name in files:
        print(f'{name:-^43s}')
        informe_camion(name, '../Data/precios.csv')
        print()
'''
def f_principal(lista):
    nombre_archivo_camion = lista[1]
    nombre_archivo_precios = lista[2]
    informe_camion(nombre_archivo_camion, nombre_archivo_precios)
if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    