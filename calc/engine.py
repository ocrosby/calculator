import math

from calc.parser import Parser, DivideByZeroException

def evaluate(expression, vars = None):
    try:
        p = Parser(expression, vars)
        value = p.getValue()
    except DivideByZeroException as ex:
        return "Divide by zero error"


    # Return an integer type if the answer is an integer
    if int(value) == value:
        return int(value)

    # If Python made some silly precision error like x.99999999999996, just return x+1 as an integer
    epsilon = 0.0000000001
    if int(value + epsilon) != int(value):
        return int(value + epsilon)

    if int(value - epsilon) != int(value):
        return int(value)

    return value
