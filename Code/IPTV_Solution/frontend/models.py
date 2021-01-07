from django.db import models
from django_countries.fields import CountryField
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField( auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
class Channel(models.Model):
    name = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=200, null=True, blank=True)
    country = CountryField()
    description = models.CharField(max_length=400, null=True, blank=True)
    date_created = models.DateTimeField( auto_now_add=True, null=True)
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.name


