from django.urls import path
from .views import(  OrderList, OrderCreate, OrderUpdate, 
DriverList, DriverCreate, DriverUpdate, DriverDetailDelete,
ClientList, ClientCreate, ClientUpdate, ClientDetailDelete
)

urlpatterns = [
    path('', OrderList.as_view(), name='order-list'),
    path('order/create/', OrderCreate.as_view(), name='order-create'),
    path('order/update/<int:pk>', OrderUpdate.as_view(), name='order-update'),
    path('driver/', DriverList.as_view(), name='driver-list'),
    path('driver/create/', DriverCreate.as_view(), name='driver-create'),
    path('driver/update/<int:pk>', DriverUpdate.as_view(), name='driver-update'),
    path('driver/detail/<int:pk>', DriverDetailDelete.as_view(), name='driver-detail'),
    path('client', ClientList.as_view(), name='client-list'),
    path('client/create/', ClientCreate.as_view(), name='client-create'),
    path('client/update/<int:pk>', ClientUpdate.as_view(), name='client-update'),
    path('client/detail/<int:pk>', ClientDetailDelete.as_view(), name='client-detail'),
]