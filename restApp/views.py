from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def apiResponse(request):
    return JsonResponse('Django rest framework', safe=False)
