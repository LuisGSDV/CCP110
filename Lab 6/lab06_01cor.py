totalPrimos = 0

n = int(input("Digite N: "))
        
for i in range(n):
    x = int(input("Digite X: "))
    if x > 1:
        primo = 1
        for j in range(2,x):
            if x % j == 0:
                primo = 0
                break

        totalPrimos += primo

print(f"Total primos = {totalPrimos}")