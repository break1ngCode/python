# Exercício 2.3: Média de Números
# 
# 1. Peça ao utilizador para introduzir três números.
# 2. Calcule e imprima a média desses números.
# 3. Modifique o programa para pedir ao utilizador cinco números.
# 4. Calcule e imprima a média desses cinco números.

first_number = int(input("Introduza o primeiro número: "))
second_number = int(input("Introduza o segundo número: "))
third_number = int(input("Introduza o terceiro número: "))

first_average = (first_number + second_number + third_number) / 3
print("A média dos três números é " + str(first_average))

fourth_number = int(input("Introduza o quarto número: "))
fifth_number = int(input("Introduza o quinto número: "))

second_average = ((first_average * 3) + fourth_number + fifth_number) / 5
print("A média dos cinco números é " + str(second_average))
