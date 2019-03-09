from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.serverlist, name='list'),
    path('list/<int:pk>/', views.serverdetail, name='detail'),
]