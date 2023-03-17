from django.shortcuts import redirect, render

from django.http import HttpResponse

# - Register, Login, Post, Update
from .forms import CreateUserForm, LoginForm, ThoughtPostForm, ThoughtUpdateForm, UpdateUserForm

# - Authentication
from django.contrib.auth.models import auth

from django.contrib.auth import authenticate

# - Delete user
from django.contrib.auth.models import User

# - To protect the views
from django.contrib.auth.decorators import login_required

# - To generate django massages
from django.contrib import messages

# - To read a thought
from .models import Thought

# Create your views here.

# - Homepage


def home(request):

    return render(request, 'index.html')

# - Register


def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your account was created!")
            return redirect('my-login')

    context = {'form': form}
    return render(request, 'register.html', context)

# - Login


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
                return redirect('dashboard')

    context = {'form': form}
    return render(request, 'my-login.html', context=context)


# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):

    return render(request, 'profile/dashboard.html')


# - Logout
def user_logout(request):

    auth.logout(request)
    return redirect("my-login")

# - Post thought


@login_required(login_url='my-login')
def post_thought(request):

    form = ThoughtPostForm()

    if request.method == 'POST':
        form = ThoughtPostForm(request.POST)

        if form.is_valid():
            thought = form.save(commit=False)
            thought.user = request.user
            thought.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'profile/post-thought.html', context=context)


# - My thoughts

@login_required(login_url='my-login')
def my_thoughts(request):

    current_user = request.user.id

    thought = Thought.objects.all().filter(user=current_user)

    context = {'thought': thought}

    return render(request, 'profile/my-thoughts.html', context=context)


# - Update thought

@login_required(login_url='my-login')
def update_thought(request, pk):

    thought = Thought.objects.get(id=pk)
    form = ThoughtUpdateForm(instance=thought)

    if request.method == 'POST':
        form = ThoughtUpdateForm(request.POST, instance=thought)

        if form.is_valid():
            form.save()

            return redirect('my-thoughts')

    context = {'form': form}
    return render(request, 'profile/update-thought.html', context=context)


# - Delete thought

@login_required(login_url='my-login')
def delete_thought(request, pk):

    thought = Thought.objects.get(id=pk)

    if request.method == 'POST':

        thought.delete()
        return redirect('my-thoughts')

    return render(request, 'profile/delete-thought.html')

# - Profile management


@login_required(login_url='my-login')
def profile_management(request):

    form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {'form': form}

    return render(request, 'profile/profile-management.html', context=context)


# - Delete account

@login_required(login_url='my-login')
def delete_account(request):

    if request.method == 'POST':

        deleteUser = User.objects.get(username=request.user)

        deleteUser.delete()

        return redirect('my-login')

    return render(request, 'profile/delete-account.html')
