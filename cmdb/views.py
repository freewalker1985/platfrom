from django.shortcuts import render

from .models import ServerDetail


def serverlist(request):
    object = ServerDetail.objects.all()
    return render(request, 'cmdb/list.html', {'object': object})
