# Exercício 9.3: Dicionário de Contagem
#
# 1. Peça ao utilizador para introduzir uma frase.
# 2. Crie um dicionário onde as chaves são as palavras da frase e os valores são a contagem de ocorrências de cada palavra.
# 3. Imprima o dicionário resultante.
# 4. Modifique o programa para ignorar a capitalização das palavras (tratar "Python" e "python" como a mesma palavra).
# 5. Modifique o programa para remover pontuações antes de contar as palavras.
import re

def get_words(text):
    # Use regular expression to find all words without punctuation and spaces
    words = re.findall(r"\b\w+(?:'\w+)?\b", text)
    return words

text = input("Please insert a phrase: ")

words_list = get_words(text)

occurrences = {}
for word in words_list:
    lowercase_word = word.lower()
    if lowercase_word not in occurrences:
        occurrences[lowercase_word] = 0
    
    occurrences[lowercase_word] += 1

print(f"Occurrences: {occurrences}")