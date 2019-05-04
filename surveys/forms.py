from django.forms import ModelForm, TextInput, Form, modelformset_factory, formset_factory
from .models import Survey, Question
from betterforms.multiform import MultiModelForm
    
class SurveyForm(ModelForm):
   class Meta:
        model = Survey
        fields = ['title', 'description']
        labels = {
            'title': 'Title',
            'description': 'Description'
        }
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title here'
                }
            ),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description here'
                }
            )
        }
        

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        labels = {
            'question_text': 'Question',
        }
        widgets={'question_text': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter question here'
        })
    }

QuestionFormSet = formset_factory(QuestionForm, extra=1)

