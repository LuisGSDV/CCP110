L = ['teste1', 'teste2', 'teste3', 'teste4']

#  Mostra elementos

for i in L:
    print(i)

# assim tbm, usando indices

for i in range (len(L)):
    print(L[i])


# Assim remove o ultimo

L.pop()
print(L) #removeu o 'teste4'

#assim remove só os especificos valores entre ()

L.remove('teste2') #removeu o valor do indice 1
print(L)