import math


def evaluate(expression):
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