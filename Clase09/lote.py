#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 07:28:44 2021

@author: ariel
"""

class Lote:
    def __init__(self,n,c,p):
        self.nombre = n
        self.cajones = c
        self.precio = p
        
    def costo(self):
        return self.cajones * self.precio
    def vender(self, vender):
        self.cajones -= vender
        return self.cajones
    def __repr__(self):
        return f'Lote({self.nombre},{self.cajones},{self.precio})'
