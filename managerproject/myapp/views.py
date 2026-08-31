from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")


def login_view(request):
    if request.method == "POST":
        
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # from.get_user() → get the user object from the form.
            login(request, form.get_user())
            return redirect("home")
    else:
        form = AuthenticationForm(request)

    return render(request, "myapp/login.html", {"form": form})
    



@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)

    return render(request, "myapp/home.html", {"tasks": tasks})

# login_required → only logged-in users can access this view.
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            # commit=False → don't save the task to the database yet.
            task = form.save(commit=False)
            # Set the user of the task to the current logged-in user.
            task.user = request.user
            task.save()
            return redirect("home")
    else:
        
        form = TaskForm()
    
    
    return render(request, "myapp/create_task.html", {"form": form})

#  user=request.user → only get the task if it belongs to the current logged-in user.
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)

    return render(request,"myapp/edit_task.html", {"form": form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == "POST":
        task.delete()
        return redirect("home")


