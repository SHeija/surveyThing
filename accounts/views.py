from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from surveys.models import Survey


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def bye(request):
    return HttpResponse("Bye!")

def profile(request):
    template_name = 'accounts/profile.html'
    surveys_list = Survey.objects.filter(author_id=request.user.id)
    context = {
        'surveys_list': surveys_list,
    }

    return render(request, template_name, context)
