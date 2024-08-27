# Exercício 12.1: Tratamento Básico de Erros
#
# 1. Escreva um programa que peça ao utilizador para introduzir dois números e divida o primeiro pelo segundo.
# 2. Utilize um bloco try/except para tratar erros de divisão por zero e de entrada de dados inválida (não numérica).
# 3. Imprima mensagens apropriadas para cada tipo de erro tratado.

try:
    n1 = int(input("Insert one number: "))
    n2 = int(input("Insert another number: "))
    quotient = n1 / n2
    print(f"Quotient: {quotient}")
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("You must enter valid integers!")
except Exception as e:
    print(f"An error occurred: {e}")