#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fileparse
from lote import Lote
import formato_tabla
from camion import Camion
def leer_camion(filename):
    '''
    Lee un archivo con el contenido de un camión
    y lo devuelve como un objeto Camion.
    '''
    with open(filename):
        
        camiondicts = fileparse.parse_csv(filename,
                                        select = ['nombre', 'cajones', 'precio'],
                                        types = [str, int, float])

    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts]
    return Camion(camion)

...
...
...

def leer_precios(nombre_archivo): #Funcion que lee y guarda los datos en un diccionario
    precios = fileparse.parse_csv(nombre_archivo,types=[str,float],has_headers = False) #Llama al metodo Parse
    
    return precios

...
...
...

def hacer_informe(camion,precios): #Función para crear un informe 3.13
    informe = []
    cambio = 0
    for i in camion:
         a = precios[i.nombre]
         b = i.precio
         cambio = a-b
         informe.append((i.nombre,i.cajones, b, cambio))
           
    return informe

...
...
...

def imprimir_informe(data_informe,formateador):  
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)
...
...
...

def informe_camion(nombre_archivo_camion,nombre_archivo_precios,fmt = "txt"):
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''
    # Leer archivos con datos
    camion = leer_camion(nombre_archivo_camion)
    precios = dict(leer_precios(nombre_archivo_precios))

    # Crear los datos para el informe
    data_informe = hacer_informe(camion, precios)

    # Imprimir el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)
...
...
...


def f_principal(lista):
    nombre_archivo_camion = lista[1]
    nombre_archivo_precios = lista[2]
    
    informe_camion(nombre_archivo_camion, nombre_archivo_precios,lista[3])
   
      
    
if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
   
    