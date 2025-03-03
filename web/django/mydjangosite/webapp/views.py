from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    """
    Простое представление, возвращающее HTML с приветствием.
    """
    return HttpResponse("<h1>Добро пожаловать в Django Demo!</h1><p>Это учебное приложение на Django.</p>")


def api_info(request):
    """
    Возвращает информацию о приложении в формате JSON.
    """
    data = {"app": "Django Demo", "version": "1.0"}
    return JsonResponse(data)
