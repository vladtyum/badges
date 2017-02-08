from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    achievements = Achievement.objects.order_by('-date')
    context_dict = {'achievements' : achievements}
    return render(request, 'badgeapp/index.html', context_dict)


def student(request, id):
    schools = School.objects.filter(topic__skill__badge__achievement__student_id=id)
    topics = Topic.objects.filter(skill__badge__achievement__student_id=id)
    skills = Skill.objects.filter(badge__achievement__student_id=id)
    achievements = Achievement.objects.filter(student=id)
    context_dict = {'schools' : schools, 'topics' : topics, 'skills' : skills, 'achievements' : achievements, }
    return render(request, 'badgeapp/student.html', context_dict)
