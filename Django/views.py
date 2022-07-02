from django.http import HttpResponse
from django.shortcuts import render


def runoob(request):
    views_name = "菜鸟教程"
    return render(request, "runoob.html", {"name": views_name})


def hello(request):
    return HttpResponse("Hello world ! ")
