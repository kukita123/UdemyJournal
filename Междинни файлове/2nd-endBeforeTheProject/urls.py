from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),

    path('tasks', views.tasks, name="tasks"),

    path('create-task', views.create_task, name="create-task"),

    path('update-task/<str:pk>', views.update_task, name="update-task"),

    path('delete-task/<str:pk>', views.delete_task, name="delete-task"),

    path('register', views.register, name="register"),

    path('success', views.success, name="success"),

    path('my-login', views.my_login, name="my-login"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('user-logout', views.user_logout, name="user-logout")
]
