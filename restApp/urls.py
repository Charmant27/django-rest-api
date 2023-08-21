from django.urls import path
from .views import apiResponse

urlpatterns = [
    path('', apiResponse),
]
