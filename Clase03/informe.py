import csv


def leer_camion(nombre_archivo):
    '''
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        costo_total = 0
        for row in rows:
            record = dict(zip(headers, row))
            #lote = (row[0], int(row[1]), float(row[2]))
            #cajones = {
            #    "nombre": lote[0],
             #   "cajones": lote[1],                esto está comentado porque es como lo hice en un principio
              #  "precio": lote[2]
            #}
            ncajones = int(record["cajones"])
            precio = float(record["precio"])
            costo_total += ncajones * precio
            camion.append(record)
        print(camion)
        '''
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    select = ['nombre', 'cajones', 'precio']
    indices = [headers.index(ncolumna) for ncolumna in select]
    row = next(rows)
    record = {ncolumna: row[index] for ncolumna, index in zip(select, indices)}
    camion = [{ ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows]
    print(camion)
    return camion


def leer_precios(nombre_archivo):
    precios = {}
    f = open(nombre_archivo)
    rows = csv.reader(f)

    for line in f:
        try:
            row = line.split(',')
            key = row[0]
            valor = float(row[1])
            precios[key] = valor

        except:
            pass

    return precios

camion_dic = leer_camion("../Data/camion.csv")
precios_dic = leer_precios("../Data/precios.csv")
costo_camion = sum([int(s['cajones']) * float(s['precio']) for s in camion_dic])
print(costo_camion)
total_vendido = sum([int(s['cajones']) * precios_dic[s['nombre']] for s in camion_dic])
print(total_vendido)
mas100 = [s for s in camion_dic if int(s['cajones']) > 100]

myn =  [s for s in camion_dic if s['nombre'] in {'Mandarina','Naranja'}]
costo10k=[s for s in camion_dic if int(s['cajones']) * float(s['precio']) > 10000 ]


'''for row in camion_dic: #calcular el valor de venta y valor del camion
    p = precios_dic[row["nombre"]]
    c = int(row["cajones"])
    total_vendido += p * c
    p1 = float(row["precio"])
    c1 = int(row["cajones"])
    costo_camion += p1 * c1
    
print("El camion costó",costo_camion) #47671.15
print("La venta recaudó",total_vendido) #62986.1
print("La diferencia fue de",total_vendido-costo_camion) #15314.949999999997
if total_vendido > costo_camion: #hubo ganancia
    print("Hubo ganacia")
else:
    print("Hubo perdida")
'''