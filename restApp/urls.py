from django.urls import path
from .views import apiResponse, taskList

urlpatterns = [
    path('', apiResponse),
    path('task-list/', taskList, name='task-list')
]
