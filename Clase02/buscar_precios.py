def buscar_precio(fruta):
    f = open("../Data/precios.csv", "rt")
    headers = next(f).split(",")
    comprobar = False
    for line in f:
        row = line.split(",")
        if row[0] in fruta:
            comprobar = True
            return print("El precio de la", fruta, "es :", float(row[1]))
    if comprobar is False:
        print(fruta, "no figura en el listado de frutas")
    f.close()
buscar_precio("Frutilla")
'''
fruta = Frambuesa
El precio de la Frambuesa es : 34.35
fruta = kale
kale no figura en el listado de frutas
fruta = Frutilla
El precio de la Frutilla es : 53.72
'''
