c = 5
l = 10

for i in range(0, c + 1):
    for j in range(0, l + 1):

        if i > 0 and j > 0:

            if i == j or j > i:
                print("@", end=" ")
            else:
                print("#", end=" ")

    print()