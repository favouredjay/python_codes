user_input = int(input("Enter a five digit number"))
first_number = user_input // 10000
second_number = user_input // 1000 % 10
third_number = user_input // 100 % 10
fourth_number = user_input % 100 // 10
fifth_number = user_input % 10

if first_number.__eq__(fifth_number) or second_number.__eq__(fourth_number):
    print("Palindrome")
else:
    print("Not a palindrome")
