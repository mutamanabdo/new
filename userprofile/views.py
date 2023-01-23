from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request , 'crm/base.html')

def dashboard(request):
    return render(request, 'crm/dashboard.html')

def singup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            # print(f"user {UserProfile} added !")
            return redirect('login')
        else:
            error = "you eneterd weinfd cridaera"
            return render(request, 'registration/signup.html',{"error":error})
    else:
        form = UserCreationForm
        return render(request, 'registration/signup.html',{"form":form})
