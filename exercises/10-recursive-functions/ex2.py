# Exercício 10.2: Sequência de Fibonacci
#
# 1. Escreva uma função recursiva chamada fibonacci que retorne o n-ésimo número da sequência de Fibonacci.
# 2. Teste a função para diferentes valores de n e imprima os resultados.
# 3. Modifique a função para usar memoização para melhorar a eficiência.

def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print("First 10 terms of the Fibonacci sequence: ")
for n in range(10):
    print(fibonacci(n))