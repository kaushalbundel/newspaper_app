from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    '''
The purpose of this model is so that we can have custom user model as per our requirement.
    This model can be used in two places:
    1. When the user is signing on or signing off
    2. When the user is loggin in or logging off
    3. When the super user is accessing the model from admin panel
    '''
    age = models.PositiveIntegerField(null=True, blank=True) #null indicates that the field can be null in the database while blank indicates that the field can be blank in the form
