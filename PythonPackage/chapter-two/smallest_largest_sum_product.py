number_one = int(input("Enter first number"))
number_two = int(input("Enter second number"))
number_three = int(input("Enter third number"))

if number_one > number_two and number_one > number_three:
    print(number_one, " is the highest")
elif number_two > number_one and number_two > number_three:
    print(number_two, " is the highest")
elif number_three > number_one and number_three > number_two:
    print(number_three, " is the highest")

if number_one < number_two and number_one < number_three:
    print(number_one, "is the lowest")
elif number_two < number_three and number_two < number_one:
    print(number_two, "is the lowest")
elif number_three < number_two and number_three < number_one:
    print(number_three, " is the lowest")

add = number_one + number_two + number_three
print("The sum of all 3 numbers is", add)
product = number_one * number_two * number_three
print("The product of all 3 numbers is", product)
