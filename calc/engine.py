import math


class Computer:
    input_value: str

    def __init__(self):
        self.input_value = ''

    def add(self, number1: float, number2: float):
        return number1 + number2

    def sub(self, number1: float, number2):
        return number1 - number2

    def multiply(self, number1: float, number2: float):
        return number1 * number2

    def divide(self, number1: float, number2: float):
        return number1 / number2

    def sine(self, value: float):
        return math.sin(value)

    def cosine(self, value: float):
        return math.cos(value)

    def tangent(self, value: float):
        return math.tan(value)

    def evaluate(self, expression):
        expression = list(expression[::-1])

        def get_value():
            sign = 1
            if expression and expression[-1] == "-":
                expression.pop()
                sign = -1
            value = 0
            while expression and expression[-1].isdigit():
                value *= 10
                value += int(expression.pop())
            return sign * value

        def get_term():
            term = get_value()
            while expression and expression[-1] in "*/":
                op = expression.pop()
                value = get_value()
                if op == "*":
                    term *= value
                else:
                    term = math.floor(1.0 * term / value)
            return term

        ans = get_term()
        while expression:
            op, term = expression.pop(), get_term()
            if op == "+":
                ans += term
            else:
                ans -= term

        return str(ans)