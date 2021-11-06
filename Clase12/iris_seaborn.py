#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:26:31 2021

@author: ariel
"""

import seaborn as sns
# creamos un dataframe de los datos de flores
iris_dataframe = sns.load_dataset("iris")
# y hacemos una matriz de gráficos de dispersión, asignando colores según la especie
g = sns.pairplot(iris_dataframe, hue="species", palette="Set2", diag_kind="kde", height=2.5)