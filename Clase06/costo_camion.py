import informe_funciones #importo informe funciones

def costo_camion(nombre_archivo):
        camion = informe_funciones.leer_camion(nombre_archivo) #lee el archivo usando leer camion de informe funciones
        costo_total = 0 #incializo en 0 el costo total
        for i in camion: #recorre la lista
            ncajones = i['cajones'] #guarda los valores de los cajones
            precio = i['precio'] #guarda los valores de los precios
            costo_total += ncajones * precio #multiplica cajones por precio y se suma a costo total
        return costo_total


#costo = costo_camion("../Data/camion.csv")
#print("Costo total:",costo) #Costo total : 47671.15