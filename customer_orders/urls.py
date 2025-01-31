from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomersViewSet,OrderViewSet
from . import views

router = DefaultRouter()
router.register('Customers', CustomersViewSet)
router.register('Order', OrderViewSet)

urlpatterns =[

path('',include(router.urls)),
path('orders/search/', views.OrderSearchView.as_view(), name='order-search'),

]

