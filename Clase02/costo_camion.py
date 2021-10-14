import informe_funciones
def costo_camion(nombre_archivo):
    camion = informe_funciones.leer_camion(nombre_archivo)
    costo_total= 0
    for i in camion:
        ncajones = i["cajones"]
        precio = i["precio"]
        costo_total += ncajones * precio
    return costo_total


costo = costo_camion("../Data/camion.csv")
print("Costo total:",costo) #Costo total : 47671.15