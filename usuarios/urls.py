from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.UserCreateView, name="CreateUser"),
    path('login/', views.UserLoginView, name="LoginUser"),
    path('logout/', views.UserLogoutView, name="LogoutUser"),
    
]