from django.db import models

# Create your models here.
class feature(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)




   