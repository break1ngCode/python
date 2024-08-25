# Exercício 5.2: Tabuada
#
# 1. Peça ao utilizador um número inteiro.
# 2. Imprima a tabuada desse número de 1 a 10.
# 3. Modifique o programa para imprimir a tabuada de 1 a 10 para todos os números de 1 a 5.
# 4. Peça ao utilizador um número e imprima a tabuada desse número de 1 a 20.
# 5. Crie uma função que receba um número e um intervalo (início e fim) e imprima a tabuada do número nesse intervalo.

user_number = int(input("Insert an integer: "))

print(f"Multiplication table of {user_number}:")
for n in range(11):
    print(f"{n} x {user_number} = {n * user_number}")

for i in range(1, 6):
    print(f"\nMultiplication table of {i}:")
    for j in range(11):
        print(f"{j} x {i} = {j * i}")

user_number = int(input("\nInsert an integer: "))
print(f"Multiplication table of {user_number} until 20:")
for n in range(21):
    print(f"{n} x {user_number} = {n * user_number}")

def multiplication_table(factor, start, stop):
    print(f"\nMultiplication table of {factor} from {start} until {stop}:")
    for n in range(start, stop + 1):
        print(f"{n} x {factor} = {n * factor}")


multiplication_table(5, 1, 10)