number = int(input("Enter numbers: "))
largest_number = None
smallest_number = None
for i in range(10):
    number = int(input("Enter numbers: "))
if largest_number is None:
    largest_number = number
elif number > largest_number:
    largest_number = number

if smallest_number is None:
    smallest_number = number
elif number < smallest_number:
    smallest_number = number

print("The largest number is", largest_number)
print("The smallest number is ", smallest_number)