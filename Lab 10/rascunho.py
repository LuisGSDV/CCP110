#lista aninhada

L1 = ['teste', 'teste2']
L2 = [1,2]
L3 = [[1,3], [3,4]]
LF = []
LF.append(L1)
LF.append(L2)
LF.append(L3)

print(LF)

# percorrer cada elemento

for listas in range(len(LF)):
    for elementos in LF[listas]:
        print(elementos)


# matriz
A = [[1, 2 ,3], [4,5,6], [7,8,9]]

for i in range(len(A)):
    x = A[i]
    print(x)
