def multiplo(a,b):
    if a % b == 0:
        return f"{a} é multiplo de {b}"
    else:
        return f"{a} não é multiplo de {b}"
    
n1 = float(input("Digite o número múltiplo: "))
n2 = float(input("Digite o número que tem como multiplo: "))

print(f"o número {multiplo(n1,n2)}")