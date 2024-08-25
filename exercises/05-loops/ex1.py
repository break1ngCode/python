# Exercício 5.1: Contagem Progressiva
#
# 1. Escreva um programa que conte de 1 a 10 e imprima cada número.
# 2. Modifique o programa para contar de 10 a 1 (em ordem decrescente).
# 3. Escreva um programa que conte apenas os números pares de 1 a 20.
# 4. Escreva um programa que some todos os números de 1 a 100.
# 5. Peça ao utilizador um número e conte de 1 até esse número.

print("Numbers between 1 and 10:")
for n in range(10):
    print(n+1)

print("\nNumbers between 10 and 1:")
for n in range(10, 0, -1):
    print(n)

print("\nEven numbers between 1 and 20:")
for n in range(1, 21):
    if n % 2 == 0:
        print(n)

print("\nEven numbers between 1 and 20 (other approach):")
for n in range(2, 21, 2):
    print(n)

numbers_sum = 0
for n in range(1, 101):
    numbers_sum += n

print("\nSum of all numbers between 1 and 100: " + str(numbers_sum))


user_number = int(input("Please, insert a number: "))
print("\nNumbers between 1 and " + str(user_number) + ": ")
for n in range(1, user_number + 1):
    print(n)