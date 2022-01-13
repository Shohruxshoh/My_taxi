from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=90)
    car_type = models.CharField(max_length=50)
    car_number = models.CharField(max_length=20)
    driver_phone = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50)
    clinet_phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS = (
        ('CREATED', 'CREATED'),
        ('CANCELLED', 'CANCELLED'),
        ('ACCEPTED', 'ACCEPTED'),
        ('FINISHED', 'FINISHED'),

    )
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='driver')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client')
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

