import random #importo random para asignar valores aleatorios
import statistics as stats #importo statistics para sacar la media de forma facil
import numpy as np #se importa numpy

def medir_temp(n): #funcion que retorna una lista con N temperaturas tomadas
    lista= [] #la lista donde se guardaran las temperaturas
    for i in range(n): #repite N veces 
        r = random.normalvariate(37.5, 0.2) #asigna un valor random al rededor de 37.5
        lista.append(r) # añade el valor a la lista
    np.save("../Data/temperaturas.npy",lista) #se guardan los vectores en el archivo         
    return lista

def resumen_temp(n): #funcion que da un resumen los valores max,min,prom y media
    lista_temp = medir_temp(n) #llama a la funcion medir_temp()
    maximo = max(lista_temp) #calcula el maximo
    minimo = min(lista_temp) #calcula el minimo
    prom = sum(lista_temp)/n #calcula el promedio
    media = stats.median(lista_temp) #calcula la media
    tupla = ("Max:",maximo,"Min:",minimo,"Prom:",prom,"Media:",media) #se guardan en una tupla
    return tupla    #retorna la tupla

print(resumen_temp(999)) #llama a la funcion del resumen y lo imprime
  
