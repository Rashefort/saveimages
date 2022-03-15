from django.urls import path
from . import views


urlpatterns = [
    path('', views.general, name='general'),
    path('<slug:slug>/', views.address, name='address'),
]
