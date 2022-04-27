from django.db import models

# Create your models here.
# Creating a model in django is similar to creating a table in a database.


class Points(models.Model):
    payer = models.CharField(null=False, max_length=30, unique=True)
    points = models.IntegerField(null=False)


class Transactions(models.Model):
    payer = models.CharField(null=False, max_length=30)
    points = models.IntegerField(null=False)
    timestamp = models.DateTimeField(null=False)
