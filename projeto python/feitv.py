login = 0

def linha(n):
    l = ""

    for i in range(0,n):
        l += "-"
    return l

def inp_menu(x):
    if x == 1:
        b = 1



if login == 0:

    print(linha(40))
    print("MENU")
    print(linha(40))

    print(linha(40))
    print("1.Login\n2.Cadastro\n3.Sobre")
    print(linha(40))
    option = (input("Digite a opção:"))
    inp_menu(option)

