# Exercício 3.3: Fatiamento de Strings
#
# 1. Crie uma string chamada word e atribua-lhe o valor "Programação".
# 2. Imprima os três primeiros caracteres da string word.
# 3. Imprima os três últimos caracteres da string word.
# 4. Imprima a string word ao contrário.
# 5. Peça ao utilizador para introduzir uma palavra e imprima cada caractere da palavra em uma nova linha.

word = "Programação"

print("Três primeiros caracteres: " + word[0:3])
print("Três últimos caracteres: " + word[::-1][0:3])
print("String invertida: " + word[::-1])

user_word = input("Introduza uma palavra: ")
for char in user_word:
    print(char)