from django.contrib import messages
from django.shortcuts import render , redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .form import AddLeadForm
from .models import lead
from client.models import client

@login_required
def lead_list(request):
    list = lead.objects.filter(created_by=request.user, converted=False)
    return render(request, 'lead/lead_list.html', {'leads':list})

@login_required
def lead_detail(request,pk):
    detail = get_object_or_404(lead, created_by=request.user, pk=pk)

    return render(request, 'lead/lead_detail.html', {'lead':detail})

@login_required
def edit_lead(request,pk):
    lead_d = get_object_or_404(lead, created_by=request.user, pk=pk)
    if request.method == 'POST':
        form = AddLeadForm(request.POST,instance=lead_d)
        if form.is_valid():    
            form.save()
            messages.success(request, 'The lead chages done sucsessfully')
            return redirect('lead_list')
    else:
        form = AddLeadForm(instance=lead_d)
        return render(request, 'lead/edit_lead.html', {'form':form})
    
    
@login_required
def leads_delete(request,pk):
    lead_d = get_object_or_404(lead, created_by=request.user, pk=pk)
    lead_d.delete()
    messages.success(request, 'The lead was deleted sucsessfully')
    return redirect('lead_list')

@login_required
def add_lead(request):
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            messages.success(request, 'The lead waas added sucsessfully')
            return redirect('lead_list')
        
    else:
        form = AddLeadForm
        return render(request, 'lead/add_lead.html', {'form':form})


@login_required
def converte_to_client(request,pk):
    l = get_object_or_404(lead, created_by=request.user, pk=pk)
    client_info = client.objects.create(
        name = l.name,
        email = l.email,
        description = l.description,
        created_by = request.user
    )
    l.converted = True
    l.save()

    messages.success(request, 'The lead converted to client sucsessfully')
    return redirect('lead_list')