from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login, logout as auth_logout

from django.contrib import messages, auth

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            auth_login(request, user)
            messages.success(request, "Logged-in successfully!")
            return redirect('index')
        else:
            messages.error(request, 'Username and Password incorrect!')
            # return redirect('login')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def logout_view(request):
    auth_logout(request)
    messages.success(request, "Logged out successfully!")
    return render(request, 'login.html')

