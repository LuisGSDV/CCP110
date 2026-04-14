# concatenação

list_1 = [1,2,3]
list_2= [4,5]
concat = list_1 + list_2
print(concat)

#.extend

list_2= [4,"t"]
list_1.extend(list_2)

print(list_1)

#repetição

list_1 = [1,2,3]
rep = list_1 * 4
print(rep)

# map(f, l), usa lista como parametro pra função

#filter(f, l) limpa numeros com base em funções

#len(palavra) serve pra condicionais com tamnho em caracteres, e tbm pra qual caractere

#l.append(1), vai adicionar 1 ao final da lista
#l.pop(1), exclui segundo valor da lista, lembre [0, 1, 2 ,3, ..]
# -> l.pop(-1), deleta ultimo valor da lista

#list_comprehesion
quadrado = []

""""
for x in range(10):
   quadrado.append( x * x)
 -------------->
em list_comprehesion
 x// y - > inteiro ; x / y -> float
"""
#count(x) -> retorna quantidade indices atribuidos com valor x

quadrado = [x * x for x in range(10)]
print(quadrado)

quadrado_par = [ x/2 for x in quadrado]
print(quadrado_par)

tres = [3 for x in range(5)]
dois = [2 for x in range(3)]

tres_com_dois = tres + dois

print(tres_com_dois.index(2)) # mostra primeiro indice atribuido a valor entre pareteses

# l.reverse() - > inverte ; l.sort() -> ordena || n funcionam com tipos heterogeneos