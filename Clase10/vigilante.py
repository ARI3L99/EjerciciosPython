#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 00:39:30 2021

@author: ariel
"""

# vigilante.py
import os
import time


def vigilar(archivo):
    f = open(archivo)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
    
            
if __name__ == '__main__':
    import informe_final

    camion = informe_final.leer_camion ('../Data/camion.csv')

    for line in vigilar('../Data/mercadolog.csv'):  
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])

        if nombre in camion:    
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')

        