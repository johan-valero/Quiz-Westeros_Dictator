from distutils.command.upload import upload
from email.policy import default
from msilib.schema import Class
from random import choices
from django.db import models
from django.forms import CheckboxInput, NumberInput


# Create your models here.

class Regime(models.Model):
    regime_name = models.CharField(max_length=50)
    regime_description = models.CharField(max_length=200)

    def __str__(self):
        return self.regime_name

class Election(models.Model):
    election_name = models.CharField(max_length=50)
    election_date = models.DateTimeField("Date des élections")
    election_nbr_tour = models.IntegerField(NumberInput)

    def __str__(self):
        return self.election_name 


class Dictateur(models.Model):
    dictateur_name = models.CharField(max_length=50)
    dictateur_maison = models.CharField(max_length=50)
    dictateur_blason = models.ImageField(upload_to='blason', blank=True)
    dictateur_avatar = models.ImageField(upload_to='avatar', blank=True)
    dictateur_regime = models.ForeignKey(Regime, on_delete=models.CASCADE)
    dictateur_election = models.ManyToManyField(Election,blank=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.dictateur_name + ' ' + self.dictateur_maison


# class Paysan(models.Model):
#     paysan_name = models.CharField(max_length=50)
#     choix_role = (
#         (1, "Electeur"),
#         (2, "Admin"),
#     )
#     paysan_role = models.IntegerField(choices=choix_role)
#     paysan_election = models.ManyToManyField(Election)

    # def __str__(self):
    #     return self.paysan_name



