from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomersViewSet, OrderViewSet, OrderSearchView
from django.contrib import admin 

# Initialize router
router = DefaultRouter()
router.register(r'customers', CustomersViewSet)
router.register(r'orders', OrderViewSet)

# Define URL patterns
urlpatterns = [
   # path('admin/', admin.site.urls),  # Admin panel
    path('api/', include(router.urls)),  # API routes
    path('api/orders/search/', OrderSearchView.as_view(), name='order-search'),  # Order search by date
]







