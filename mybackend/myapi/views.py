from django.http import JsonResponse

def get_welcome_message(request):
    return JsonResponse({"message": "Welcome to my Django API!"})

def get_farewell_message(request):
    return JsonResponse({"message": "Goodbye from my Django API!"})
