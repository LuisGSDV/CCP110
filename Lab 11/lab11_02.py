## meu jeito -->

import random

d = {}
x = 0
r = {}

def contarVal(dict):
    
    global x, r

    for i in range(1,21):
        for chave in dict.keys():
            if dict[chave] == i:
                x += 1
            
            r[i] = x
        x = 0
    
    
    return print(f"{r}")
    
    

for i in range(100):
    n = random.randint(1, 20)
    d[i] = n

resultado = contarVal(d)

print(resultado)

"""

professor -->

lista = [random.randint(0,20) in range(11)]

for v in lista:
    dicionario[v] = lista.count();
    
"""