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

    # - Logout
    path('user-logout', views.user_logout, name="user-logout"),

    # - Post tgought
    path('post-thought', views.post_thought, name='post-thought'),

    # - My thoughts
    path('my-thoughts', views.my_thoughts, name="my-thoughts"),

    # - Update thought
    path('update-thought/<str:pk>', views.update_thought, name="update-thought"),

    # - Delete thought
    path('delete-thought/<str:pk>', views.delete_thought, name="delete-thought"),

    # - Profile management
    path('profile-management', views.profile_management, name="profile-management"),

    # - Delete account
    path('delete-account', views.delete_account, name="delete-account"),
]
