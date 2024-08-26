# Exercício 8.2: Escrita em Ficheiro
# 
# 1. Escreva um programa que peça ao utilizador para introduzir uma frase.
# 2. Guardar a frase introduzida em um ficheiro chamado 'ex2.txt'.
# 3. Modifique o programa para permitir que o utilizador introduza várias frases, salvando cada uma em uma nova linha no ficheiro.
# 4. Modifique o programa para adicionar as novas frases no final do ficheiro existente, sem sobrescrever o conteúdo.
# 5. Crie um programa que leia o ficheiro output.txt e imprima todo o seu conteúdo.


with open('./data/ex2.txt', 'a') as f:
    while True:
        phrase = input("Insert a phrase ('quit' to stop): ")

        if phrase == 'quit':
            break
        
        f.write(phrase + '\n')
    
    f.close()

with open('./data/ex2.txt', 'r') as f:
    text = f.readlines()
    for line in text:
        print(line.rstrip())
