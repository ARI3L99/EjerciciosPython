#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fileparse import parse_csv
import lote
import formato_tabla

def leer_camion(nombre_archivo): 
    '''
    
    Guarda los datos en una lista con objetos Lote 

    '''

    camion = parse_csv(nombre_archivo,select = ['nombre', 'cajones', 'precio'],types=[str,int,float]) #Llama al metod Parse
    camion_lista = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion]
    
    return camion_lista

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
   
    