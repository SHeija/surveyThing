from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
#from django.contrib.auth.models import User

from .forms import SurveyForm, QuestionFormSet, QuestionModelFormSet
from .models import Survey, Question

def index(request):
    return HttpResponse("Surveys yo")

def detail(request, survey_id):
    template_name = 'surveys/detail.html'
    survey = get_object_or_404(Survey, pk=survey_id)
    questions = get_list_or_404(Question, survey_id=survey_id)
    context = {
        'survey': survey,
        'questions': questions
    }
    return render(request, template_name, context)

def delete(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    survey.delete()
    return HttpResponseRedirect('/accounts/profile/')

def add(request):
    template_name = 'surveys/addNew.html'
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        sform = SurveyForm(request.POST)
        qforms = QuestionFormSet(request.POST)
        # check whether it's valid:
        if sform.is_valid() and qforms.is_valid():
            # save the survey
            survey = sform.save(commit=False)
            survey.date_created = timezone.now()
            survey.author = request.user
            survey.save()
            
            #saving questions
            for qform in qforms:
                new_q = qform.save(commit=False)
                new_q.survey = survey
                if new_q.question_text: #don't save empty questions
                    new_q.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/accounts/profile/')
    # if a GET (or any other method) we'll create a blank form
    else:
        sform = SurveyForm()
        qforms = QuestionFormSet()

    context = {
        'sform': sform,
        'qforms': qforms,
    }

    return render(request, template_name, context)

def edit_survey(request, survey_id):
    template_name = 'surveys/edit_survey.html'
    if request.method == 'POST':
        sform = SurveyForm(request.POST)
        if sform.is_valid():
            survey = get_object_or_404(Survey, pk=survey_id)
            survey.title = sform.cleaned_data['title']
            survey.description = sform.cleaned_data['description']
            survey.save()
            return HttpResponseRedirect('/accounts/profile/')
    else:
        sform = SurveyForm(instance = get_object_or_404(Survey, pk=survey_id))
    
    context = {
        'sform': sform
    }

    return render(request, template_name, context)

        