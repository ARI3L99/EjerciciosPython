import csv

def parse_csv(nombre_archivo, select = None, types = None,has_headers = True,silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    try:
        if select and has_headers == False:
            raise RuntimeError("Para seleccionar, necesito encabezados.")
        else:
            with open(nombre_archivo) as f:
                filas = csv.reader(f)
                if has_headers:
                    # Lee los encabezados del archivo
                    encabezados = next(filas)

            # Si se indicó un selector de columnas,
            # buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
        
                    if select:
                        indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                        encabezados = select
                    else:
                        indices = []

                    registros = []
                    for fila in filas:
                        if not fila:    # Saltear filas vacías
                            continue
                    # Filtrar la fila si se especificaron columnas
                        if indices:
                            fila = [fila[index] for index in indices]
                        if types:
                            try:
                                fila = [func(val) for func, val in zip(types, fila) ]
                            

               
                            except ValueError:
                                if silence_errors:
                                    print(fila, "no se pudo convertir")
                         # Armar el diccionario
                        registro = dict(zip(encabezados, fila))
                        registros.append(registro)
                else:
                    registros = []
                    for fila in filas:
                        if not fila:
                            continue
                        if types:
                            fila = [func(val) for func, val in zip(types, fila) ]
                        registro = (fila)
                        registros.append(registro)
                    
            return registros
                    
    except RuntimeError as e:
        if silence_errors: # solo muestra los errores si silence_errors
            print(e)
    
        
    



#camion = parse_csv('../Data/camion.csv', types=[str, int, float])
#cajones_lote = parse_csv('../Data/camion.csv', select=['nombre', 'cajones'], types=[str, int])
#precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=True)