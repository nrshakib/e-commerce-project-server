from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    data = {
        'message': "Welcome to the E-commerce api"
    }
    return JsonResponse(data)
