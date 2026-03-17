c = 5
l = 5

for i in range(0, l +1):
    for j in range (0, c+1):

        if i % 2 == 0:

            if j % 2 == 0:
                print("$", end=" ")

            elif j % 2 == 1:
                print("&", end=" ")

        if i % 2 == 1:

            if j % 2 == 0:
                print("%", end=" ")
            
            elif j % 2 == 1:
                print("#", end=" ")

        elif i % 2 == 1:

            