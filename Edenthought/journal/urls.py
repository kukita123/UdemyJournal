from unicodedata import name
from django.urls import path

from . import views


urlpatterns = [

    # - Homepage
    path('', views.home),

    # - Register
    path('register', views.register, name="register"),

    # - Login
    path('my-login', views.my_login, name="my-login"),

    # - Dashboard
    path('dashboard', views.dashboard, name="dashboard"),

    # - Logout url
    path('user-logout', views.user_logout, name="user-logout"),

    # - Post Thought
    path('post-thought', views.post_thought, name="post-thought"),

    # - My thoughts
    path('my-thoughts', views.my_thoughts, name="my-thoughts"),

]
