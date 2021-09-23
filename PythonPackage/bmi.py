import math

height = 1.0
weight = 1.0


def __init__(self, name="", age=1):
    self.name = name
    self.age = age


def set_name():
    input("Enter your name")
    self.name = name


def get_name():
    return name


def set_age(self):
    int(input("Enter age"))
    if 0 >= age > 200:
        raise Exception("Wrong input")

    self.age = age


def get_age():
    return age


def set_height(self):
    int(input("""
    Enter height in meters of in foot
    Press 1 to enter height in meters
    Press 2 to enter height in foot
    """))

    if input == 1:
        int(input("Enter height in meters"))
        print(height)
    elif input == 2:
        int(input("Enter height in foot"))
        height = height * 0.305

        self.height = height
    else:
        print("invalid entry")
        set_height(self)


def get_height():
    return height


def set_weight(self):
    input("""
    Enter weight in kg or pounds
    1. Enter weight in kg
    2. Enter weight in pounds
    """)
    if input == 1:
        input("Enter weight in kg")
        print(weight)
    elif input == 2:
        input("Enter weight in pounds")
        weight = weight * 0.453592

        self.weight = weight
    else:
        print("Invalid entry")
        set_weight(self)


def get_weight():
    return weight


def bmi():
    bmi = get_weight() / math.pow(get_weight(), 2)

    if bmi < 18.5:
        print("underweight")
    elif 18.5 <= bmi <= 24.5:
        print("Normal")
    elif 25 <= bmi < 30:
        print("Overweight")
    elif bmi >= 30:
        print("Obese")
    return bmi


def full_info():
    set_name()
    set_age(self)
    set_weight(self)
    set_height(self)
    bmi()

if __name__ == '__main__':



