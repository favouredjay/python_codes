passes = 0
failure = 0

for student in range(10):
    grade = int(input("Enter grades"))
    if 70 <= grade <= 100:
        passes += 1
    elif grade < 70:
        failure += 1

print("Passes are", passes)
print("Failures are", failure)

if passes >= 8:
    print("Bonus to the instructor")
