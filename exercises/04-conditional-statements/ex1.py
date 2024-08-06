# Exercício 4.1: Verificar Maioridade
#
# 1. Peça ao utilizador a sua idade.
# 2. Verifique se a pessoa é maior de idade (18 anos ou mais) e imprima uma mensagem apropriada.
# 3. Peça ao utilizador a idade e verifique se a pessoa é um adolescente (entre 13 e 19 anos).
# 4. Peça ao utilizador para introduzir duas idades e verifique qual é a maior.
# 5. Peça ao utilizador uma nota (0 a 100) e imprima a letra correspondente (A, B, C, D, F).

age = int(input("Please, enter your age: "))

if age >= 18:
    print("You are older than 18 years old.")
elif 13 <= age <= 19:
    print("You are a teenager.")
else:
    print("You are a child.")


age_1 = int(input("Please, enter one age: "))
age_2 = int(input("Please, enter another age: "))

if age_1 > age_2:
    print(f"{age_1} is greater than {age_2}.")
elif age_1 < age_2:
    print(f"{age_1} is less than {age_2}.")
else:
    print(f"{age_1} and {age_2} are equal.")


grade = float(input("Insert a grade between 0 and 100: "))

if 80 < grade <= 100:
    print("A")
elif 60 < grade <= 80:
    print("B")
elif 40 < grade <= 60:
    print("C")
elif 20 < grade <= 40:
    print("D")
elif grade > 100:
    print("Grade can't be greater than 100.")
else:
    print("E")
