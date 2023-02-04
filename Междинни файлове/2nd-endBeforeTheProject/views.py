from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .forms import CreateUserForm, LoginForm

from .forms import TaskForm
from . models import Task

# Login:
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Protect the views

from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):

    return render(request, 'index.html')


def tasks(request):

    # return all records from the database table/model:

    queryAllData = Task.objects.all()
    context = {'tasks': queryAllData}

    return render(request, 'tasks.html', context)

    # return a single record from the database table/model selected by name:

    #queryData = Task.objects.get(title = "Go to gym")
    #context = {'singleTask': queryData}

    # return render(request, 'tasks.html', context)

    # return a single record from the database table/model selected by ID:

    #queryData = Task.objects.get(id = 4)
    #context = {'singleTask': queryData}

    # return render(request, 'tasks.html', context)


def create_task(request):

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('tasks')

    context = {'form': form}

    return render(request, 'create-task.html', context)


def update_task(request, pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('tasks')

    context = {'form': form}

    return render(request, 'update-task.html', context)


def delete_task(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()

        return redirect('tasks')

    return render(request, 'delete-task.html')


def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect("success")

    context = {'form': form}

    return render(request, 'register.html', context)


def success(request):
    return render(request, 'success.html')


def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return render(request, "dashboard.html")

    context = {'form': form}
    return render(request, "my-login.html", context)


@login_required(login_url="my-login")
def dashboard(request):
    return render(request, "dashboard.html")


def user_logout(request):
    auth.logout(request)

    return redirect('my-login')
