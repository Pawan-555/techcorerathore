from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # <-- Ise badalkar aise simple kar dein
    path('', include('app_pages.urls')), 
]