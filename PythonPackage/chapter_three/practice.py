for i in range(2, 10, 2):
    print(i, end='')

for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()

for row in range(4):
    for column in range(8, -2, -2):
        print('@', end='')
    print()
