# Exercício 10.1: Potência
#
# 1. Escreva uma função recursiva chamada power que calcule a potência de uma base elevada a um determinado expoente.
# 2. Teste a função com diferentes valores de n e imprima os resultados.
# 3. Modifique a função para incluir uma verificação que impede que o cálculo seja feito com um expoente negativos.

def power(base, exponent):
    if exponent < 0:
        print("The exponent can not be negative.")
        return

    if exponent == 0:
        return 1

    if exponent == 1:
        return base

    return base * power(base, exponent - 1)

print(power(2, 3))
print(power(5, 0))
print(power(7, 2))
print(power(2, 5))