from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>This is my Home Page</h1>")

def about(request):
    return render(request, 'about.html')
