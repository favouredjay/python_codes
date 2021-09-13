total = 0
grade_counter = 0

grade = int(input("Enter grades"))

while grade != -1:
    total += grade
    grade_counter += 1
    grade = int(input("Enter grades"))

if grade_counter != 0:
    average = total / grade_counter
    print("Average is", average)
else:
    print("No grades entered")
