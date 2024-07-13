from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Coffee Lovers</h1>')

def about(request):
    return HttpResponse('<h1>About us</h1>')

def posts(request):
    return HttpResponse('<h1>Posts</h1>')
