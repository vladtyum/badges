from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    dream_job = models.CharField(max_length=30, blank=True)
    photo = models.ImageField(upload_to='student-photos', blank=True)
    school = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username


class School(models.Model):
    name = models.CharField(max_length=30, blank=True, unique="True",)
    photo = models.ImageField(upload_to='schools', blank=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=30, blank=True, unique="True",)
    school = models.ForeignKey('School', null="True", on_delete=models.SET_NULL,)
    photo = models.ImageField(upload_to='topics', blank=True)
    
    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=30, blank=True, unique="True",)
    topic = models.ForeignKey('Topic',  null="True", on_delete=models.SET_NULL,)
    photo = models.ImageField(upload_to='skills', blank=True)
    
    def __str__(self):
        return self.name


class Badge(models.Model):
    name = models.CharField(max_length=30, blank=True, unique="True",)
    number = models.IntegerField(blank=True)
    skill = models.ForeignKey('Skill', null="True", on_delete=models.SET_NULL, )
    description = models.CharField(max_length=300, blank=True)
    photo = models.ImageField(upload_to='skills', blank=True)
    
    def __str__(self):
        return self.name

class Evidence(models.Model):
    achievement = models.OneToOneField('Achievement', null="True", on_delete=models.SET_NULL,)
    name = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=300, blank=True)
    date = models   .DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='skills', blank=True)

    def __str__(self):
        return self.name


class Achievement(models.Model):
    student = models.ForeignKey('Student', null="True", on_delete=models.SET_NULL,)
    badge = models.ForeignKey('Badge',  null="True", on_delete=models.SET_NULL,)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.badge.name 