idd = 0
sexo = ""
sal = 0

soma_idade = 0
cont_pessoas = 0

soma_sal_homens = 0
cont_homens = 0

mulheres_600 = 0

p = 1

while True:

    idd = int(input(f"Digite a idade da pessoa {p}: "))

    if idd < 0:
        print("Você digitou uma idade não válida, fim de entrada")
        break

    sexo = input(f"Digite o sexo (M/F) da pessoa {p}: ")
    sal = float(input(f"Digite o salário da pessoa {p}: "))

    soma_idade += idd
    cont_pessoas += 1

    if sexo == "M":
        soma_sal_homens += sal
        cont_homens += 1

    if sexo == "F" and sal < 600:
        mulheres_600 += 1

    p += 1


media_idade = soma_idade / cont_pessoas

if cont_homens > 0:
    media_sal_homens = soma_sal_homens / cont_homens
else:
    media_sal_homens = 0


print("Média de idade:", media_idade)
print("Média de salários dos homens:", media_sal_homens)
print("Quantidade de mulheres com salário abaixo de 600:", mulheres_600)


        


