# File Operations revision
# from os import *
import os


if __name__ == '__main__':
    try:
        # if the file exists, read it
        file = open("myfile.txt", "r")
        content = file.read()
        print(content)
        file.close()

    # File doesn't exist, so let's create it
    except FileNotFoundError:
        file = open("myfile.txt", "w")
        file.write("Hello")
        # close or flush to save changes
        file.close()

    # use with whenever we work with streams
    # you don't need to close the stram
    try:
        with open("myfile.csv", "r") as file:
            # Read lines and store them in a list
            content = file.readlines()  
            print(content[0])
            for line in content[:2]:
                # strip() removes leading/trailing whitespace and newline characters
                print(line.strip())  
    except FileNotFoundError:
        # File doesn't exist, so let's create it
        with open("myfile.csv", "w") as file:
            pass
        # Writing at the end of the file (append) 
        # If the file doesn't exist it also creates the file
        with open("myfile.txt", "a") as file:
            old_name = "myfile.txt"
            new_name = "newfile.txt"
            os.rename(old_name, new_name)
            # os.remove(old_name)
            file.write("Hello\n")  

    # handling errors and exceptions  
    try:
        x = int(input("First number: "))
        y = int(input("Second number: "))
    except ValueError:
        print("Please enter a valid number next time!")
    except ZeroDivisionError:
        print("Cannot divide by zero")
        y = 1
        print(x / y)
    finally:
        print(x / y)
        print("Done!")

    # V2
    valid_input = False
    while not valid_input:
        try:
            x = int(input("First number: "))
            y = int(input("Second number: "))
            valid_input = True  # Set the flag to True for valid inputs
        except ValueError:
            print("Please enter a valid number!")

    # raising exceptions
    def some_function():
        if True:
            # raising ordinary exception
            # raise Exception("Something went terribly wrong! (We can provide more context here)")
            raise ValueError("Something went terribly wrong! (We can provide more context here)")

    some_function()
