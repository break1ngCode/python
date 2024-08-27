# Exercício 9.2: Operações com Dicionários
# 
# Crie um dicionário com 5 pares de chave-valor representando nomes de alunos e as suas notas.
# Imprima o nome e a nota de cada aluno.
# Calcule e imprima a média das notas dos alunos.
# Encontre e imprima o nome do aluno com a pior nota.
# Adicione uma nova entrada ao dicionário e imprima o dicionário atualizado

students = { "Alice": 20, "Bob": 19, "Charles": 18, "Dwight":  17, "Evelyn": 16 }

print("First approach: ")
for name in students:
    print(f"{name}: {students[name]}")

print("\nAnother approach: ")
grades_sum = 0
for name, grade in students.items():
    grades_sum += grade
    print(f"{name}: {grade}")

print(f"\nAverage grade: {grades_sum / len(students)}")

worst_grade = (None, 20) # default tuple
for name, grade in students.items():
    if grade < worst_grade[1]:
        worst_grade = (name, grade)

print(f"\nWorst grade - {worst_grade[0]} with only {worst_grade[1]}")

students["Frank"] = 9.5

print(f"\nUpdated dictionary: {students}")