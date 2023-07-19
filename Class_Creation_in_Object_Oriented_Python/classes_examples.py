"""
How to prepare a class definition
How to create a constructor and Getters and Setters 
How to sort data using objects

Task 1: Create the Class definition based on requirements.
Task 2: Create the Constructor to allow us to create objects with data.
Task 3: Add Getters and Setters to access and modify the attributes.
Task 4: Add a String representation of the object for output.
Task 5: Sort a list of objects.
"""

# Task1: assigning default attributes to instances of the object
class Car_default:
    make = "buick"
    model = "lesabre"
    color = "red"
    year = 2013
    price = 10000


# Task2: constructor function __init__ 
class Car:
    # if instance of the object is not passed a particular attribute then default option is chosen
    def __init__(self, make = "unkown", model = "unknown", color = "unknown", year = -1, price = -1):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
    

# Task 3: getters and setters
class Car_advanced:
    """
    Getters provide access control 
    Setters provide provide protection for the attributes
    There are no "private" attributes in python but we use _ to indicate that this attribute should not be changed
    @something are decorators
    """
    def __init__(self, make = "unkown", model = "unknown", color = "unknown", year = -1, price = -1):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    # @property
    # def price(self):
    #     return self.price
    

# Example 4: 
class Product:
    # constructor function
    def __init__(self, name, price):
        self._name = name
        self._price = price

    # getter 
    @property
    def price(self):
        return self._price

    # set new price - setter
    @price.setter
    def price(self, new_price):
        self._price = new_price

    def get_details(self):
        return f"Product: {self._name}, Price: {self._price}"

car1 = Car_default()
car2 = Car()
car3 = Car("mazda", "mx5", "red", "2000", "15000")
car4 = Car_advanced()

print("\nModel = " + car1.model)
print("\n", car2.model)
print("\n", car3.model, "£" + car3.price)

# Example usage:
p = Product("Widget", 15)
print("\n", p.get_details())

p.price = 20  # Setting the price using the setter
print(p.price)  # Output: 20

