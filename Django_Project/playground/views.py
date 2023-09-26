from django.shortcuts import render
from django.http import HttpResponse

"""
this is a request handler, its not a view, its doesn't have a template or html
this is where we define our views or view functions 
"""


# Create your views here.
# a view function is a function that takes a request and returns a response
# request -> response
# its a request handler
# is some frameworks its called an action but in django is called a view
# but something that a user sees is a template

def calculate():
    x = 1
    y = 2
    return x
    

def say_hello(request):
    # x = 1 # for debugging purposes (step OVER)
    # x = calculate() # step INTO

    # return HttpResponse("Hello World!")
    return render(request, "hello.html", {'name': 'Chris'})
