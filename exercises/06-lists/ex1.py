# Exercício 6.1: Criação e Acesso a Listas
#
# 1. Crie uma lista chamada fruits contendo as frutas: maçã, banana, cereja, damasco.
# 2. Imprima o primeiro e o último elemento da lista.
# 3. Adicione a fruta 'kiwi' à lista fruits.
# 4. Remova a fruta 'banana' da lista.
# 5. Imprima a lista atualizada.


fruits = ["Apple", "Banana", "Cherry", "Damascus"]

print(f"First element: {fruits[0]}")
print(f"Last element: {fruits[-1]}")

fruits.append('Kiwi')

fruits.remove("Banana")

print("Updated list: " + str(fruits))