from django.shortcuts import render, get_object_or_404

from .models import ServerDetail


def serverlist(request):
    objs = ServerDetail.objects.all()
    return render(request, 'cmdb/list.html', {'objs': objs})


def serverdetail(request, pk):
    obj = get_object_or_404(ServerDetail, pk=pk)
    return render(request, 'cmdb/detail.html', {'obj': obj})
