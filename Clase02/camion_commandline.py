import csv
import sys
def costo_camion(nombre_archivo):

        f = open(nombre_archivo)
        rows = csv.reader(f)
        headers = next(rows)

        precio_total = 0
        for line in f:
                try:
                        row = line.split(',')
                        precio_cajones= int(row[1]) * float(row[2])
                        precio_total += precio_cajones
                except ValueError:
                        print("Faltan datos")
        return precio_total
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/missing.csv'

costo = costo_camion(nombre_archivo)
print("Costo total :", costo) #Costo total : 30381.15