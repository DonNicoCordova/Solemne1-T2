from django.db import models
from basket.defines import POSITION_PLAYER_CHOICES
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos')
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=120)
    nickname = models.CharField(max_length=120)
    birthday = models.DateField()
    age = models.PositiveIntegerField()
    email = models.EmailField()
    height = models.PositiveIntegerField(help_text="Altura en cm")
    weight = models.PositiveIntegerField(help_text="Peso en kilos")
    picture = models.ImageField(upload_to='picture_players')
    position = models.CharField(max_length=60, choices=POSITION_PLAYER_CHOICES)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    rut = models.PositiveIntegerField()
    dv = models.CharField(max_length=1)

    def full_rut(self):
        return '{}-{}' . format(self.rut, self.dv)

    def __str__(self):
        return self.name

class Coach(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    nickname = models.CharField(max_length=120)
    team = models.OneToOneField(Team,null=True,on_delete=models.SET_NULL)

    rut = models.PositiveIntegerField()
    dv = models.CharField(max_length=1)

    def __str__(self):
        return self.name

    def full_rut(self):
        return '{}-{}' . format(self.rut, self.dv)

class Match(models.Model):
    date = models.DateTimeField(null=True,default=None)
    name = models.CharField(max_length=100)
    team1 = models.ForeignKey(Team,default=None,related_name="Team1",on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team,default=None,related_name="Team2",on_delete=models.CASCADE)

class TeamCompose(models.Model):
    players = models.ManyToManyField(Player, default=None,)
    author = models.ForeignKey(Coach,null=True,default=None,on_delete=models.SET_NULL)
    match = models.ForeignKey(Match,null=True,default=None,on_delete=models.SET_NULL)


    