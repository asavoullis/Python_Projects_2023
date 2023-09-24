# super and inheritance


class Base:
    @classmethod
    def f(self, x):
        print("Base.f", self, x)

class Derived(Base):
    # using @classmethod will automatically pass in the class instead of an instance
    @classmethod
    def f(self, x):
        print("Derived.f", self, x)

        # instead of copy pasting code from the base class which introduces redundant code and is also very error-prone
        # print("Base.f", self, x)
        # we instead use super

        # this is going to call base.f(x)
        super().f(x)
        # do not use super().f(self, x) because its automatically filled
        print("Derived.f finished")


# suppose we want a logging dictionary
class LoggingDict(dict):
    """
    I want it to be usuable exactly like a dictionary but when i get set or delete a key, I want a logging message to standard out
    Instead of trying to implement our own dictionary, we just inherit from the built-in dict 
    and then use super in the setitem, getitem and delitem methods
    """
    def __setitem__(self, key, value):
        # logging message
        print(f'Setting {key}: {value}')
        # the super call ensures that the real dictionary functionality still goes through
        super().__setitem__(key, value)
    
    def __getitem__(self, item):
        print(f'Getting {item}')
        return super().__getitem__(item)
    
    def __delitem__(self, key):
        super().__delitem__(key)

    # in just a few lines of code, super allowed us to have fully functioning dictionary that also gives us logging messages

    
class B():
    def f(self):
        print("B.f", self)
        super().f()


# https://youtu.be/KSiRzuSx120
if __name__ == "__main__":
    d = Derived()
    d.f(42)
    print("\n")

    print("LOGGING DICT EXAMPLE")
    # creating an instance of the loggingdictionary
    d = LoggingDict()
    # set the value of d[0] to subscribe
    d[0] = "subscribe"
    # print the dictionary
    print(d)
    # grabbing the value of d[0]
    x = d[0]
    # delete the dict
    del d[0]
    print()


    b = B()
    b.f()