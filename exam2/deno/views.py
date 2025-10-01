from django.shortcuts import render, HttpResponse

# Create your views here.


def server(request):
    return HttpResponse('this is my test server venice i need a signal so everyone know me for it ')