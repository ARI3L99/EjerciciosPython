#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 18:41:13 2021

@author: ariel
"""

# camion.py

class Camion:
    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes)

    def precio_total(self):
        return sum(l.costo() for l in self.lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
    
    def __len__(self):
        n = 0
        for l in self.lotes:
            n += 1
        return n
    
    def __getitem__(self,n):
        return self.lotes[n]
    
    def __str__(self):
        mostrar = f'Camion con {len(self)} lotes:'
        for x,i in enumerate(self.lotes):
            mostrar +="\n" + str(self.lotes[x])
        return mostrar
    
    def __repr__(self):
        mostrar = "Camion("
        for x, i in enumerate(self.lotes):
            mostrar += f'{self.lotes[x]},'
        mostrar += ")"
        return mostrar
        
        
            