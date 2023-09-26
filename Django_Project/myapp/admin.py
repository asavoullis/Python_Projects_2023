from django.contrib import admin
from .models import TodoItem

"""
This allows us to register database models so we can view them on our admin panel
in this file we register our database models so that they will appear inside our admin panel
allowing us to modify and view them 
"""
# Register your models here.
admin.site.register(TodoItem)