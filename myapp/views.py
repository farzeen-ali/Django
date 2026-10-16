from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to my First Django App!</h1><p>This is my First Paragraph</p>")

def about(request):
    return HttpResponse("<h1>Welcome to About Page</h1><p>This is about page</p>")

