import random
def generar_punto(): #genera numeros entre 0 y 1 para x e y
    x = random.random()
    y = random.random()
    return x, y #retorna el valor de ambas variables
N = 100000 #se solicita 100000 veces generar punto
M = 0 #se inicialiaza el contador de M en 0
for i in range(N): #repite N veces 
    x, y = generar_punto() #llama a generar punto asignandole un valor a cada uno
    if (x**2 + y**2) < 1: #comprueba que (x**2 + y**2) sea menor a 1
        M += 1  #se suma 1 al contador si cumple la condición 
        
pi = 4*M/N #se guarda el valor estimado de pi
print(f"{pi:.6f}") #se imprime pi por pantalla
