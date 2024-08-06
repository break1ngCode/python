# Exercício 4.3: Verificação de Senha
# 
# 1. Peça ao utilizador para introduzir uma senha.
# 2. Peça ao utilizador para introduzir a senha novamente para confirmação.
# 3. Verifique se as duas senhas introduzidas são iguais e imprima uma mensagem apropriada.
# 4. Implemente uma verificação para garantir que a senha tenha pelo menos 8 caracteres.
# 5. Implemente uma verificação para garantir que a senha contenha pelo menos uma letra maiúscula, uma letra minúscula e um número.

password = input("Insert a top secret password: ")
re_password = input("Insert again a top secret password: ")

if password != re_password:
    print("The passwords do not match!")
    exit(1)

if len(password) < 8:
    print("The password must have at least 8 characters.")
    exit(1)

has_upper = False
has_lower = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True

if not(has_upper and has_lower and has_digit):
    print("The password is not strong enough")
    exit(1)

print("The password meets the requirements.")
