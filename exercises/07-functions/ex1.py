# Exercício 7.1: Função de Saudação
#
# 1. Escreva uma função chamada greeting que receba um name como parâmetro e imprima "Olá, name!".
# 3. Modifique a função para receber também a idade e imprimir "Olá, name, você tem age anos."
# 4. Escreva uma função que receba um nome e uma saudação como parâmetros e imprima a saudação seguida do nome.
# 5. Crie uma função que não receba parâmetros e apenas imprima "Olá, Mundo!".
# 6. Crie uma função que receba uma lista de nomes e imprima uma saudação para cada nome na lista.

def greeting(greeting, name, age):
    print(f"{greeting}, {name}, you're {age} years old.")

def hello_world():
    print("Hello World!")

def greeting_multiple(names):
    for name in names:
        print(f"Hello, {name}!")

greeting("Hi", "Cristiano", 39)
hello_world()
greeting_multiple(["Cristiano", "Messi", "Neymar"])