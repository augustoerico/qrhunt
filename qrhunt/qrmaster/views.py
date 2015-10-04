from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from qrmaster.models import Quest, Hint
from django.contrib.auth.models import User

@login_required(login_url='qrmaster:login')
def index(request):
    user = request.user
    quests = Quest.objects.filter(master=user)
    
    return render(request, 'qrmaster/index.html', 
				  {'user': user, 'quests': quests})

# QUEST STUFF -----------------------------------------------------------------
@login_required(login_url='qrmaster:login')
def quest(request, pk):
    quest = Quest.objects.get(pk=pk)
    hints = quest.hint_set.all()
    
    return render(request, 'qrmaster/quest.html',
                 {'quest': quest, 'hints': hints})

@login_required(login_url='qrmaster:login')
def quest_create(request):
    master = request.user
    name = request.POST['name']
    
    quest = Quest(name=name, master=master)
    quest.save()
    
    return redirect('qrmaster:index')

@login_required(login_url='qrmaster:login')
def quest_delete(request, pk):
    quest = Quest.objects.get(pk=pk)
    quest.delete()
    
    return redirect('qrmaster:index')

@login_required(login_url='qrmaster:login')
def quest_edit(request, pk):
    quest = Quest.objects.get(pk=pk)
    quest.name = request.POST['name']
    quest.save()
    
    return redirect('qrmaster:index')

# HINT STUFF ------------------------------------------------------------------
def hint(request, pk):
    hint = Hint.objects.get(id=pk)
    return render(request, 'qrmaster/hint.html',
                 {'hint': hint})

@login_required(login_url='qrmaster:login')
def hint_create(request, quest_pk):
    title = request.POST['title']
    message = request.POST['message']
    
    quest = Quest.objects.get(pk=quest_pk)
    quest.hint_set.create(title=title, message=message)
    
    return redirect('qrmaster:index')

@login_required(login_url='qrmaster:login')
def hint_delete(request, pk):
    hint = Hint.objects.get(id=pk)
    hint.delete()
    
    return redirect('qrmaster:index')

@login_required(login_url='qrmaster:login')
def hint_edit(request, pk):
    hint = Hint.objects.get(id=pk)
    hint.title = request.POST['title']
    hint.message = request.POST['message']
    hint.save()
    
    return redirect('qrmaster:index')

# LOGIN STUFF -----------------------------------------------------------------
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

def account_create(request):
	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']
	
	user = User.objects.create_user(username, email, password)
	if user:
		messages.add_message(request, messages.SUCCESS, 'Account created.')		
	else:
		messages.add_message(request, messages.ERROR, 'Failed at account creation.')
	
	return redirect('qrmaster:login')