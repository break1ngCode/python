# Exercício 3.1: Concatenar Strings
# 
# 1. Crie duas variáveis de string, first_name e last_name.
# 2. Concatene as duas variáveis com um espaço entre elas e imprima o nome completo.
# 3. Peça ao utilizador para introduzir o seu primeiro e último nome e imprima o nome completo em maiúsculas.
# 4. Peça ao utilizador para introduzir o seu nome completo e imprima o número total de caracteres (incluindo espaços).
# 5. Peça ao utilizador para introduzir uma frase e verifique se a palavra "Python" está presente na frase.

first_name = "breaking"
last_name = "Code"
full_name = first_name + " " + last_name + "."

user_first_name = input("Introduza o seu primeiro nome: ")
user_last_name = input("Introduza o seu último nome: ")
print("O seu nome é: " + (user_first_name + " " + user_last_name).upper())

user_full_name = input("Introduza o seu nome completo: ")
print(f"O seu nome tem {len(user_full_name)} caracteres")

phrase = input("Por favor, introduza uma frase: ")

if "Python" in phrase:
    print("Python está na frase!")
else:
    print("Python não está na frase.")