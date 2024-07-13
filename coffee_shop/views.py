from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpsResponse('<h1>Coffee Lovers</h1>')
