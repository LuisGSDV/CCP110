L = []

def maior(a, x):
    
    if a > x:
        print('ta retornando: %f' %a)
        x = a
        return a
    else:
        print('ta retornando: %f' %x)
        return x

#-----------------------------------------------------------

for i in range(10):
    q = float(input("Digite os números da lista: "))
    L.append(q)

x = L[0]
    
for a in L:
    resultado = maior(a, x)

print(L)
print(resultado)

#-----------------------------------------------------------


