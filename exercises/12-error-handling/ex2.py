# Exercício 12.2: Tratamento de Erros em Funções
#
# 1. Escreva uma função chamada read_int que peça ao utilizador para introduzir um número inteiro.
# 2. Utilize um bloco try/except dentro da função para tratar entradas inválidas e peça ao utilizador para tentar novamente até que um número inteiro válido seja introduzido.
# 3. Chame a função e imprima o número inteiro fornecido pelo utilizador.

def read_int():
    while True:
        try:
            n = int(input("Insert an integer: "))
            break
        except:
            print("Please, insert a valid integer.")
    return n


print(read_int())