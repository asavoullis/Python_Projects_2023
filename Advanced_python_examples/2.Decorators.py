# Decorators and Wrapper functions
# making code more resuable, readable and scalable - effective
# decorators generators functional python etc 

class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # destructor
    def __del__(self):
        """
        whenever the object is destroyed we get this printed out
        """
        print("Object is being deconstructed/deleted!")

    def __repr__():
        return


class Vector_v1:
    """
    We now have this vector class and we probably want know how to deal with vectors but our python script doesn't
    It doesn't know what a vector is and doesn't know what x and y is and how to deal with them
    We therefore need to define the operation (see __add__ method below)
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # operator overloading (we haven't overloaded that particular operator yet)
    # we don't have the definition of + so lets define it here
    # in this case other also has to be a vector
    def __add__(self, other):
        return Vector_v1(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector_v1(self.x - other.x, self.y - other.y)

    # other examples:
        # def __mul__(self, other):
        # def __div__(self, other):

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    # magic method
    # lets now define in the class how we want the vector to be represented
    # the str method defines what happens when i typecast the vector into a string
    # def __str__(self):

    # using the representation method we tell it how to represent a vector when we need to represent it
    def __repr__(self) -> str:
        return f"X: {self.x}, Y: {self.y}"

    # this triggers when you apply the length function onto a vector object
    def __len__(self):
        return 10

    # this triggers when you call the object 
    def __call__(self):
        print("hello i was called")

# this is how you call the init method
# https://youtu.be/KSiRzuSx120
if __name__ == "__main__":
    p = Person("Mike", 25)

    # to manually delete the object
    del p
    print("\n")

    v1 = Vector_v1(10, 20)
    v2 = Vector_v1(50, 60)
    v3 = v1 + v2
    print("v3:")
    print(v3.x)
    print(v3.y,"\n")

    print("v4:")
    v4 = v1 - v2
    print(v4.x)
    print(v4.y)
    # lets now represent the vector for example check what happens when we try to print the vector 
    # and not just its x and y attributes
    # we get the vector object just a message telling us okay this is an object of the class vector_v1 at that location
    # it doesn't tell us anything about its attributes or values
    print(v4, "\n") 

    print("v7:")
    v5 = Vector(10, 20)
    v6 = Vector(50, 60)
    v7 = v5 + v6
    print(v7)
    # this is calls the __len__ method of the class
    print(len(v7))
    # in python you call objects like functions, for example like below
    v7()