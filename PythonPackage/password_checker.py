user_name = input("What's your name?")

password = input("what's your password")
password_secret = len(password) * '*'

print(f'{user_name}, your password {password_secret} is {len(password)} digit long')