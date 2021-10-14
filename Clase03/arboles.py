import csv
#funcion para leer y guardar una lista con los arboles de un parque
def leer_parque(nombre_archivo,parque):
     lista_arboles= []

     with open(nombre_archivo, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = dict(zip(headers, row))
                if record["espacio_ve"] == parque: 
                    lista_arboles.append(record)
                else:
                    pass
            return lista_arboles
general_paz = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
for x,i in enumerate(general_paz, start=1): #muestra los 690 arboles del parque general paz
    print(f"{x} {i}")

...
...
...
#funcion para guardar una lista de especies sin que se repitan
def especies(lista_arboles):
    lista_especies = []
    for row in lista_arboles:
        lista_especies.append(row["nombre_com"])
    unicos = set(lista_especies)
    return unicos

lista_especies = especies(general_paz)
for x,i in enumerate(lista_especies): #enumera y muetra por pantalla las especies del parque general paz
    print(f"{x} {i}")

...
...
...
#Funcion que cuenta cuantos arboles de cada tipo hay
def contar_ejemplares(lista_arboles):
    from collections import Counter
    contador = Counter()
    for row in lista_arboles:
        
        contador[row["nombre_com"]] += 1
        
    return contador

...
...
...

los_andes = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "ANDES, LOS")
centenario = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "CENTENARIO")
lista_especies2 = especies(los_andes)
lista_especies3 = especies(centenario)
contarA= contar_ejemplares(general_paz)
contarB= contar_ejemplares(los_andes)
contarC= contar_ejemplares(centenario)

print(f"General Paz : {contarA.most_common(5)}")    #Muestra las 5 especies más comunes del parque general paz
print(f"Los Andes : {contarB.most_common(5)}")     #Muestra las 5 especies más comunes del parque los andes
print(f"Centenario : {contarC.most_common(5)}")     #Muestra las 5 especies más comunes del parque centenario

...
...
...
#funcion para obtener las alturas de los arboles de un parque
def obtener_alturas(lista_arboles,especies):
    lista_alturas = []
    for row in lista_arboles:
        if row["nombre_com"] in especies:
            lista_alturas.append(float(row["altura_tot"]))
    return lista_alturas
lista_alturas = obtener_alturas(general_paz, "Jacarandá")

print(f"Altura maxima :{max(lista_alturas)}") #muestra la altura maxima de los arboles en un parque
print(f"Altura promedio : {sum(lista_alturas)/len(lista_alturas)}") #muestra la altura promedio de los arboles del parque

...
...
...
#funcion para obtener la inclinacion de los arboles de un parque
def obtener_inclinaciones(lista_arboles,especies): #recorre la lista de arboles de un parque y los guarda en una lista
    lista_inclinacion = []
    for row in lista_arboles:
        if row["nombre_com"] in especies:
            lista_inclinacion.append(int(row["inclinacio"]))
    return lista_inclinacion

lista_inclinacion  = obtener_inclinaciones(general_paz, "Jacarandá")
print(lista_inclinacion)

...
...
...
#funcion para obtener el especimen más inclinado
def especimen_mas_inclinado(lista_arboles):
    mayor_inclinacion = 0 #Inicio este valor en cero que luego se actualiza para guardar el de mayor inclinación
    especie = especies(lista_arboles) #crea una lista con las especies
    for i in especie: #recorre la lista de especies
        #print(i)
        lista = obtener_inclinaciones(lista_arboles,i) #guarda todas las inclinaciones de los arboles de la especie actual
        #print(lista)
        if max(lista) > mayor_inclinacion: #verifica cual es el valor más alto
            mayor_inclinacion = max(lista) #guarda el mayor valor
            mas_inclinado = i #guarda el nombre del que tiene el mayor valor
    print("Mas inclinado",mayor_inclinacion) #muestra por pantalla el valor del más inclinado
    return mas_inclinado
mayor_inclinacion_centenario = especimen_mas_inclinado(centenario)
print(mayor_inclinacion_centenario) #Mas inclinado 80
                                    #Falso Guayabo (Guayaba del Brasil)
mayor_inclinacion_general_paz = especimen_mas_inclinado(general_paz)
print(mayor_inclinacion_general_paz) #Mas inclinado 70
                                     #Macrocarpa (Ciprés de Monterrey o Ciprés de Lambert)
mayor_inclinacion_los_andes = especimen_mas_inclinado(los_andes)
print(mayor_inclinacion_los_andes) #Mas inclinado 30
                                   #Jacarandá

...
...
...
#función para obtener el promedio de los arboles más inclinados
def especie_promedio_mas_inclinada(lista_arboles):
    prom = 0
    especie_promedio = ""
    especie = especies(lista_arboles)
    for i in especie:
        #print(i) lo uso para ver por pantalla por que arbol va pasando
        lista = obtener_inclinaciones(lista_arboles, i)
        #print(lista) veo la lista actual de cada arbol
        promedio = sum(lista) / len(lista) #saca el promedio de la lista de arboles de la especie
        if promedio > prom:
            prom = promedio #guarda el valor promedio más inclinado de los arboles
            especie_promedio = i # guarda el nombre de la especie de arbol promedio más inclinado
    print("especimen promedio más inclinado", prom) #Indica el valor de la inclinación promedio más alta
    return especie_promedio
especie_mas_inclinada = especie_promedio_mas_inclinada(los_andes)
print(especie_mas_inclinada) #en el caso del parque Los andes imprime Álamo plateado con 25 de inclinación
