# Exercício 2.1: Operações Básicas
#
# Crie duas variáveis a e b com valores numéricos.
# Realize e imprima o resultado das operações de adição, subtração, multiplicação e divisão entre a e b.
# Crie uma variável c com o valor da divisão inteira de a por b.
# Crie uma variável d com o valor do resto da divisão de a por b.
# Crie uma variável e que seja o resultado de a elevado à potência de b.
# Utilizando a biblioteca math, refaça o exercício 5 e encontre a raiz quadrada do resultado.

import math

a = 10
b = 5
print('a + b = ' + str(a + b))
print('a - b = ' + str(a - b))
print('a x b = ' + str(a * b))
print('a / b = ' + str(a / b))

c = a // b
d = a % b
e = a ** b

print('a // b = ' + str(c))
print('a % b = ' + str(d))
print('a ** b = ' + str(e))

potencia = math.pow(a, b)
print('math.pow(a, b) = ' + str(potencia))
print('math.sqrt(potencia) = ' + str(math.sqrt(potencia)))