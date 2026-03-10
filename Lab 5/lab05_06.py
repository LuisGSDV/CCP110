i = 1
n = 0
soma = 0

while i != 0:
    x = int(input("digite numeros"))
    if x == 0:
        i = 0
        print(f"quantidade de números {n}")
        print(f"soma de todos os numeros {soma}")
        print(f"média aritmética {soma / n}")
        

    else :
        soma += x
        n += 1
    