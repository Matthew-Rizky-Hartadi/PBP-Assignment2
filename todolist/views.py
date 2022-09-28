from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import Task
import datetime

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todolist_item = Task.objects.filter(user = request.user)
    context= {
        'list_item': todolist_item,
        'user': request.user,
    }
    return render(request, 'todolist.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('todolist:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # create response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return redirect('todolist:show_todolist')
            
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/todolist/login/')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title != "" and description != "":
            Task.objects.create(user=request.user, title=title, description=description, date=datetime.datetime.today())
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, "Please fill the title/description")
    
    return render(request, 'create-task.html')

@login_required(login_url='/todolist/login/')
def finish_task(request, id):
    item = Task.objects.get(user = request.user, id=id)
    item.is_done = not item.is_done
    item.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    item = Task.objects.get(user = request.user, id=id)
    item.delete()
    return redirect('todolist:show_todolist')