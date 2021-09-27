class PlayerCharacter:
    def __init__(self, name, age):
        if age > 18:
            self.name = name
            self.age = age

    def run(self):
        return f'my name is {self.name}'

    @classmethod
    def adding(cls, num1, num2):
        return num1 + num2


player1 = PlayerCharacter("Cindy", 20)
player1.rank = 50
print(player1.rank)
print(player1.name)
print(PlayerCharacter.adding(50, 30))
print('hello'.swapcase().startswith('H'))
