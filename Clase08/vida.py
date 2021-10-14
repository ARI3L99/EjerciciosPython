#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 21:37:53 2021

@author: ariel
"""

from datetime import datetime

def vida_en_segundos(fecha_nac):
    '''
    

    Se le debe pasar una cadena con dd/mm/aaaa
    Y devolvera los segundos vividos por la persona
    '''
    fecha_actual = datetime.now() 
    fecha_nac_separada = fecha_nac.split('/')
    nacimiento = datetime(int(fecha_nac_separada[2]),int(fecha_nac_separada[1]),int(fecha_nac_separada[0]))
    segundos_vividos = fecha_actual.timestamp() - nacimiento.timestamp()
    return segundos_vividos

#a = vida_en_segundos('07/02/1999')
#print(f'segundos de vida: {a:0.2f}')