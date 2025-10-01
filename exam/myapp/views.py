from django.shortcuts import render, HttpResponse

# Create your views here.


# myapp/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse(request, "Hello from the index page of myapp!")