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
    
def scatter_hd(lista_de_pares): #funcion que genera un grafico de la relacion entre altura y diametro de los arboles
    os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv') #
    plt.scatter(lista_de_pares[1], lista_de_pares[0], alpha = .5) #genera el grafico
    plt.xlabel("Diametro") #indica donde va el diametro en el grafico
    plt.ylabel("Altura") #indica la altura
    plt.show() 
    
import os
import matplotlib.pyplot as plt

arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv") #llamo al metodo para leer el archivo
#lista=[[float(arbol['altura_tot']),float(arbol["diametro"])] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

h = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
#obtener una lista con la altura
d = [float(arbol["diametro"]) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
#obtener una lista con los diametros
lista_de_pares =(h,d) #genera una lista con los diametros y alturas
scatter_hd(lista_de_pares) #llama a la funcion para graficar


#plt.hist(h ,bins=20)
