"""
A class is a blueprint for creating objects.
An object is an instance of a class.
A class has attributes and methods.
An attribute is a variable that belongs to a class.
A method is a function that belongs to a class.
A class can have a constructor, which is a special method that is called when an object is created.
"""
# A class is a blueprint for creating objects.


class Microwave:
    # constructor
    def __init__(self, brand: str, model: str, price: float, power_rating: str, capacity: int, turned_on: bool = False ) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.power_rating = power_rating
        self.capacity = capacity
        self.turned_on = turned_on

    def turn_on(self):
        if self.turned_on:
            print(f'{self.brand} {self.model} is already on')
        else:
            self.turned_on = True
            print(f'{self.brand} {self.model} is now on')
    def run(self, seconds: int):
        if self.turned_on:
            print(f'{self.brand} {self.model} is running for {seconds} seconds')
        else:
            print(f'{self.brand} {self.model} is not on')
    
    def __add__(self, other):
        if isinstance(other, Microwave):
            return self.price + other.price
    def __str__(self):
        return f'{self.brand} {self.model} is $USD {self.price}'
    
smeg_microwave: Microwave = Microwave("Smeg", "M1000", 1000, "1000W", 10)

print(smeg_microwave)