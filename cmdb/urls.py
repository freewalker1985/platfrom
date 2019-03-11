from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.serverlist, name='list'),
    path('list/add/', views.serveradd, name='list_add'),
    path('list/edit/<int:pk>/', views.serveredit, name='list_edit'),
]