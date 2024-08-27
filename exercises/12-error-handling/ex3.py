# Exercício 12.3: Manipulação de ficheiros com Tratamento de Erros
# 
# 1. Escreva um programa que tente abrir um ficheiro para leitura cujo nome é fornecido pelo utilizador.
# 2. Utilize um bloco try/except para tratar o erro caso o ficheiro não exista e imprima uma mensagem apropriada.
# 3. Modifique o programa para também tratar erros de permissão de leitura e outros erros gerais de I/O, imprimindo mensagens apropriadas para cada caso.


def read_file(filename, mode = 'r+'):
    try:
        with open(filename, mode) as f:
            lines = f.readlines()
            print("File opened successfully!")
            for line in lines:
                print(line.rstrip())
    except FileNotFoundError:
        print(f"{filename} was not found!")
    except PermissionError:
        print(f"You don't have permissions to open '{filename}'")

read_file('ex3-valid.txt')
read_file('ex3-does-not-exist.txt')
read_file('ex3-invalid.txt')
