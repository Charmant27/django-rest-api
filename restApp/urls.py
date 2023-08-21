from django.urls import path
from .views import apiResponse, taskList, singleTask, createTask, updateTask, deleteTask

urlpatterns = [
    path('', apiResponse),
    path('task-list/', taskList, name='task-list'),
    path('single-task/<str:pk>/', singleTask, name='single-task'),
    path('add-task/', createTask, name='add-task'),
    path('update-task/<str:pk>/', updateTask, name='update-task'),
    path('delete-task/<str:pk>/', deleteTask, name='delete-task')
]
