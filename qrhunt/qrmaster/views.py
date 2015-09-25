from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='qrmaster:login')
def index(request):
	return render(request, 'qrmaster/index.html')    

def do_login(request):
    
    if request.method == 'GET':
        return render(request, 'qrmaster/login.html')
    
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
           if user.is_active:
                messages.add_message(request, messages.SUCCESS, 'Login successful.')
                login(request, user)
                return redirect('qrmaster:index')

        messages.add_message(request, messages.ERROR, 'Failed at login.')
        return redirect('qrmaster:login')

def do_logout(request):
    logout(request)
    return redirect('qrmaster:login')