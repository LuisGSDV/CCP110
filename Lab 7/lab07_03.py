def maior(a,b):
    if a > b :
        return a
    elif a < b:
        return b   
    else:
        return "nenhum, pois possuem igualdade"
    
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: " ))

print(f"o maior número é: {maior(n1,n2)}")