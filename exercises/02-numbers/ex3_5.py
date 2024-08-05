# 5. Modifique o programa para calcular e imprimir a média de uma quantidade variável de números fornecidos pelo utilizador.

n = int(input("Números a ler: "))
total_sum = 0
for i in range(n):
    number = int(input(f"Número {i+ 1}: "))
    total_sum += number

print("A média total é de " + str(total_sum / n))