# Exercício 4.2: Par ou Ímpar
#
# 1. Peça ao utilizador um número inteiro.
# 2. Verifique se o número é par ou ímpar e imprima uma mensagem apropriada.
# 3. Peça ao utilizador para introduzir um número e verifique se ele é múltiplo de 5.
# 4. Peça ao utilizador para introduzir três números e imprima o maior deles.
# 5. Peça ao utilizador para introduzir um número e verifique se ele está entre 10 e 20 (inclusive).

n1 = int(input("Please, insert an integer: "))
print(f"The number is {'even' if n1 % 2 == 0 else 'odd'}")

n2 = int(input("Please, insert an integer: "))
print(f"The number is {'not' if n2 % 5 != 0 else ''} multiple of 5.")

n3 = int(input("Please, insert one integer: "))
n4 = int(input("Please, insert another integer: "))
n5 = int(input("Please, insert the third integer: "))

if n3 >= n4 and n3 >= n5:
    print(f"{n3} is the bigger number.")
elif n4 >= n3 and n4 >= n5:
    print(f"{n4} is the bigger number.")
else:
    print(f"{n5} is the bigger number.")

n6 = int(input("Please, insert the last integer: "))
print("Is between 10 and 20" if 10 <= n6 <= 20 else "Is not between 10 and 20")