from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField(blank=True, null=True)
    email = models.CharField(max_length=64, unique=True)
