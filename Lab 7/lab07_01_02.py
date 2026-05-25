## Função para calculo de média

def media(a, b):
    media = (a + b) / 2
    return media

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print(f"a média é: {media(n1,n2)}")