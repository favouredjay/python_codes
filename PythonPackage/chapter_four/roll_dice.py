import random

frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0

for i in range(6_000_000):
    face = random.randrange(1, 7)
    if face == 1:
        frequency1 += 1
    elif face == 2:
        frequency2 += 1
    elif face == 3:
        frequency3 += 1
    elif face == 4:
        frequency4 += 1
    elif face == 5:
        frequency5 += 1
    elif face == 6:
        frequency6 += 1

print("Face", "-", "Frequency")
print("1 ", " - ", frequency1)
print("2 ", " - ", frequency2)
print("3 ", " - ", frequency3)
print("4 ", " - ", frequency4)
print("5 ", " - ", frequency5)
print("6 ", " - ", frequency6)

