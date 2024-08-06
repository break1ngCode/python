# Exercício 3.2: Métodos de Strings
#
# 1. Crie uma string chamada phrase e atribua-lhe a frase "Aprender Python é divertido!".
# 2. Converta a string para maiúsculas, minúsculas e conte quantas vezes a letra 'e' aparece na frase.
# 3. Substitua a palavra "divertido" por "interessante" na string phrase.
# 4. Divida a string phrase em uma lista de palavras.
# 5. Peça ao utilizador para introduzir uma frase e inverta a ordem das palavras na frase.

phrase = "Aprender Python é divertido!"
phrase_uppercase = phrase.upper()
phrase_lowercase = phrase.lower()
count_e = phrase.count('e')

print(phrase_uppercase)
print(phrase_lowercase)
print(f"A frase tem a letra 'e' {count_e} vezes")

phrase = phrase.replace("divertido", "interessante")
print(phrase)

words = phrase.split(" ")
print(f"Palavras: {words}")

user_phrase = input("Escreva uma frase: ")

user_reverse_phrase = " ".join(reversed(user_phrase.split(" ")))

print("Frase invertida: " + user_reverse_phrase)