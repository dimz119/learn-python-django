from django.urls import path

from . import views

# added app namespace
app_name = 'inventory'

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('fbv', views.fbv_view, name='fbv'),
    # path('car/', views.CarFormView.as_view(), name='car'),
    path('create_car/', views.CarCreateView.as_view(), name='car-create'),
    path('list_car/', views.CarListView.as_view(), name='car-list'),
    path('detail_car/<int:pk>', views.CarDetailView.as_view(), name='car-detail'),
    path('update_car/<int:pk>', views.CarUpdateView.as_view(), name='car-update'),
    path('delete_car/<int:pk>', views.CarDeleteView.as_view(), name='car-delete'),
]
