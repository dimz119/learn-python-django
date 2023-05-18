from django.urls import path
from .greet import greeting
from . import views

# added app namespace
app_name = 'api'

urlpatterns = [
    path('greet/', greeting, name='greeting'),
]
