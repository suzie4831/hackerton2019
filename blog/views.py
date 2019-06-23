from django.shortcuts import render, redirect
from .models import Team

# Create your views here.

def home(request):
   teams = Team.objects
   return render(request, 'home.html', {'teams': teams})

def team(request):
    return render(request, 'team.html')

def profile(request):
    return render(request, 'profile.html')

def login(request):
    return render(request, 'login.html')

def timetable(request):
    return render(request, 'timetable.html')

def timetable_edit(request):
    return render(request, 'timetable_edit.html')


