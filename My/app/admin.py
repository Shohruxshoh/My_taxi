from django.contrib import admin

from app.models import Order, Client, Driver

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('driver', 'client', 'created', 'updated')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'clinet_phone', 'address', 'created', 'updated')

class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_type', 'car_number', 'driver_phone', 'created', 'updated')


admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Driver, DriverAdmin)
