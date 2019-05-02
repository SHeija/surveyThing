from django.forms import ModelForm
from .models import Survey, Question
from betterforms.multiform import MultiModelForm
    
class SurveyForm(ModelForm):
   class Meta:
        model = Survey
        fields = ['title', 'description']

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

class SurveyCreationForm(ModelForm):
    form_classes = {
        'survey': SurveyForm,
        'question': QuestionForm,
    }