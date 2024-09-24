from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('boat.urls', namespace='boat')),
    path('order/', include('order.urls', namespace='order')),
]
