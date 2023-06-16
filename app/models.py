from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_image=models.ImageField(upload_to="profile_image",blank=True)
    address = models.CharField(max_length=300)
