from django.db import models

''' 
from datetime import timedelta
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

#from django.dispatch import receiver
#from django.db.models.signals import post_save

class UserNew(AbstractUser):
    image = models.ImageField(upload_to='users_image',blank=True)
    age = models.PositiveIntegerField(default=18)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(auto_now=True, blank=True,null=True)

    def is_activation_key_expires(self):
        if now() <=self.activation_key_expires + timedelta(hours=48):
            return False
        return True

'''
class User(models.Model):
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField(blank=True, null=True)
    email = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name
