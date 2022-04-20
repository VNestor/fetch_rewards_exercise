from django.db import models

# Create your models here.
# Creating a model in django is similar to creating a table in a database.


class User(models.Model):
    name = models.CharField(max_length=30, unique=True)
    points = models.IntegerField(null=False)


class Transaction(models.Model):
    payer = models.CharField(max_length=30)
    points = models.IntegerField(null=False)
    timestamp = models.DateTimeField(null=False)
