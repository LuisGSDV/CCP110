a = 1
x = 0
quant_aluno = 0
soma = 0

while a < 81 :

    x = float(input(f"digite a nota dos alunos{a}: "))
    a = a + 1
    soma = soma + x
    n_insufic = x < 6.0

    if n_insufic:
        quant_aluno += 1


else:
    media_aluno = soma / (a - 1)
    print("todos os alunos foram regitrados")
    print(f" quantidade de notas insuficientes: {quant_aluno} ")
    print(f"média das notas: {media_aluno}")
    






