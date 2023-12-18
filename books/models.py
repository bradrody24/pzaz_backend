from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  image = models.ImageField(upload_to='images/', null=True)
