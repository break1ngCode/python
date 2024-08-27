# Exercício 11.3: Polimorfismo
#
# 1. Crie uma classe chamada Animal, com nome, espécie, e com um método chamado make_sound que imprime "O animal faz um som".
# 2. Crie subclasses Dog e Cat que herdam de Animal e sobrescrevam o método make_sound para imprimir "O cachorro late" e "O gato mia", respectivamente.
# 3. Crie instâncias de Dog e Cat e chame o método make_sound para cada uma delas.

class Animal:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Some generic sound!")

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name, "Dog")
    
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name, "Cat")
    
    def make_sound(self):
        print("Miau!")

dog = Dog("Bobby")
cat = Cat("Garfield")

dog.make_sound()
cat.make_sound()