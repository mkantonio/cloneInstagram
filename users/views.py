from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('post:post_list')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
    return render(request, 'users/login.html')
