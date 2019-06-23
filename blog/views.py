from django.shortcuts import render, redirect, get_object_or_404
from .models import Dday,Team,Members
from django.utils import timezone
from .forms import DdayForm

# Create your views here.

def home(request):
    ddays=Dday.objects
    teams=Team.objects
    return render(request, 'home.html', {'teams':teams, 'ddays':ddays})

def team(request, team_id):
    team_detail = get_object_or_404(Team, pk= team_id)

    return render(request, 'team.html', {'team': team_detail})

def profile(request):
    return render(request, 'profile.html')

def login(request):
    return render(request, 'login.html')

def timetable(request):
    return render(request, 'timetable.html')

def timetable_edit(request):
    return render(request, 'timetable_edit.html')

def new(request):
    return render(request,'new.html')

def create(request):
    team=Team()
    team.t_name=request.GET['t_name']
    team.t_class=request.GET['t_class']
    team.save()
    return redirect('home')


def dday_new(request,team_id):
    post = get_object_or_404(Team, pk= team_id)
    if request.method == "POST":
        form = DdayForm(request.POST)
        if form.is_valid():
            dday = form.save(commit=False)
            dday.post = Team.objects.get(pk=team_id)
            dday.save()
            return redirect('team', team_id)
    else:
        form = DdayForm()
        return render(request, 'dday_form.html', {'form':form})
