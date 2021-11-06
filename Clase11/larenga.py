#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 17:02:01 2021

@author: ariel
"""

def triangulo_pascal(n,k):
    """
    recibe una posicion a buscar dentro del triangulo de pascal
    """
    if (n==k or k ==0):
        return 1;
    else:
        return triangulo_pascal(n-1, k-1)+triangulo_pascal(n-1, k)
    