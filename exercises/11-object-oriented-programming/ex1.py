# Exercício 11.1: Classes e Objetos
#
# 1. Crie uma classe chamada Person com os atributos name e age.
# 2. Crie um método na classe Person chamado greeting que imprima "Olá, meu nome é name e eu tenho age anos."
# 3. Crie uma instância da classe Person e chame o método greeting.

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def greeting(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} year{'s' if self.age > 1 else ''} old.")

if __name__ == '__main__':
    p1 = Person("Ronaldo", 39)
    p2 = Person("Messi", 1)

    p1.greeting()
    p2.greeting()