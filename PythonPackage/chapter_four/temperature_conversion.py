def convert_to_fahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit


def convert_to_fahrenheit_for_hundred_degrees():
    print("Celsius ", "     ", " fahrenheit")
    for celsius in range(1, 101):
        fahrenheit = (9 / 5) * celsius + 32
        print(" ", celsius, "             ", round(fahrenheit, 1))



print(convert_to_fahrenheit_for_hundred_degrees())
