# Exercício 13.1: Calculadora Simples
#
# 1. Escreva uma função chamada calculator que peça ao utilizador dois números e a operação desejada (+, -, *, /).
# 2. Retorne o returnado da operação.
# 3. Adicione a possibilidade de realizar a operação de exponenciação (potência).
# 4. Adicione a possibilidade de realizar a operação de divisão inteira.
# 5. Adicione a possibilidade de realizar a operação de módulo (resto da divisão).
import math

VALID_OPERATIONS = ["+", "-", "*", "/", "**", "//", "%", 'q']

class Calculator:
    def __init__(self) -> None:
        pass

    def sum(self, a: int | float, b: int | float) -> int | float:
        return a + b

    def subtract(self, a: int | float, b: int | float) -> int | float:
        return a - b

    def multiply(self, a: int | float, b: int | float) -> int | float:
        return a * b

    def divide(self, a: int | float, b: int | float) -> int | float:
        return a / b

    def pow(self, a: int | float, b: int | float) -> int | float:
        return math.pow(a, b)
    
    def whole_division(self, a: int | float) -> int | float:
        return math.sqrt(a)

    def remainder(self, a: int | float, b: int | float) -> int | float:
        return a % b        

    def compute(self, a: int | float, b: int | float, operation: str):
        if operation == "+":
            return self.sum(a, b)
        elif operation == "-":
            return self.subtract(a, b)
        elif operation == "*":
            return self.multiply(a, b)
        elif operation == "/":
            return self.divide(a, b)
        elif operation == "**":
            return self.pow(a, b)
        elif operation == "//":
            return self.whole_division(a, b)
        elif operation == "%":
            return self.remainder(a, b)
        else:
            return 0

def print_operations():
    print("+ (Sum)")
    print("- (Subtract)")
    print("* (Multiply)")
    print("/ (Divide)")
    print("** (Pow)")
    print("// (Whole division)")
    print("% (Remainder)")
    print("q (Quit)")

def insert_operation():    
    while True:
        print_operations()
        operation = input("Please, insert a valid operation: ")

        if operation in VALID_OPERATIONS:
            return operation

        print("The operation is not supported. Please try again.")

calculator = Calculator()

while True:
    print("Python Calculator")
    try:
        a = float(input("Please, insert a number: "))
        operation = insert_operation()

        if operation == 'q':
            print("Quitting Python Calculator.")
            break

        b = float(input("Please, insert a number: "))
        
        result = calculator.compute(a, b, operation)

        print(f"The result of {a} {operation} {b} = {result}")
    except:
        print("An error occurred. You should insert a number.")