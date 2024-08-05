# Exercício 1.2: Conversão de Tipos
#
# Crie uma variável height e atribua-lhe um valor em metros (ex: 1.75).
# Converta a altura de metros para centímetros e imprima o resultado.
# Peça ao utilizador para introduzir a sua altura e converta o valor para um número de ponto flutuante.
# Calcule e imprima a altura do utilizador em polegadas (1 metro = 39.3701 polegadas).
# Peça ao utilizador para introduzir a respetiva idade e verifique se o tipo da variável é int.

height = 1.75

print("Altura em centímetros: " + str(1.75 * 100))

user_height = float(input("Por favor introduza a sua altura em metros: "))
print("A sua altura em polegadas é: " + str(user_height * 39.3701))

user_age = input("Por favor introduza a sua idade: ")
print(type(user_age))
