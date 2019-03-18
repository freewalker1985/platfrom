from django.urls import path
from . import views

app_name = 'cmdb'
urlpatterns = [
    path('list/', views.serverlist, name='list'),
    path('list/add/', views.serveradd, name='list_add'),
    path('list/del/<int:pk>', views.serverdel, name='list_del'),
    path('list/edit/<int:pk>/', views.serveredit, name='list_edit'),
    path('handler/ssh/<ip>', views.invokessh, name='ssh'),
    path('handler/scp/', views.invokescp, name='scp'),
]