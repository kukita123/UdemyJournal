from django.shortcuts import redirect, render

# - Registration, Login
from .forms import CreateUserForm, LoginForm, ThoughtPostForm
from django.http import HttpResponse

# - Login
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

# - Protect user dashboard from unauthorized login
from django.contrib.auth.decorators import login_required

# - Import django messages
from django.contrib import messages

# Create your views here.

# - Homepage


def home(request):

    return render(request, 'index.html')


# - Register
def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Your account was created successfully!")
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


# - User logout
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
            thought.user = request.user  # this is the foreign key for the user, who is logged in

            thought.save()
            return redirect('dashboard')

    context = {'form': form}

    return render(request, 'profile/post-thought.html', context=context)
