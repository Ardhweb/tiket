from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import  UserManager
from django.utils.timezone import now
from datetime import timedelta
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import UserManager
#Extended Version of Table Schema for User Table.
class User(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure email is unique
    user_role = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mobile = models.CharField(max_length=12,blank=True,null=True)

    USERNAME_FIELD = 'email'  # Authentication based on email
    REQUIRED_FIELDS = ['username']  # Keep username mandatory

    objects = UserManager()

    def __str__(self):
        return self.email

   


