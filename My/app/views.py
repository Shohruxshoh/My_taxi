from django.shortcuts import render
from rest_framework import generics
from .serializers import ClientSerializer, DriverSerializer, OrderSerializer
from .models import Client, Driver, Order
# Create your views here.


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



class OrderCreate(generics.CreateAPIView):
    serializer_class = OrderSerializer  
    queryset = Order.objects.all()


class OrderUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class DriverList(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class DriverCreate(generics.CreateAPIView):
    serializer_class = DriverSerializer  
    queryset = Driver.objects.all()

class DriverUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

class ClientList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientCreate(generics.CreateAPIView):
    serializer_class = ClientSerializer  
    queryset = Order.objects.all()

class ClientUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
