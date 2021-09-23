pi = 0
for i in range(1, 200000):
    if i == 1:
        pi = 4
    elif i % 2 == 0:
        pi = pi - 4 / (i + (i - 1))
    else:
        pi = pi + 4 / (i + (i - 1))

        print(i, "-", pi)
