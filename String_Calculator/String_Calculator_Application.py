""" The objective is to write a simple string calculator application with the following requirements listed below. 


You should choose how many or few of the requirements below to implement for the test submission, in the time you have available. 
The more working requirements you implement the better your score. 
However, do not attempt to complete all requirements at the expense of neat and maintainable code and a working solution!

Assessment criteria (what are we looking for?):
1.	Code is neatly structured, maintainable and understandable.
2.	Good code comments help us understand your thinking and implementation.
3.	The implemented requirements work as described by this document.
4.	Your submitted project (source files) compiles into an executable and runs.
5.	Avoid quick hacks! We’re looking for good planning and good software design.

Your submitted solution should be a single set of code that implements some or all of the requirements below.
You can choose to implement this as a Test Driven Development (TDD) exercise, although this is not mandatory. 
Use the approach that best works for you in the time available.

String Calculator Requirements
Pick from the following for your test submission:

1.	Create a simple String calculator with a method int Add(string numbers) 
a)	The method will return the sum of comma-separated integer numbers parsed from the numbers parameter 
(for an empty string it will return 0). Examples for the numbers parameter are: “” or “1” or “1,2”
b)	The Add method should handle an unknown amount of numbers

2.	In addition to commas, allow the Add method to handle new lines between numbers.
a)	the following input is ok:  “1\n2,3” (will equal 6)
b)	the following input is NOT ok: “1,\n”

3.	As well as comma-separated and new lines, allow the Add method to support different delimiters
a)	To set the delimiter, the beginning of the input string will contain a separate line that looks like this: 
“//[delimiter]\n[numbers…]” for example “//;\n1;2” should return 3 where the default delimiter is ‘;’.
b)	the first line is optional. all existing scenarios should still be supported.

4.	The Add method when called with a negative number will throw an exception “negatives not allowed”. The exception string should include a comma-separated list of each negative number passed to the Add method. 

5.	The Add method should ignore any numbers bigger than 1000, so adding 2 + 1001 = 2

6.	Allow the Add method to support Delimiters of any length with the following format: “//[delimiter]\n” for example: “//[***]\n1***2***3” should return 6.

7.	In addition to point 6, allow the Add method to support multiple delimiters like this: “//[delim1][delim2]\n” for example “//[*][%]\n1*2%3” should return 6.

8.	In addition to point 7, allow the Add method to support multiple delimiters of any length like this:
“//[delim1][delim2]\n” for example “//[**][%%%]\n1**2%%%3” should return 6.


By: Charilaos Alkiviades Savoullis
 
 """

import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        # If the string is empty, return 0
        if not numbers:
            return 0
        
        # Split the numbers based on comma, newline, or custom delimiter
        # normal delimiters
        delimiter = ',|\n'
        # Check if the string 'numbers' starts with '//'.
        if numbers.startswith("//"):
            # If it does, extract the custom delimiter and numbers.
            custom_delimiter, numbers = re.match(r"//(\[?.*?\]?)\n(.*)", numbers).groups()
            
            # Create a delimiter pattern using regular expressions by joining escaped characters from the custom delimiter.
            delimiter = '|'.join(map(re.escape, re.findall(r"\[?(.*?)\]?", custom_delimiter)))
            
        numbers_list = re.split(delimiter, numbers)

        # Filter out empty strings and convert the numbers to integers, then filter numbers greater than 1000
        numbers_list = [int(x) for x in numbers_list if x.strip() and int(x.strip()) <= 1000]

        # Check for negative numbers
        negatives = [x for x in numbers_list if x < 0]
        if negatives:
            raise ValueError("Negatives not allowed: " + ', '.join(map(str, negatives)))

        # Return the sum of the numbers
        return sum(numbers_list)

# Testing the implementation
calculator = StringCalculator()

# Test cases
print(calculator.add("")) # Expected output: 0
print(calculator.add("1")) # Expected output: 1
print(calculator.add("1,2")) # Expected output: 3
print(calculator.add("1\n2,3")) # Expected output: 6
print(calculator.add("//;\n1;2")) # Expected output: 3
print(calculator.add("2,1001")) # Expected output: 2
print( calculator.add("//[***]\n1***2***3")) # Expected output: 6
print(calculator.add("//[*][%]\n1*2%3")) # Expected output: 6