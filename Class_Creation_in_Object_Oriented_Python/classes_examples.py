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

# assigning default attributes to instances of the object
class Car_default:
    make = "buick"
    model = "lesabre"
    color = "red"
    year = 2013
    price = 10000


# constructor function __init__ 
class Car:
    # if instance of the object is not passed a particular attribute then default option is chosen
    def __init__(self, make = "unkown", model = "unknown", color = "unknown", year = -1, price = -1):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
    



car1 = Car_default()
car2 = Car()
car3 = Car("mazda", "mx5", "red", "2000", "15000")

print("\nModel = " + car1.model)
print("\n", car2.model)
print("\n", car3.model, "£" + car3.price)

