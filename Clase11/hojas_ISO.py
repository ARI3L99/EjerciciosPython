#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 01:49:31 2021

@author: ariel
"""

def medidas_hoja_A(n, ancho=1189, largo= 841):
    """
    Se le pasa un numero entero que va a indicar el tamaño de hoja
    que se desea y devuelve una tupla con el ancho y largo en ese orden

    """
    if n == 0:
        return ancho,largo
    else:
        if ancho > largo:    
            ancho= ancho//2
        else:
            largo = largo//2
        
        return medidas_hoja_A(n-1,ancho,largo)
        
        