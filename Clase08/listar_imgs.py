#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 00:04:01 2021

@author: ariel
"""

import os

def archivos_png(directorio):
    lista_png = []
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if '.png' in name:
                print(name)
                lista_png.append(name)
                
        for name in dirs:
            if '.png' in name:
                print(name)
                lista_png.append(name)
                
    return lista_png

if __name__ == "__main__":
    import sys
    archivos_png(sys.argv[1])
    