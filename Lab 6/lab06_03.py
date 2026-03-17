c = 5
l = 5
n = 1

for i in range(0, l+1):

    if i % 2 == 0:
        n = 0

    elif i % 2 == 1:
        n = 1

    for j in range (0, c+1):

        if j % 2 == n :
            print("*", end= " ")
        else:
            print("#", end = " ")
    
    print()


            


        
        