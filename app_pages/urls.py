from django.urls import path
from .views import home_view
from .views import contact_view



urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact_page')
]