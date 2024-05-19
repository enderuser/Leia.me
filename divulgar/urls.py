from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.DivulgarCreateView, name="DivulgarCreate"),
    path('update/', views.DivulgarUpdateView, name="DivulgarUpdate"),
    path('delete/<int:id>', views.DivulgarDeleteView, name="DivulgarDelete"),
    path('list/', views.DivulgarListView, name="DivulgarList"),
    path('detail/<int:id>', views.DivulgarDetailView, name="ver_livro"),
]