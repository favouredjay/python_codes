gallons_used = float(input("Enter the gallons used or -1 to end"))
miles_driven = float(input("Enter miles driven"))

miles_counter = 0
total = 0

while gallons_used != -1:
    miles_per_gallon = miles_driven / gallons_used
    total = total + miles_per_gallon
    miles_counter += 1
    print("The miles/gallon of this tank was", miles_per_gallon)

    gallons_used = float(input("Enter the gallons used or -1 to end"))
    if gallons_used != -1:
        miles_driven = float(input("Enter miles driven"))
    else:
        print("The overall average miles/gallon was", total / miles_counter)
