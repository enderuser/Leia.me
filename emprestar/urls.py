from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmprestarListView, name="DivulgarList"),
    
]