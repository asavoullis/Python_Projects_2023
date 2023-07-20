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
        self._price = price

    # getter
    @property
    def price(self):
        return self._price
    
    # setter
    @price.setter
    def price(self, p):
        if (p <= 0):
            raise ValueError("Price is zero or less!")
        print("Setter for price called")
        self._price = p
    

# Example of Task3: 
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


# Task 4: Create String Representation
class Car_adv2:
    """
    Use str method to create a string representation of the object __str__
    """
    def __init__(self, make = "unkown", model = "unknown", color = "unknown", year = -1, price = -1):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self._price = price
    
    # getter
    @property
    def price(self):
        return self._price
    
    # setter
    @price.setter
    def price(self, p):
        if (p <= 0):
            raise ValueError("Price is zero or less!")
        print("Setter for price called")
        self._price = p

    def __str__(self):
        return "car(make = " + self.make + ", model = " + str(self.model) + ", color = " + str(self.color) + ", year = " + str(self.year) + ", price = " + str(self.price) + ")"


# Task 5: Sorting Objects
class Car_adv3:
    """
    Read data from file
    Extract data from each entry
    Create the object from the entry
    Add the object to the list
    Sort the list of objects and print them
    """
    def __init__(self, make = "unkown", model = "unknown", color = "unknown", year = -1, price = -1):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self._price = price
    
    # getter
    @property
    def price(self):
        return self._price
    
    # setter
    @price.setter
    def price(self, p):
        if (p <= 0):
            raise ValueError("Price is zero or less!")
        print("Setter for price called")
        self._price = p

    def __str__(self):
        return "car(make = " + self.make + ", model = " + str(self.model) + ", color = " + str(self.color) + ", year = " + str(self.year) + ", price = " + str(self.price) + ")"




car1 = Car_default()
car2 = Car()
car3 = Car("mazda", "mx5", "red", "2000", "15000")


print("\nModel = " + car1.model)
print("\n" + car2.model)
print("\n" + car3.model, "£" + car3.price)

# Example usage:
p = Product("Widget", 15)
print("\n"+ p.get_details())

p.price = 20  # Setting the price using the setter
print(p.price)  # Output: 20


car4 = Car_advanced()
print("\n" + "Model =" + car4.model)
car4.price = 1000
# ca4.price = -1 # This will raise an error
car5 = Car_advanced("mazda", "mx5", "red", 2013, 1000)
print("\n" + "Model =" + car5.model)


car6 = Car_adv2("bmw", "m4", "green", 2010, 45000)
print("\n" + "Model =" + car6.model)
print("\n"+"Car:"+ str(car6) + "\n")


fh = open("cars.csv", "r")
cars_data = fh.readlines()
cars_data.pop(0)
cars_list = []
for rawstring in cars_data:
    make,model,color,year,price = rawstring.split(",")
    cars_list.append(Car_adv3(make,model,color,int(year),float(price)))

cars_list.sort(key = lambda car: car.price)
print(*cars_list, sep="\n")