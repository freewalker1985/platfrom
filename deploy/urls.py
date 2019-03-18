from django.urls import path

from . import views


app_name = 'deploy'
urlpatterns = [
    path('list/', views.serverlist, name='deploy'),
]