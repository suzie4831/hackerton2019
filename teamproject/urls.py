"""teamproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import blog.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.loginpage, name="login"),
    path('accounts/',include('allauth.urls')),
    path('home',blog.views.home, name="home"),
    path('profile',blog.views.profile, name="profile"),
    path('team/<int:team_id>', blog.views.team, name="team"),
    path('timetable', blog.views.timetable, name="timetable"),
    path('timetable_edit', blog.views.timetable_edit, name="timetable_edit"),
    path('team/new/',blog.views.new, name="new"),
    path('team/create/',blog.views.create,name="create"),
    path('<int:team_id>/dday/new', blog.views.dday_new, name="dday_new"),
    path('signup/', blog.views.signup, name='signup'),
    path('login/', blog.views.login, name='login'),
    path('logout/', blog.views.logout, name='logout'),
    path('table/', blog.views.table, name='table'),
    path('loginpage/',blog.views.loginpage, name='loginpage'),

]
