from django.db import models

from users.models import User #web_service_with_TODO_notes.users.models


class Project(models.Model):
    name_project = models.CharField(max_length=32)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name  #name_project


class Todo(models.Model):
    text = models.CharField(max_length=32)
    user = models.ForeignKey(User, models.PROTECT) # точно?
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited")

    def __str__(self):
        return self.name
