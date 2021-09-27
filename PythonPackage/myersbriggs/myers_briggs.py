from question import questions, get_answers
from question import PersonalityTypes


class myers_briggs(object):
    question = questions
    answers = get_answers()


def question_question():
    return questions


def set_question(self):
    self.question = questions


def answers():
    return get_answers()


def choice():
    for counter in range(21):
        print(questions[counter])
        answer = str(input("Enter your answer"))
        print(get_answers().append(answer))
        validate_input()


def extrovert_or_introvert():
    a = 0
    b = 0
    for i in questions:
        if answers()[i] == 'A':
            a += 1

        else:
            b += 1

        if a > b:
            return PersonalityTypes.E
        elif b > a:
            return PersonalityTypes.I


def sensing_or_intuitive():
    a = 0
    b = 0

    for i in questions:
        if answers()[i] == 'a':
            a += 1
        else:
            b += 1

        if a > b:
            return PersonalityTypes.S
        elif b > a:
            return PersonalityTypes.N


def thinking_or_feeling():
    a = 0
    b = 0

    for i in questions:
        if answers()[i] == 'a':
            a += 1
        else:
            b += 1

        if a > b:
            return PersonalityTypes.T
        elif b > a:
            return PersonalityTypes.F


def judging_or_feeling():
    a = 0
    b = 0

    for i in questions:
        if answers()[i] == 'a' or answers()[i] == 'a':
            a += 1
        else:
            b += 1

        if a > b:
            return PersonalityTypes.J
        elif b > a:
            return PersonalityTypes.F


def validate_input():
    for i in answers():
        if answers()[i] != 'A'.casefold() or answers()[i] != 'B':
            raise Exception("Wrong input")
