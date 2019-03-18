from django.shortcuts import render, get_object_or_404, redirect

from .models import ServerDetail
from .froms import ServerDetailForm

import win32api



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
            return redirect('cmdb:list')
    else:
        form = ServerDetailForm(instance=obj)
    return render(request, 'cmdb/edit.html', {'form': form, 'obj': obj})


def serverdel(request, pk):
    obj = get_object_or_404(ServerDetail, pk=pk)
    obj.delete()
    return redirect('cmdb:list')


def invokessh(request, ip):
    agr = '-ssh root@' + ip
    win32api.ShellExecute(0, 'open', 'putty.exe ', agr, '', 1)
    return redirect('cmdb:list')


def invokescp(request):
    win32api.ShellExecute(0, 'open', 'C:\Program Files (x86)\WinSCP\WinSCP.exe', '', '', 1)
    return redirect('cmdb:list')