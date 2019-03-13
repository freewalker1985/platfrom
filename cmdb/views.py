from django.shortcuts import render, get_object_or_404, redirect

from .models import ServerDetail
from .froms import ServerDetailForm


def serverlist(request):
    objs = ServerDetail.objects.all()
    return render(request, 'cmdb/list.html', {'objs': objs})


def serveradd(request):
    if request.method == 'POST':
        form = ServerDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = ServerDetailForm()
    return render(request, 'cmdb/add.html', {'form': form})


def serveredit(request, pk):
    obj = get_object_or_404(ServerDetail, pk=pk)
    if request.method == 'POST':
        form = ServerDetailForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = ServerDetailForm(instance=obj)
    return render(request, 'cmdb/edit.html', {'form': form, 'obj': obj})


def serverdel(request, pk):
    obj = get_object_or_404(ServerDetail, pk=pk)
    obj.delete()
    return redirect('list')

