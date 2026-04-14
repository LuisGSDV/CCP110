print("Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações: 'Qual o melhor Sistema Operacional para uso em servidores?'")
print("As possíveis respostas são: \n 1- Windows Server \n 2- Unix \n 3- Linux \n 4- Netware \n 5- Mac OS \n 6- Outro")
print("Para isso, foram entrevistadas 10 pessoas (simule): ")

L = []

while len(L) <= 10:
    x = int(input("Digite o código do melhor SO para servidores"))

    if x <= 6 and x > 0:
        L.append(x)

    else:
        print("Digite uma valor válido!")

print(f"Valores para Windows Server: {L.count(1)}")
print(f"Valores para Unix: {L.count(2)}")
print(f"Valores para Linux: {L.count(3)}")
print(f"Valores para Netware: {L.count(4)}")
print(f"Valores para Mac: {L.count(5)}")
print(f"Valores para Outro: {L.count(6)}")



