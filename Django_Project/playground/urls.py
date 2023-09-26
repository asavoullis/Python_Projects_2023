from django.urls import path
# from our current folder import the views model so we can reference our views function 
from . import views

# URLConf module
urlpatterns = [
    # we are just passing a reference to this function so no () needed here
    path('hello/', views.say_hello)

]







