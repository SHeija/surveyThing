from django.forms import ModelForm
from .models import Survey, Question

class SurveyCreationForm(ModelForm):
    class Meta:
        model = Survey
        fields = ['title', 'description']