from django.shortcuts import render
from .models import PSD

# Create your views here.

def index(request):
    return render(request, 'page/home.html')

def analysis(request):
    return render(request, 'page/analysis.html')

def map(request):
    return render(request, 'page/map.html')