#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de tipo semantico ya que no hacía lo que se esperaba, debía encontrar si había "a" en
#una cadena pero solo comprobaba el primer caracter.
#    Lo corregí usando directamente un if que comprueba si la cadena contiene "a"
#Código corregido:

def tiene_a(expresion):
    if "a" in expresion:
        return True
    else:
        return False

print(tiene_a('UNSAM 2020')) #False
print(tiene_a('abracadabra')) # True
print(tiene_a('La novela 1984 de George Orwell')) #True
...
...

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de sintaxis le faltan los ":" en la función,en el while y en el if, también en el if
# faltaba usar "==" en vez de "=" y por ultimo decía return "Falso" en vez de False.
#Código corregido:
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020')) #False
print(tiene_a('La novela 1984 de George Orwell')) #True
...
...

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era por el tipo de dato que se le pasa a la funcion, se espera una String pero se le está
#pasando un entero que sería el (1984), se puede solucionar pasando un ("1984") entre comillas para así tenerlo como
#String
#Código corregido:
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020') # False
tiene_uno('La novela 1984 de George Orwell') #True
tiene_uno("1984") #True (al haber corregido ese error)
...
...

#%%
#Ejercicio 3.4 suma()
#Comentario: el error estaba en que la función no retornaba nada y todo lo que se hiciese dentro de la función
#quedaba dentro de la función.
#   Lo corregí añadiendo un return en la función
#Código corregido:
def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

...
...

#%%
#Ejercicio 3.5 leer_camion()
#Comentario: el error estaba en que el diccionario registro vacío estaba al comienzo de la funcion
#por lo tanto se guardaba una sola vez y no se volvía a crear uno vacío para volver a guardar los nuevos datos
#   Lo corregí creando el registro vacío dentro del for haciendo que así guarde los nuevos datos cada vez que pasa
#   por una nueva linea del .csv
#Código corregido:
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]

    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
'''
[{'cajones': 100, 'nombre': 'Lima', 'precio': 32.2},                
 {'cajones': 50, 'nombre': 'Naranja', 'precio': 91.1},
 {'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
 {'cajones': 200, 'nombre': 'Mandarina', 'precio': 51.23},
 {'cajones': 95, 'nombre': 'Durazno', 'precio': 40.37},
 {'cajones': 50, 'nombre': 'Mandarina', 'precio': 65.1},
 {'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44}]
'''

