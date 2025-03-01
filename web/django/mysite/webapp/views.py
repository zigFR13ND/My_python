from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    """
    Простое представление, возвращающее HTML с приветствием.
    """
    return HttpResponse("<h1>Добро пожаловать в Django Demo!</h1><p>Это учебное приложение на Django.</p>")

