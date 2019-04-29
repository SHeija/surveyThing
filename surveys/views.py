from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .forms import SurveyCreationForm
from .models import Survey, Question

def index(request):
    return HttpResponse("Surveys yo")

def add(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SurveyCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            s = Survey(title=form.cleaned_data['title'], description=form.cleaned_data['description'], date_created=timezone.now())
            s.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/accounts/profile/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SurveyCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'surveys/addNew.html', context)
  
    '''
    s = Survey(title="Yo dawg", description="Lorem ipsum", date_created=timezone.now())
    s.save()
    q = Question(survey=s, question_text="What's up dog?")
    q.save()
    return HttpResponse("Added new yo")
    '''


