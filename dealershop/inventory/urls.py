from django.urls import path

from . import views

# added app namespace
app_name = 'inventory'

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
]
