from rest_framework.serializers import ModelSerializer
from .models import Order, Client, Driver


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'clinet_phone', 'address', 'created', 'updated']


class DriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'name', 'car_type', 'car_number', 'driver_phone', 'created', 'updated']

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'driver', 'client', 'status', 'created', 'updated']
