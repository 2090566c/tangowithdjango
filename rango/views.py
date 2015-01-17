from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world!")

def about(request):
    return HttpResponse("Rango says this is the about page, this tutorial has been put together by Gary Curran 2090566")
