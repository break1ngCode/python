# Exercício 7.2: Função de Soma
#
# 1. Escreva uma função chamada simple_sum que receba dois números como parâmetros e retorne a soma deles.
# 2. Modifique a função para receber uma lista de números e retorne a soma de todos os elementos.
# 3. Crie uma função que receba dois números e retorne a multiplicação deles.
# 4. Crie uma função que receba uma lista de números e retorne o maior número.
# 5. Crie uma função que receba uma lista de números e retorne a média dos números.

def simple_sum(n1, n2):
    return n1 + n2

def sum_list(numbers):
    numbers_sum = 0
    for n in numbers:
        numbers_sum += n
    return numbers_sum

def multiply(n1, n2):
    return n1 * n2

def biggest_number(numbers):
    return min(numbers)

def mean(numbers):
    numbers_sum = 0
    for n in numbers:
        numbers_sum += n
    
    return numbers_sum / len(numbers)

numbers_list = [1,2,3,4,5]

print(simple_sum(1,2))
print(sum_list(numbers_list))
print(multiply(3,4))
print(biggest_number(numbers_list))
print(mean(numbers_list))
