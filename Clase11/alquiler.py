#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:01:59 2021

@author: ariel
"""
import numpy as np
import matplotlib.pyplot as plt
def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

minx = 0
maxx = 200
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
g = plt.scatter(x = superficie, y = alquiler)
plt.title('gráfico de dispersión de los datos')

plt.xlabel('x')
plt.ylabel('y')

a, b = ajuste_lineal_simple(superficie, alquiler)
errores = alquiler - (a*superficie + b)
grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
grilla_y = grilla_x*a + b
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()
print(errores)
print("ECM:", (errores**2).mean())