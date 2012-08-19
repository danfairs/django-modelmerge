from django.db import models
from django.utils import timezone


class Topping(models.Model):
    name = models.CharField(max_length=20)


class Customer(models.Model):
    name = models.CharField(max_length=20)


class Notes(models.Model):
    text = models.TextField()


class Pizza(models.Model):

    name = models.CharField(max_length=20)
    size = models.PositiveIntegerField()
    toppings = models.ManyToManyField(Topping)
    customer = models.ForeignKey(Customer)
    notes = models.OneToOneField(Notes)
    created = models.DateTimeField(default=timezone.now)
