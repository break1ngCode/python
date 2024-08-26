# Exercício 8.1: Leitura de Ficheiro
#
# 1. Crie um ficheiro de texto chamado text.txt contendo algumas linhas de texto.
# 2. Escreva um programa que leia o conteúdo do ficheiro e imprima cada linha.
# 3. Modifique o programa para contar e imprimir o número de linhas no ficheiro.
# 4. Modifique o programa para contar e imprimir o número de palavras no ficheiro.
# 5. Modifique o programa para procurar uma palavra específica no ficheiro.

with open('./data/ex1.txt', 'r') as file:
    text = file.readlines()
    words = 0
    for line in text:
        line_without_breaks = line.rstrip()
        print(line_without_breaks)
        words += len(line_without_breaks.split(" "))

        if 'its' in line_without_breaks.lower():
            print(f"\n('its' is in {line_without_breaks})\n")

    
    print(f"\nNumber of lines: {len(text)}")
    print(f"\nNumber of words: {words}")