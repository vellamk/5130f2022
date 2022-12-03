from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import decision


# Create your views here.

def about(request):
    return render(request, 'about.html')


def Decision(request):

    return render(request, 'Decision-factors.html')


def home(request):
    return render(request, 'home.html')


def report(request):
    return render(request, 'report.html')


def index(request):
    return render(request, 'index.html')


def signup(request):
    return render(request, 'signup.html')
