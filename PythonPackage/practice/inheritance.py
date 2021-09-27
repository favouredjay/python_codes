class User():
    def sign_in(self):
        return 'logged in'

    def attack(self):
        return 'do nothing'


class player_1(User):
    def __init__(self, name, power):
        self.power = power
        self.name = name

        def attack(self):
            User.attack(self)
            return f'{self.name} attack with {self.power}'


class player_2(User):
    def __init__(self, name, power):
        def attack(self):
            return {power}


play = player_1("Joy", 50)
print(play.attack())


class A:
    num = 1


class B(A):
    num = 3


class C(A):
    num = 50


class D(B, C):
    pass


print(D.num)


def cube_list(values):
    for i in range(len(values)):
        values[i] **= 3
    return values


numbers = [1, 2, 3, 4, 5, 6, 7]
print(cube_list(numbers))
