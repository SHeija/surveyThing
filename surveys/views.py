from django.shortcuts import render
from django.http import HttpResponse
from .models import Survey, Question
from django.utils import timezone

def index(request):
    return HttpResponse("Surveys yo")

def add(request):
    s = Survey(title="Yo dawg", description="Lorem ipsum", date_created=timezone.now())
    s.save()
    q = Question(survey=s, question_text="What's up dog?")
    q.save()
    return HttpResponse("Added new yo")

