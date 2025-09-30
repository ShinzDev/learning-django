from django.shortcuts import render, HttpResponse
from .models import TodoItem
# from flask import request
# Create your views here

def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items })







    # return HttpResponse("All you python devs I am coming 🥵🥵🥵😳😳  ")



















 
 
 
 
