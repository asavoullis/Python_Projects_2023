# Decorators and Wrapper functions
# making code more resuable, readable and scalable - effective
# decorators generators functional python etc 

# The basic idea behind decorators is that they add a certain functionality to a function 
# or they surround the function they wrap the function with an additional functionality 
# To show this we are going to be using a function in a function first and then how its actually done

# this decorator function is used to decorate other functions - we pass a function
def mydecorator(function):
    # we then inside specify a wrapper function
    # this function has some functionality and then it calls the function
    def wrapper():
        print("I am decorating your function")
        function()
    return wrapper


def helloworld():
    print("Hello World!")









# https://youtu.be/iZZtEJjQLjQ
if __name__ == "__main__":
    mydecorator(helloworld)() 

    try:
        file = open("example.txt", "r")
    except FileNotFoundError:
        print("Error: File not found.")
    else:
        content = file.read()
        print("File content:", content)
        file.close()

    try:
        num = int(input("Enter a number: "))
        result = 10 / num
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
    except Exception as e:
        print("An error occurred:", e)
    
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    # In this case, the finally block is executed regardless of whether an exception was raised or not.
    finally:
        print("Execution completed.")
