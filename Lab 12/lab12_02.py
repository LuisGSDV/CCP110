arquivo_par = open("arquivo-par.txt", "w")
arquivo_impar = open("arquivo-impar.txt", "w")
multiplo_4 = open("multiplo-4.txt", "w")

numeros = [x for x in range(1000)]

for x in numeros:
    if x % 2 == 0 :
        arquivo_par.write(f"{x}\n")

        if x % 4 == 0:
            multiplo_4.write(f"{x}\n")

    else:
        arquivo_impar.write(f"{x}\n")



arquivo_par.close()
arquivo_impar.close()
multiplo_4.close()