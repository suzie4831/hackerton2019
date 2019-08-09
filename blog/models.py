from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Myuser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    major = models.CharField(max_length=50,  default='')
    phone_num = models.CharField(max_length=100, default='')
    stu_num = models.IntegerField(default='')

    def __str__(self):
        return self.name

class Team(models.Model):
    user = models.ForeignKey(Myuser, related_name='my_user', on_delete=models.CASCADE)
    t_name = models.CharField(max_length=100, default='')
    t_class = models.CharField(max_length=100)

    def __str__(self):
        return self.t_name


class Dday(models.Model):
    team = models.ForeignKey(Team, related_name='my_team', on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    date = models.DateField()

    def delta(self):
        delta=datetime.now().date()- self.date
        return delta


    def approve(self):
        self.approved_dday = True
        self.save()

    def __str__(self):
        return self.title
