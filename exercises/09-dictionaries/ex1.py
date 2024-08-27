# Exercício 9.1: Criação e Acesso a Dicionários
#
# 1. Crie um dicionário chamado student com as chaves name, age e course.
# 2. Atribua valores a essas chaves e imprima o valor correspondente à chave course.
# 3. Adicione uma nova chave grade com um valor numérico ao dicionário student.
# 4. Remova a chave age do dicionário.
# 5. Imprima o dicionário atualizado.

student = {"name": "Bob", "age": 21, "course": "Software Engineering"}

# Other implementation: student = dict(name="Bob", age=21, course="Software Engineering")

student["grade"] = 20

print(f"Student: {student}")

del student["age"]

print(f"Student without 'age': {student}")
