i = 1
n = 0
soma = 0

while i != 0:
    x = int(input("digite numeros, menos o 0 (ou n) :"))
    if x == 0:
        i = 0
        print(f"soma de todos os numeros {soma}")

    soma = soma + x
