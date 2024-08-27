# Exercício 10.3: Soma dos Dígitos
#
# Escreva uma função recursiva chamada digits_sum que calcule a soma dos dígitos de um número inteiro.
# Teste a função com diferentes valores e imprima os resultados.
# Modifique a função para lidar com números negativos, somando os dígitos do valor absoluto do número.

def digits_sum(n):
    n = abs(n)
    
    if n < 10:
        return n
    
    return (n % 10) + digits_sum(n // 10)

print(digits_sum(123))
print(digits_sum(4567))
print(digits_sum(-9876))
print(digits_sum(0))
print(digits_sum(-5))