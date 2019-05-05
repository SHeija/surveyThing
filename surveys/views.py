from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
#from django.contrib.auth.models import User

from .forms import SurveyForm, QuestionFormSet
from .models import Survey, Question

def index(request):
    return HttpResponse("Surveys yo")

def add(request):
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

    return render(request, 'surveys/addNew.html', context)