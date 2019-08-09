from django.shortcuts import render, redirect, get_object_or_404
from .models import Dday,Team,Myuser
from django.utils import timezone
from .forms import DdayForm, TeamForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login


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

def loginpage(request):
    return render(request, 'loginpage.html')

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

def nav(requset):
    latest= Dday.objects.earliest('date')
    return render(request, 'nav.html', {'latest':latest})

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user=User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            name=request.POST['name']
            major=request.POST['major']
            phone_num=request.POST['phone_num']
            stu_num=request.POST['stu_num']
            myuser=Myuser(user=user,name=name,major=major,phone_num=phone_num,stu_num=stu_num)
            myuser.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            if user:
                auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'username ro password is incorrect.'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method=="POST":
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')


def table(request):
    return render(request, 'table.html')
