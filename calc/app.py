import math
from tkinter import Tk, END, Button, GROOVE, Entry

from calc.parser import Parser, DivideByZeroException

BUTTONS = ["x\u02b8", "C", "CE", "√", chr(247), "sinθ", "invsin",
           "x\u00B2", "1", "2", "3", "*", "cosθ", "invcos",
           "x\u00B3", "4", "5", "6", "-", "tanθ", "invtan",
           "log₁₀", "7", "8", "9", "+", "deg", "rad",
           "ln", "0", ".", "%", "=", "(", ")"]

class App:
    def __init__(self, root: any, entry_box):
        self.root = root
        self.entry_box = entry_box

    def evaluate(self, expression, vars = None):
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

    def button_clicked(self, value):
        entry_box_value = self.entry_box.get()
        answer = ''

        try:  # Here I am using the try and except block in ordert to avoid getting any syntax errors
            # This is useful because if I click the cos button without any nnumber infront of it, my program will not crash
            if value == 'x\u02b8':  # 7**2
                self.entry_box.insert(END, '**')
                return

            elif value == 'x\u00B2':
                answer = eval(entry_box_value) ** 2

            elif value == 'x\u00B3':
                answer = eval(entry_box_value) ** 3

            elif value == 'log₁₀':
                __x = eval(entry_box_value)
                answer = math.log10(__x)

            elif value == 'ln':
                answer = math.log2(eval(entry_box_value))

            elif value == 'C':
                entry_box_value = entry_box_value[0:len(entry_box_value) - 1]
                self.entry_box.delete(0, END)
                self.entry_box.insert(0, entry_box_value)
                return

            elif value == 'CE':
                self.entry_box.delete(0, END)

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
                entry_box.insert(END, "/")
                return

            elif value == '=':
                answer = eval(entry_box_value)

            else:
                entry_box.insert(END, value)
                return

            self.entry_box.delete(0, END)
            self.entry_box.insert(0, answer)

        except SyntaxError:
            pass


    def add(self, a, b):
        return a + b


    def subtract(self, a, b):
        return a - b


    def multiply(self, a, b):
        return a * b


    def divide(self, a, b):
        return a / b


    def mod(self, a, b):
        return a % b


    def lcm(self, a, b):
        return math.lcm(a, b)


    def gcd(self, a, b):
        return math.gcd(a, b)


    operations = {'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add,
                  'SUBTRACTION': subtract, 'DIFFERENCE': subtract, 'MINUS': subtract, 'SUBTRACT': subtract,
                  'PRODUCT': multiply, 'MULTIPLICATION': multiply, 'MULTIPLY': multiply,
                  'DIVISION': divide, 'DIV': divide, 'DIVIDE': divide,
                  'LCM': lcm, 'GCD': gcd,
                  'MOD': mod, 'REMAINDER': mod, 'MODULUS': mod}


    def find_numbers(self, t):
        return [int(s) for s in t.split() if s.isdigit()]
        # l = []
        # for num in t:
        #     try:
        #         l.append(int(num))
        #     except ValueError:
        #         pass
        # return l

def configure_root(root):
    root.title('Scientific Calculator')
    root.config(bg='gray')
    root.geometry('870x550+50+50')

def create_button(app, root, caption: str):
    button = Button(root,
                    width=6,
                    height=3,
                    bd=3,
                    relief=GROOVE,
                    text=caption,
                    bg='gray',
                    fg='gray',
                    font=('serif', 20, 'bold'),
                    activebackground='gray',
                    command=lambda button=caption: app.button_clicked(button))
    return button


def main(_root):
    entry_box = Entry(_root,
                      font=('Comic Sans MS', 26, 'bold'),
                      bg='gray',
                      fg='white',
                      bd=15,
                      width=25,
                      relief=GROOVE)

    configure_root(_root)

    app = App(_root, entry_box)

    entry_box.grid(row=0, column=0, columnspan=7)

    column_value = 0
    row_value = 1

    for i in BUTTONS:
        button = create_button(app, _root, i)
        button.grid(row=row_value, column=column_value)
        column_value += 1
        if column_value > 6:
            row_value += 1
            column_value = 0


if __name__ == "__main__":
    root = Tk()

    main(root)

    root.mainloop()