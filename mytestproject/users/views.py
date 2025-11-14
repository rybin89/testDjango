from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from .forms import LoginForm
# Create your views here.

def get(request):
    users = User.objects.all()
    return HttpResponse(users)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.user
            login(request,user)
            return redirect('notes')
    else:
        form = LoginForm()
    return render(request,'users/login.html',{'form':form})
def logout_user(request):
    logout(request)
    return redirect('login')