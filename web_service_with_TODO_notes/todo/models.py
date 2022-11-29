from django.db import models

from web_service_with_TODO_notes.users.models import User


class Project(models.Model):
    name_project = models.CharField(max_length=32)
    users = models.ManyToManyField(User)


class Todo(models.Model):
    text = models.CharField(max_length=32)
    user = models.ForeignKey(User, models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited")
