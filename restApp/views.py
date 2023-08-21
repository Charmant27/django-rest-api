# rest framework imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Taskserializer
from .models import Task

# Create your views here.

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
