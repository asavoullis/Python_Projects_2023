from django.shortcuts import render, HttpResponse
from .models import TodoItem
"""
Which is mainly where we'll work, where we'll create different views or routes that we can access on our website.
"""


# we will take the request object as a parameter which will allow us to access things like query parameters 
# and the body of the different requests that are being sent to this function
def home(request):
    return render(request, "home.html")


def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})
"""This view is going to render a template that will view all of the different to do list items that we have"""