from operator import add, eq
import random
from abc import ABC, abstractmethod

class Equation:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    @abstractmethod
    def calc(self):
        pass

class Add(Equation):
    def calc(self):
        result=self.num1+self.num2
        print("%d + %d = ?") % (self.num1, self.num2)
add1 = Add()
class Subtract(Equation):
    def calc(self):
        result=self.num1-self.num2
        print("%d - %d = ?") % (self.num1, self.num2)
subtract = Subtract()
class Multiply(Equation):
    def calc(self):
        result=self.num1*self.num2
        print("%d * %d = ?") % (self.num1, self.num2)
multiply = Multiply()
class Divide(Equation):
    def calc(self, num1, num2):
        result=round(num1+num2, 2)
        print("%d / %d = ?") % (num1, num2)
divide = Divide()

a={
'+': add1(),
'-': subtract(),
'*': multiply(),
'/': divide()
}

random.choice(['+', '-', '*', '/'])

# while True:
#         try:
#             user_input = float(input())
#             break
#         except ValueError:
#             print("To nie jest liczba!")
# if user_input == result:
#     print("Wynik prawidłowy")
# else:
#     print("Wynik błędny")