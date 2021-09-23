word = input("Enter word or sentence")
vowel = ['a', 'e', 'i', 'o', 'u']
isContained = False
for i in word:
    if i in vowel:
        isContained = True
        break

if isContained:
    print("word contains vowel")
else:
    print("word does not contain vowel")

number = int(input("Enter number"))
if number % 2 == 0:
    print("is even")
else:
    print("is odd")
