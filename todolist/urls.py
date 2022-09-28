from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task, delete_task, finish_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('delete_task/<int:id>', delete_task, name='delete_task_id'),
    path('finish_task/<int:id>', finish_task, name='finish_task_id'),

]