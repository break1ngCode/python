# Exercício 6.3: Lista de Compras
#
# 1. Crie uma lista chamada groceries com alguns itens de supermercado.
# 2. Adicione um item à lista de compras.
# 3. Remova um item da lista de compras.
# 4. Verifique se um item específico está na lista.
# 5. Peça ao utilizador para introduzir itens até que ele introduza 'sair' e adicione cada item à lista de compras. Imprima a lista final.

groceries = ["Sugar", "Pasta", "Apple", "Meat", "Potatoes", "Chocolate"]

groceries.append("Rice")
groceries.remove("Pasta")

if "Apple" in groceries:
    print("'Apple' is in groceries")

while True:
    item = input("Please insert an item (type 'quit' to stop): ")

    if item == "quit":
        break

    groceries.append(item)

print(f"Groceries list: {groceries}")
