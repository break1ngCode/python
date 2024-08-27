# Exercício 11.2: Herança
# 
# 1. Crie uma classe chamada Employee que herde da classe Person e adicione o atributo salary.
# 2. Crie um método na classe Employee chamado raise que aumente o salário do funcionário em uma determinada percentagem.
# 3. Crie uma instância da classe Employee, ajuste o salário e chame o método raise.

from ex1 import Person

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    def give_raise(self, percentage):
        self.salary = self.salary * (1 + (percentage / 100))

employee1 = Employee("Bob", 25, 45000)
employee1.give_raise(50)

print(f"Salary after raise: {employee1.salary}")