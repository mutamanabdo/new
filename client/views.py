from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import client
from .forms import AddClientForm
from django.contrib import messages

@login_required
def client_list(request):
    clients = client.objects.filter(created_by=request.user)
    return render(request, 'client/client_list.html',{'clients':clients})

@login_required
def client_detail(request,pk):
    client_d = get_object_or_404(client , created_by=request.user,pk=pk)
    return render(request,'client/client_detail.html',{'client':client_d})

@login_required
def client_add(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            messages.success(request, 'The client was added sucsessfully')
            return redirect('client_list')
        
    else:
        form = AddClientForm
        return render(request, 'client/client_add.html', {'form':form})
    
@login_required
def client_delete(request,pk):
    client_d = get_object_or_404(client, created_by=request.user, pk=pk)
    client_d.delete()
    messages.success(request, 'The lead was deleted sucsessfully')
    return redirect('client_list')

@login_required
def client_edit(request,pk):
    client_d = get_object_or_404(client, created_by=request.user, pk=pk)
    if request.method == 'POST':
        form = AddClientForm(request.POST,instance=client_d)
        if form.is_valid():    
            form.save()
            messages.success(request, 'The client chages done sucsessfully')
            return redirect('client_list')
    else:
        form = AddClientForm(instance=client_d)
        return render(request, 'client/client_edit.html', {'form':form},status=404)