from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    return render(request, "myapp/home.html", {"tasks": tasks})

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.method)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:

        form = TaskForm()
    
    
    return render(request, "myapp/create_task.html", {"form": form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)

    return render(request,"myapp/edit_task.html", {"form": form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == "POST":
        task.delete()
        return redirect("home")


