# Exercício 8.3: Leitura e Escrita em Ficheiro CSV
#
# 1. Crie um ficheiro CSV chamado ex3.csv com os cabeçalhos "Nome", "Idade", "Cidade".
# 2. Escreva um programa que adicione uma nova linha ao ficheiro CSV com dados fornecidos pelo utilizador.
# 3. Modifique o programa para adicionar várias linhas ao ficheiro CSV com um loop.
# 4. Escreva um programa que leia todas as linhas do ficheiro CSV e imprima cada linha no terminal.
# 5. Modifique o programa para contar e imprimir o número total de linhas no ficheiro CSV (excluindo o cabeçalho).

with open('./data/ex3.csv', 'a') as f:
    
    while True:

        name = input("Your name: ")
        age = input("Your age: ")
        city = input("Your city ('quit' to stop): ")

        if city == 'quit':
            break

        f.write(f'{name},{age},{city}\n')
    
    f.close()

with open('./data/ex3.csv', 'r') as f:
    
    lines = f.readlines()
    for line in lines:
        print(line.rstrip())
    
    print(f"Number of lines: {len(lines[1:])}")
    
    f.close()