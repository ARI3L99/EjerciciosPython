import random
def cocumple(N):
    n = 0
    for i in range(N):
        lista_personas = [random.randint(1, 365) for x in range(30)]
        r = []
        for x in lista_personas:
            if x not in r:
                r.append(x)
            else:
                n +=1
            prom = (n/30)/N
    return prom
print(f"{cocumple(10000)}")