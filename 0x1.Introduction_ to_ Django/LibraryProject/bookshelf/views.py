from django.shortcuts import render

from django.http import HttpRequest

def index(request): 
    return HttpRequest("Welcome to my book shelf.")

# Create your views here.
