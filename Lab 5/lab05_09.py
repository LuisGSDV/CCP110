soma = 0
termo = 0
i = 1
x = 0


if x == 0:

        x = int(input("digite um número: "))

        if x > 0:

            for i in range(1, x + 1):
                    
                termo = 1 / i
                soma = termo + soma

            print(soma)
                        
            

        else:
            print("número inválido digite um número positivo")
            
    
    




        




