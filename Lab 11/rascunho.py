## .keys() = retorna chave || .values = retorna valor
## d = {chave: valor}
## print(d[chave]) = valor

#percorre valores do dicionario

d = {3: "luis", 7: "sim", 3: "não"}

for chave in d.keys():
    print(d[chave])

    if d.keys()[-1]:
        print("fim")