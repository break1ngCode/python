# Exercício 6.2: Operações com Listas
#
# 1. Crie uma lista com 5 números inteiros e calcule a soma de todos os elementos.
# 2. Encontre o maior e o menor número na lista.
# 3. Ordene a lista por ordem crescente e decrescente.
# 4. Crie uma lista de palavras e verifique se uma palavra específica está na lista.
# 5. Peça ao utilizador para introduzir 5 números e armazene-os em uma lista. Depois, imprima a lista.

numbers = [1,3,4,5,2]

print(f"Sum of list: {sum(numbers)}")

print(f"Biggest number on the list: {max(numbers)}")
print(f"Lowest number on the list: {min(numbers)}")

numbers.sort()
print(f"Ascending ordered list {numbers}")
numbers.sort(reverse=True)
print(f"Descending ordered list {numbers}")

words = ["I", "love", "coding", "in", "Python"]

if "love" in words:
    print("'love' is in words.")

if not "Java" in words:
    print("'Java' is not in words")


user_numbers = []
for _ in range(5):
    n = int(input("Please insert a number: "))
    user_numbers.append(n)

print(f"Inserted numbers: {user_numbers}")