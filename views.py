from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def data(request):
    return HttpResponse("<h1>Сегодня 22.11.2024</h1>")


def test(request):
    return HttpResponse("<h1>Тестируем проект Django</h1>")