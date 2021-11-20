from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')


def sign(request):
    return render(request, 'signin_up.html')

def explore(request):
    return render(request, 'explore.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def profile(request):
    return render(request, 'profile.html')



def help(request):
    return render(request, 'help.html')


def success(request):
    return render(request, 'success.html')