v = 0
L = []
R = []
LR = []
menor_25 =0
menor_50 = 0
menor_75 = 0
menor_100 = 0

#---------------------------------
def div_num(x):

    global menor_25, menor_50, menor_75, menor_100

    if x < 25 and x >= 0:
        menor_25 += 1
        
    
    elif x < 50 and x >= 26:
        menor_50 += 1

    elif x < 75 and x >= 51:
        menor_75 += 1


    elif x < 100 and x >= 76:
        menor_100 += 1

    global R
    R = [menor_25, menor_50, menor_75, menor_100]
    return R
#--------------------------------  

while v >= 0:
    v = int(input("digite os números que vão compor a lista, pare com número negativo: "))
    L.append(v)

else:

    R = list(map(div_num, L))
    LR = R[-1]

    print(f"A quantidade de número entre 0 e 25 é {LR[0]}")
    print(f"A quantidade de número entre 26 e 50 é {LR[1]}")
    print(f"A quantidade de número entre 51 e 75 é {LR[2]}")
    print(f"A quantidade de número entre 76 e 100 é {LR[3]}")


