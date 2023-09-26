from django.db import models
"""
here we will place our database models
Django provides (ORM) Object Relational Mapping
This means we can write some python code to create different database models
and then have whatever database models we create be automatically made for us
in some kind of structured database schema like SQLlite

we will make something called migration and this migration is actually automated code
that will then go and create the corresponding model in something like SQL / MongoDB
"""
# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
