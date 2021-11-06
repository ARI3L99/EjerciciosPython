import informe_final

def costo_camion(filename):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe_final.leer_camion(filename)
    return camion.precio_total()



'''
def f_principal(lista):
    camion = lista[1]
    costo = costo_camion(camion)
    print("Costo total:",costo) #Costo total : 47671.15
    
if __name__ == "__main__":
    import sys
    f_principal(sys.argv)
    '''
    