def geringoso(lista):
    d = {
        lista[0] : lista[0],
        lista[1] : lista[1],
        lista[2] : lista[2]
     }
    for k in d:
        translate = ""
        for c in d[k]:
            if c in "AEIOUaeiou":
                translate += c
                translate += "p"
            translate += c
        d[k] = translate
    return (d)
frutas = ['banana', 'manzana', 'mandarina']
translate = geringoso(frutas)
print(translate)
'''
output : {'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}
'''
