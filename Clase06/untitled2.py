import csv


def leer_camion(nombre_archivo): #Funcionque lee y guarda los datos dentro de una lista
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            cajones = {
                "nombre": lote[0],
                "cajones": lote[1],
                "precio": lote[2]
            }
            camion.append(cajones)
    return camion

...
...
...

def leer_precios(nombre_archivo): #Funcion que lee y guarda los datos en un diccionario
    precios = {}
    f = open(nombre_archivo)

    for line in f:
        try:
            row = line.split(',')
            key = row[0]
            valor = float(row[1])
            precios[key] = valor

        except:
            pass

    return precios

...
...
...

camion= leer_camion("../Data/camion.csv") #Leer los datos de camion.csv
precios = leer_precios("../Data/precios.csv") #Leer los datos de precios.csv
costo_camion = 0.0
total_vendido = 0.0

for row in camion: #calcular el valor de venta y valor del camion
    print(row)
    total_vendido += precios[row["nombre"]] * row["cajones"]
    costo_camion += row["precio"] * row["cajones"]

print("El camion costó",costo_camion) #47671.15
print("La venta recaudó",total_vendido) #62986.1
print("La diferencia fue de",total_vendido-costo_camion) #15314.949999999997
if total_vendido > costo_camion: #hubo ganancia
    print("Hubo ganacia")
else:
    print("Hubo perdida")
    
...
...
...


def hacer_informe(camion,precios): #Función para crear un informe 3.13
    n = 0
    informe = []
    for i in camion:
         a = precios[camion[n]["nombre"]] 
         b = camion[n]["precio"]
         cambio = a-b
         informe.append((camion[n]["nombre"],camion[n]["cajones"], b, cambio))
         n += 1
         
    return informe

...
...
...

informe = hacer_informe(camion,precios)

headers = ("Nombre", "Cajones", "Precio", "Cambio")
print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
print("-"*10,"-"*10,"-"*10,"-"*10)
for nombre, cajones, precio, cambio in informe: # Imprimir tabla con formato 3.14
    print(f"{nombre:>10s} {cajones:>10d} {'$' + str(precio):>10s} {cambio:>10.02f}") 
   
