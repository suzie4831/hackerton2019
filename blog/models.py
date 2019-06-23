from django.db import models
from datetime import datetime
from django.utils import timezone

class Team(models.Model):
    t_name = models.CharField(max_length=100)
    t_class = models.CharField(max_length=100)

    def __str__(self):
        return self.t_name

class Members(models.Model):
    name=models.CharField(max_length=30)
    major=models.CharField(max_length=50)
    number=models.IntegerField()
    callnum=models.CharField(max_length=50)
    teamname=models.CharField(max_length=50)

    def __str__(self):
        return self.name

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
