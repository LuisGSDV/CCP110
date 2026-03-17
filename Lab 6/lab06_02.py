l = int(input("digite o número de linhas: "))
c = int(input("digite o número de colunas: "))

for i in range (0, l):
    for j in range (0, c):
        if i == 0 or j == 0 or i == l - 1 or j == c - 1:
            print("*", end=' ')
        
        else:
            print(' ', end = ' ')

    print()