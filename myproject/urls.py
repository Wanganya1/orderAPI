
#from django.contrib import admin
#from django.urls import path,include
#from django.views.generic import RedirectView

#urlpatterns = [
 #   path('admin/', admin.site.urls),
  #  path('api/', include('customer_orders.urls')),
   # path('', RedirectView.as_view(url='/api/', permanent=True)),
#]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', include('customer_orders.urls')),  # Include customer_orders app URLs
]
