import random
def tirar():
    lista = [random.randint(1, 6) for x in range(5)] #genera una lista con 5 valores aleatorios entre 1 y 6
    return lista

def es_generala(tirada):
    return all(x == tirada[0] for x in tirada) #comprueba en toda la lista si los numeros son iguales y retorna verdadero o falso


def prob_generala(N):
    G = 0
    for i in range(N):
        intentos = 3 #cantidad de intentos con la que inicia 
       
        while intentos > 0: #bucle mientras tenga intentos disponibles
            tirada = tirar() #se llama al metodo tirar 
            intentos -= 1 # se resta un itento
            if es_generala(tirada): #comprueba si es generala
                G+= 1 #suma las veces que salió generala
                break #corta el bucle si es que salió generala en cualquier punto
    prob = G/N #calcula la probalidad
    print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
    return prob #retorna la probabilidad 
   
N = 100000 #numero de manos
print(prob_generala(N)) 


