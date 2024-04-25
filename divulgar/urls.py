from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.DivulgarCreateView, name="DivulgarCreate"),
    path('update/', views.DivulgarUpdateView, name="DivulgarUpdate"),
    path('list/', views.DivulgarListView, name="DivulgarList"),
    
]