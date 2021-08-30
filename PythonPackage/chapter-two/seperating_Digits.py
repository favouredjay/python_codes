number = int(input("Enter a five digit Number"))

first_number = number // 10000
second_number = number // 1000 % 10
third_number = number // 100 % 10
fourth_number = number % 100 // 10
fifth_number = number % 10

print("The seperated digit is ", first_number, " ", second_number, " ", third_number, " ", fourth_number, " ", fifth_number)
