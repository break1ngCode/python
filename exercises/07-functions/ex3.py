# Exercício 7.3: Função de Fatorial
#
# 1. Escreva uma função chamada factorial que receba um número inteiro e retorne o fatorial desse número.
# 2. Modifique a função para verificar se o número é negativo e retorne uma mensagem apropriada.
# 3. Implemente a função utilizando recursão.
# 4. Teste a função com diferentes valores de entrada.
# 5. Crie uma função que receba um número inteiro e utilize a função factorial para calcular e imprimir o fatorial de cada número de 1 até o número fornecido.

def factorial(n):
    if n < 1:
        print("The number must be positive.")
        return

    total = 1
    for i in range(n, 1, -1):
        total *= i
    return total

def recursive_factorial(n):

    if n == 1:
        return 1

    return n * recursive_factorial(n-1)
    
def all_factorials(n):
    print("All Factorials: ")
    for i in range(1, n + 1):
        print(recursive_factorial(i))

print(factorial(5))
print(recursive_factorial(5))

print(factorial(6))
print(recursive_factorial(6))

all_factorials(5)