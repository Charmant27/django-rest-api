# rest framework imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Taskserializer
from .models import Task

# Create your views here.

# simple demonstration
@api_view(['GET'])
def apiResponse(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = Taskserializer(tasks, many=True)
    return Response(serializer.data)

# getting a single task
@api_view(['GET'])
def singleTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = Taskserializer(task, many=False)
    return Response(serializer.data)

# creating a new task
@api_view(['POST'])
def createTask(request):
    serializer = Taskserializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# updating a task
@api_view(['POST'])
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = Taskserializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Item deleted successfully')
