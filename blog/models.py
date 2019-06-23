from django.db import models

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


