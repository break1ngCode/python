# Exercício 1.3: Valores Booleanos
#
# Crie uma variável student e atribua-lhe um valor booleano indicando se é estudante ou não.
# Imprima a mensagem "Sou estudante" ou "Não sou estudante" baseada no valor da variável.
# Crie uma variável tem_pet e atribua-lhe um valor booleano indicando se tem um animal de estimação.
# Imprima a mensagem "Eu tenho um animal de estimação" ou "Eu não tenho um animal de estimação" baseada no valor da variável.
# Crie uma variável bigger_than_ten que verifica se um dado número introduzido pelo utilizador é maior que 10, imprimindo o resultado.

student = True

if student:
    print("Sou estudante!")
else:
    print("Não sou estudante")

have_pet = False

if have_pet:
    print("Eu tenho um animal de estimação")
else:
    print("Eu não tenho um animal de estimação")

bigger_than_10 = int(input("Por favor introduza um número: "))

if bigger_than_10 > 10:
    print(str(bigger_than_10) + ' é maior que 10')
else:
    print(str(bigger_than_10) + ' não é maior que 10')