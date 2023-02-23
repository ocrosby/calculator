import math


class Computer:
    def __init__(self):
        pass

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