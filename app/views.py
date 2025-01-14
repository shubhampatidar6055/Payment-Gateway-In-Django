from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def success(request):
    return render(request, 'success.html')

def email(request):
    return render(request, "email.html")