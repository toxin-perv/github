from django.db import models

# Create your models here.
class contact(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)