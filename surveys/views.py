from django.shortcuts import render
from django.forms import inlineformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import CreateView
#from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect


from .forms import SurveyCreationForm, SurveyForm, QuestionForm
from .models import Survey, Question

def index(request):
    return HttpResponse("Surveys yo")

def add(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        sform = SurveyForm(request.POST)
        qforms = QuestionForm(request.POST)
        # check whether it's valid:
        if sform.is_valid() and qforms.is_valid():
            # process the data in form.cleaned_data as required
            survey = sform.save(commit=False) #Survey(title=sform.cleaned_data['title'], description=sform.cleaned_data['description'], date_created=timezone.now())
            survey.date_created = timezone.now()
            survey.save()
            
            new_q = qforms.save(commit=False)
            new_q.survey = survey
            new_q.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/accounts/profile/')
    # if a GET (or any other method) we'll create a blank form
    else:
        sform = SurveyForm()
        qforms = QuestionForm()

    context = {
        'sform': sform,
        'qforms': qforms,
    }

    return render(request, 'surveys/addNew.html', context)

  
    '''
    class Add(CreateView):
    form_class = SurveyCreationForm
    success_url = '/accounts/profile'

    def form_valid(self, form):
        # Save the user first, because the profile needs a user before it
        # can be saved.
        survey = form['survey'].save(commit=False)
        survey.date_created = timezone.now()
        survey.save()
        question = form['question'].save(commit=False)
        question.survey = survey
        question.save()
        return redirect(self.get_success_url())

    def add(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        sform = SurveyCreationForm(request.POST, instance=Survey())
        qforms = [QuestionCreationForm(request.POST, prefix=str(x), instance=Question()) for x in range(0,3)]
        # check whether it's valid:
        if sform.is_valid() and all([qf.is_valid() for qf in qforms]):
            # process the data in form.cleaned_data as required
            new_s = sform.save() #Survey(title=sform.cleaned_data['title'], description=sform.cleaned_data['description'], date_created=timezone.now())
            new_s.date_created = timezone.now()
            for qf in qforms:
                new_q = qf.save(commit=False)
                new_q.survey = new_s
                new_q.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/accounts/profile/')
    # if a GET (or any other method) we'll create a blank form
    else:
        sform = SurveyCreationForm(instance=Survey)
        qforms = [QuestionCreationForm(request.POST, instance=Question()) for x in range(0,3)]

    context = {
        'sform': sform,
        'qforms': qforms,
    }

    return render(request, 'surveys/addNew.html', context)

    def add_poll(request):
    if request.method == "POST":
        pform = PollForm(request.POST, instance=Poll())
        cforms = [ChoiceForm(request.POST, prefix=str(x), instance=Choice()) for x in range(0,3)]
        if pform.is_valid() and all([cf.is_valid() for cf in cforms]):
            new_poll = pform.save()
            for cf in cforms:
                new_choice = cf.save(commit=False)
                new_choice.poll = new_poll
                new_choice.save()
            return HttpResponseRedirect('/polls/add/')
    else:
        pform = PollForm(instance=Poll())
        cforms = [ChoiceForm(prefix=str(x), instance=Choice()) for x in range(0,3)]
    return render_to_response('add_poll.html', {'poll_form': pform, 'choice_forms': cforms})


    s = Survey(title="Yo dawg", description="Lorem ipsum", date_created=timezone.now())
    s.save()
    q = Question(survey=s, question_text="What's up dog?")
    q.save()
    return HttpResponse("Added new yo")
    '''


