from django.urls import path
from . import views

urlpatterns = [
    path('', views.weightCount, name='weight'),
]