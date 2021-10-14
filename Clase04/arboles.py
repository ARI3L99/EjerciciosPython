import csv

def leer_arboles(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows) #guarda los nombres de los valores
    arboleda = [] #creo la lista donde se guardaran los diccionarios
    for r in rows:
        row = next(rows) #va recorriendo el archivo
        types = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float]
        #asigna los tipos de valores que va necesitar
        convertir = [func(val) for func, val in zip(types, row)] #guarda una lista con los tipos ya asignados
        record = dict(zip(headers, convertir)) #crea el diccionario
        arboleda.append(record) #guarda el diccionario actual
    return arboleda #retorna la lista de diccionarios de arboles
    
    

arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv") #llamo al metodo para leer el archivo


H=[[float(arbol['altura_tot']),float(arbol["diametro"])] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
altura = [[float(arbol['altura_tot'])] for arbol in arboleda]

#guarda los valores de la altura y el diametro de los arboles Jacaranda
print(H)
import os
import matplotlib.pyplot as plt
os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
#plt.hist(altura,bins=5)