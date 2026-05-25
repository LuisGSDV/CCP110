def areaTri(b, h):
    area = b * h / 2
    return area

n1 = float(input("Digite a base do triangulo: "))
n2 = float(input("Digite a altura do triangulo: "))

print(f"A área de triângulo é: {areaTri(n1,n2)}")