#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 17:55:12 2021

@author: ariel
"""

class TorreDeControl:
    '''
    Define una torre de control que contiene dos listas de aviones por despegar
    y aviones por aterrizar
    
    
    '''
    def __init__(self):
        self.vuelos_aterrizar = []
        self.vuelos_despegar = []
        self.vacio = False
    def nuevo_arribo(self,aterrizar):
        '''
        encola un elemento aterrizar a la cola vuelos_aterrizar
        '''
        self.vuelos_aterrizar.append(aterrizar)
    def nueva_partida(self,despegar):
        '''
        encola un elemento despegar a la cola vuelos_despegar
        '''
        self.vuelos_despegar.append(despegar)
    def ver_estado(self):
        '''
        Muestra el estado de las colas
        '''
        if len(self.vuelos_aterrizar + self.vuelos_despegar) == 0:
            print("No hay vuelos en espera.")
            self.vacio = True
        elif len(self.vuelos_aterrizar) == 0 and len(self.vuelos_despegar) != 0:
           print(f'vuelos esperando para despegar {self.vuelos_despegar}')
        elif len(self.vuelos_despegar) == 0 and len(self.vuelos_aterrizar) != 0:
            print(f'vuelos esperando para aterrizar {self.vuelos_aterrizar}') 
        else:
            print(f'vuelos esperando para aterrizar {self.vuelos_aterrizar} \nvuelos esperando para despegar {self.vuelos_despegar}')
            
   
    def asignar_pista(self):
        '''
        Asigna una pista a los vuelos, por lo que los elimina de la cola
        comprabando el estado de las colas
        '''
        self.ver_estado()
        if self.vacio == True:
             pass
        else:
            if len(self.vuelos_aterrizar) != 0:
                return self.vuelos_aterrizar.pop(0)
            elif len(self.vuelos_despegar) != 0:
                return self.vuelos_despegar.pop(0)
            
            
#%%
class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0