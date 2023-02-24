import math

from tkinter import *

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

def button_clicked(value):
    entry_box_value = entryBox.get()
    answer = ''

    try:  # Here I am using the try and except block in ordert to avoid getting any syntax errors
        # This is useful because if I click the cos button without any nnumber infront of it, my program will not crash
        if value == 'x\u02b8':  # 7**2
            entryBox.insert(END, '**')
            return

        elif value == 'x\u00B2':
            answer = eval(entry_box_value) ** 2

        elif value == 'x\u00B3':
            answer = eval(entry_box_value) ** 3

        elif value == 'log₁₀':
            answer = math.log10(eval(entry_box_value))

        elif value == 'ln':
            answer = math.log2(eval(entry_box_value))

        elif value == 'C':
            entry_box_value = entry_box_value[0:len(entry_box_value) - 1]
            entryBox.delete(0, END)
            entryBox.insert(0, entry_box_value)
            return

        elif value == 'CE':
            entryBox.delete(0, END)

        elif value == '√':
            answer = math.sqrt(eval(entry_box_value))

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(entry_box_value)))

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(entry_box_value)))

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(entry_box_value)))


        # elif value == 'invsin':
        #     answer = math.asin(math.radians(eval(entry_box_value)))

        # elif value == 'invcos':
        #     answer = math.acos(math.radians(eval(entry_box_value)))

        # elif value == 'invtan':
        #     answer = math.atan(math.radians(eval(entry_box_value)))

        elif value == 'deg':
            answer = math.degrees(eval(entry_box_value))

        elif value == "rad":
            answer = math.radians(eval(entry_box_value))


        elif value == chr(247):
            entryBox.insert(END, "/")
            return

        elif value == '=':
            answer = eval(entry_box_value)

        else:
            entryBox.insert(END, value)
            return

        entryBox.delete(0, END)
        entryBox.insert(0, answer)

    except SyntaxError:
        pass


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def mod(a, b):
    return a % b


def lcm(a, b):
    l = math.lcm(a, b)
    return l


def gcd(a, b):
    h = math.gcd(a, b)
    return h


operations = {'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add,
              'SUBTRACTION': subtract, 'DIFFERENCE': subtract, 'MINUS': subtract, 'SUBTRACT': subtract,
              'PRODUCT': multiply, 'MULTIPLICATION': multiply, 'MULTIPLY': multiply,
              'DIVISION': divide, 'DIV': divide, 'DIVIDE': divide,
              'LCM': lcm, 'GCD': gcd,
              'MOD': mod, 'REMAINDER': mod, 'MODULUS': mod}


def findNumbers(t):
    l = []
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l


if __name__ == "__main__":
    root = Tk()
    root.title('Scientific Calculator')
    root.config(bg='gray')
    root.geometry('870x550+50+50')

    entryBox = Entry(root, font=('Comic Sans MS', 26, 'bold'), bg='gray', fg='white', bd=15, width=25, relief=GROOVE)
    entryBox.grid(row=0, column=0, columnspan=7)

    button_list = ["x\u02b8", "C", "CE", "√", chr(247), "sinθ", "invsin",
                   "x\u00B2", "1", "2", "3", "*", "cosθ", "invcos",
                   "x\u00B3", "4", "5", "6", "-", "tanθ", "invtan",
                   "log₁₀", "7", "8", "9", "+", "deg", "rad",
                   "ln", "0", ".", "%", "=", "(", ")"]
    columnvalue = 0
    rowvalue = 1

    for i in button_list:

        button = Button(root, width=6, height=3, bd=3, relief=GROOVE, text=i, bg='gray', fg='gray',
                        font=('serif', 20, 'bold'), activebackground='gray',
                        command=lambda button=i: button_clicked(button))
        button.grid(row=rowvalue, column=columnvalue)
        columnvalue += 1
        if columnvalue > 6:
            rowvalue += 1
            columnvalue = 0


    root.mainloop()