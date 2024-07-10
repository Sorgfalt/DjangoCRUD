from django.test import TestCase
from django.db import models


# Create your tests here.
class User(models.Model):
    userId = models.CharField(max_length=20)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=70)

    class Meta:
        db_table = 'user'
