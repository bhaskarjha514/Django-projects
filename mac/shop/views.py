from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    return render(request,'shop/index.html')

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return render(request,'shop/')

def tracker(request):
    return render(request,'shop/')

def search(request):
    return render(request,'shop/')

def prodView(request):
    return render(request,'shop/')

def checkout(request):
    return render(request,'shop/')
# Create your views here.
