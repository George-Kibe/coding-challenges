"""
Encapsulation
Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit or class, while restricting direct access to some of the object’s components.
"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Alice")
account.deposit(100)
account.withdraw(40)
print(account.get_balance())  # Output: 60
# print(account.__balance) # → Error: AttributeError


"""
Abstraction
Abstraction hides the complex implementation details and shows only the essential features of the object.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())


"""
Inheritance
Inheritance allows a class (child or subclass) to inherit attributes and methods from another class (parent or superclass).
"""

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return f"{self.brand} is moving"

class Car(Vehicle):
    def drive(self):
        return f"{self.brand} car is driving"

my_car = Car("Toyota")
print(my_car.drive())  # Output: Toyota car is driving



"""
Polymorphism
Polymorphism allows objects of different classes to be treated through the same interface, typically via method overriding or duck typing.
"""

class Bird:
    def fly(self):
        return "Flying in the sky"

class Airplane:
    def fly(self):
        return "Flying through engines"

def let_it_fly(entity):
    print(entity.fly())

let_it_fly(Bird())       # Output: Flying in the sky
let_it_fly(Airplane())   # Output: Flying through engines
