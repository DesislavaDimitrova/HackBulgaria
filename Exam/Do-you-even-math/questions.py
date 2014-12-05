from random import randint, choice
from operator import add, sub, mul, floordiv, pow


class Questions():

    def __init__(self):
        self.x = randint(1, 10)
        self.y = randint(1, 10)
        self.operators = {
        "addition": ("+", add),
        "substraction": ("-", sub),
        "multiplication": ("*", mul),
        "division": ("/", floordiv),
        "power": ("^", pow)
        }

    def generate_question(self):
        operator_name, (operator_symbol, self.operator_func) = choice(list(self.operators.items()))
        question = "What is the answer to %d %s %d?" % (self.x, operator_symbol, self.y)
        return question

    def solve_question(self):
        correct_answer = self.operator_func(self.x, self.y)
        return correct_answer


def main():
    a = Questions()
    print(a.generate_question())
    print(a.solve_question())


if __name__ == '__main__':
    main()
