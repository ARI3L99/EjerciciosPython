#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 20:46:32 2021

@author: ariel
"""
import pandas as pd
import os

def comparar_especie(nombre_cientifico_vereda,nombre_cientifico_parque):
    '''
    

    Se deben pasar los nombres cientificos como figuran en cada archivo y
    se mostrara un grafico que compara las diferencias de la altura y el 
    diametro dependiendo si estan en la vereda o en un parque.

    '''
    directorio = '../Data'
    archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
    archivo_parques = 'arbolado-en-espacios-verdes.csv'
    fname_veredas = os.path.join(directorio,archivo_veredas)
    fname_parque = os.path.join(directorio,archivo_parques)
    df_parques = pd.read_csv(fname_parque)
    df_veredas = pd.read_csv(fname_veredas)

    cols_sel_1 = ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']
    cols_sel_2 = ['nombre_cie','diametro', 'altura_tot']
    #copia la parte del df para aislar lo que nos interesa
    df_tipas_vereda = df_veredas[df_veredas['nombre_cientifico'] == nombre_cientifico_vereda][cols_sel_1].copy()
    #Inserta una columna nueva llamada ambiente con valor vereda para todos los de df_tipas_vereda
    df_tipas_vereda.insert(1,"ambiente","vereda")
    df_tipas_parque = df_parques[df_parques['nombre_cie'] == nombre_cientifico_parque][cols_sel_2].copy()
    #Inserta una columna nueva a df_tipas_parque
    df_tipas_parque.insert(1,"ambiente","parque")
    
    #Renombra las columnas de ambos DataFrame
    df_tipas_vereda = df_tipas_vereda.rename(columns={"nombre_cientifico": "Nombre Cientifico", "ambiente": "Ambiente", "diametro_altura_pecho": "Diametro", "altura_arbol": "Altura"})
    df_tipas_parque = df_tipas_parque.rename(columns={"nombre_cie": "Nombre Cientifico", "ambiente": "Ambiente", "diametro": "Diametro", "altura_tot": "Altura"})
    
    #Por ultimo se unen ambos df y se grafican comparando segun el ambiente donde se encuentra
    df_tipas = pd.concat([df_tipas_vereda, df_tipas_parque])
    df_tipas.boxplot('Diametro',by = 'Ambiente')
    df_tipas.boxplot('Altura',by = 'Ambiente')
    
    return df_tipas
#df = comparar_especie('Jacaranda mimosifolia','Jacarandá mimosifolia')