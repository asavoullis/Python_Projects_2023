from django.urls import path 
from . import views

"""
this is where we'll place different URL routes and then connect them to our views
"""

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos")

]

"""
How to use a template
So a template is essentially a reusable HTML file that allows us to display dynamic data. 
And we can have templates inherit from other templates.
"""