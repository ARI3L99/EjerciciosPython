#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:50:22 2021

@author: ariel
"""
import pandas as pd
import os
import seaborn as sns

directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df_lineal = pd.read_csv(fname)
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
#df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
#df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')
#sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')
df_jacarandas = df_lineal[df_lineal['nombre_cientifico'] == 'Jacaranda mimosifolia'][cols_sel].copy()