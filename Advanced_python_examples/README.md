# Python Script Documentation

This repository contains Python scripts demonstrating various concepts and features, along with explanations. Below, you'll find documentation for each script.

- 1.OOP_dunders_magic_generators.py
- 1.OOP_v2.py
- 2.Decorators.py
- 3.Exceptions_File_Operations.py

##

## OOP_dunders_magic_generators.py

### Description

This Python script provides examples and explanations of object-oriented programming concepts, dunders (double underscores) and magic methods, as well as other Python features such as decorators and generators.

### Classes

- `Person`: Represents a person with `name` and `age` attributes. Demonstrates constructor and destructor methods.
- `Vector_v1`: Represents a 2D vector with `x` and `y` components. Overloads addition and subtraction operators.
- `Vector`: Improved version of the `Vector_v1` class with additional magic methods for customization.
- `Person2` and `Person3`: Examples of class definitions with different approaches for representing a person.
- `User`: Demonstrates private methods using name mangling.
- `Base` and `Derived`: Illustrates inheritance and the use of `super()` to call methods from base classes.

### Usage

To run the script and see the examples in action, execute the following command:

```bash
python 1.OOP_dunders_magic_generators.py
```

##

## OOP_v2.py

### Description

### Super and Inheritance

This Python script provides examples and explanations of inheritance and the use of the `super()` function.

### Classes

### `Base` and `Derived`

- `Base` class defines a class method `f(self, x)` that prints a message.
- `Derived` class inherits from `Base` and overrides the `f(self, x)` method to add functionality and demonstrate the use of `super()` to call the parent class's method.

### `LoggingDict`

- Class `LoggingDict` inherits from the built-in `dict` class.
- It overrides the `__setitem__`, `__getitem__`, and `__delitem__` methods to log messages when setting, getting, or deleting dictionary items.
- The use of `super()` ensures that the original dictionary functionality is preserved.

### `B`

- Class `B` defines a method `f(self)` and demonstrates the use of `super()` within a method.

### Usage

To run the script and see the examples in action, execute the following command:

```bash
python 1.OOP_v2.py
```

##

## Decorators and Wrapper Functions

This Python script provides an example of decorators and wrapper functions, demonstrating how decorators can be used to add functionality to functions.

## Decorators

### `mydecorator`

- `mydecorator` is a decorator function used to decorate other functions.
- It defines a wrapper function inside, which adds functionality and then calls the original function.

### `helloworld`

- `helloworld` is a sample function that prints "Hello World!"

### Using the Decorator

To demonstrate the use of the decorator, the script applies `mydecorator` to the `helloworld` function and invokes it.

### Error Handling

The script also includes examples of error handling using `try`, `except`, and `finally` blocks.

- It attempts to open a file ("example.txt") and handles exceptions related to file not found.
- It takes user input, performs division, and handles exceptions for zero division, invalid input, and general exceptions.
- A `finally` block is used to ensure certain code is executed regardless of whether an exception was raised.

### Usage

To run the script and see the examples in action, execute the following command:

```bash
python 2.Decorators.py
```

##

## File Handling and Exceptions

### Description

This Python script provides examples of file operations and exception handling.

### File Operations

### Reading and Writing Files

- The script demonstrates reading and writing files using the `open()` function.
- If the file "myfile.txt" exists, it reads its content; otherwise, it creates the file and writes "Hello" to it.
- It also uses the `with` statement for file handling, eliminating the need to manually close the file.

### Reading CSV Files

- The script attempts to read a CSV file ("myfile.csv") and prints the first few lines.
- If the file doesn't exist, it creates an empty file.

### Renaming Files

- There's an example of renaming a file from "myfile.txt" to "newfile.txt."

### Exception Handling

- The script demonstrates exception handling using `try`, `except`, and `finally` blocks.
- It handles `ValueError` and `ZeroDivisionError` exceptions for user input.
- It raises a custom exception (`ValueError`) using the `raise` statement in the `some_function()`.

### Validating User Input

- The script validates user input by using a `while` loop and prompting the user to enter valid numbers.

### Usage

To run the script and see the examples in action, execute the following command:

```bash
python 3.Exceptions_File_Operations.py
```
