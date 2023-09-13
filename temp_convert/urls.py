from django.urls import path
from . import views

urlpatterns = [
    path('', views.tempConvert, name='temp'),
]