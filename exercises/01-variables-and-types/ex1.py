# Exercício 1.1: Variáveis Simples
#
# Crie uma variável chamada name e atribua-lhe o seu próprio nome.
# Crie uma variável chamada age e atribua-lhe a sua própria idade.
# Crie uma variável chamada city e atribua-lhe o nome da cidade onde mora.
# Imprima uma frase que diga "Olá, meu nome é name, tenho age anos e moro em city."
# Crie uma variável chamada current_year e outra chamada birth_year. 
# Calcule a idade baseada nesses valores e verifique se coincide com a idade fornecida.

name = 'Ronaldo'
age = 39
city = 'Doha'

print('Olá, o meu nome é ' + name + ', tenho ' + str(age) + ' anos e moro em ' + city + '.')

current_year = 2024
birth_year = 1985

print('Idade: ' + str(current_year - birth_year))