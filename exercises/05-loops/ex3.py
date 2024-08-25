# Exercício 5.3: Soma de Números

# 1. Peça ao utilizador para introduzir números inteiros até que ele introduza '0'.
# 2. Calcule e imprima a soma de todos os números introduzidos.
# 3. Modifique o programa para também calcular e imprimir a média dos números introduzidos.
# 4. Implemente uma verificação para garantir que o utilizador introduza apenas números inteiros.
# 5. Adicione uma opção para o utilizador reiniciar a soma e começar a introduzir números novamente.

n = None
numbers_sum = 0
iterations = 0
while True:
    n = input("Insert an integer (0 to stop, negative to restart): ")
    
    try:
        n = int(n)
        
        if n == 0:
            break
        
        if n < 0:
            numbers_sum = 0
            iterations = 0
            continue
        
        numbers_sum += n
        iterations += 1
    except ValueError:
        print("The number should be an integer!")

print(f"The sum is: {numbers_sum}")
print(f"The mean is: {numbers_sum / iterations}")