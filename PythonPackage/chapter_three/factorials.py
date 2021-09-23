value = int(input("Enter number"))
product = 1

for i in range(1, value+1):
    if value % i == 0:
        product = product * i
        print(i)
print(product)
