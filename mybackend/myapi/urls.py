from django.urls import path
from .views import get_welcome_message, get_farewell_message

urlpatterns = [
    path('welcome/', get_welcome_message),
    path('farewell/', get_farewell_message),
]
