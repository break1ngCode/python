# Exercício 2.2: Cálculo de Área
#
# Escreva um programa que peça ao utilizador o comprimento e a largura de um retângulo e calcule a área.
# Modifique o programa para calcular o perímetro do retângulo.
# Peça ao utilizador o raio de um círculo e calcule a área (use π = 3.14159).
# Modifique o programa para calcular o perímetro de um círculo.
# Peça ao utilizador a base e a altura de um triângulo e calcule a respetiva área.

import math

width = float(input('Introduza a largura de um retângulo: '))
height = float(input('Introduza a altura de um retângulo: '))

area = width * height
perimeter = width * 2 + height * 2
print(f"A área do retângulo é {area:.2f} e o perímetro é {perimeter:.2f}.")

radius = float(input('Introduza o raio de um círculo: '))
circle_area = math.pi * radius ** 2
circle_perimeter = 2 * math.pi * radius
print(f"A área do círculo é {circle_area:.2f} e o perímetro é {circle_perimeter:.2f}")

triangle_base = float(input('Introduza a base de um triângulo: '))
triangle_height = float(input('Introduza a altura de um triângulo: '))
triangle_area = (triangle_base * triangle_height) / 2
print(f"A área do triângulo é {triangle_area:.2f}")
