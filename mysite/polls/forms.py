from django import forms

# class SurveyForm(forms.Form):
#     # https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#built-in-widgets
#     user_name = forms.CharField(
#         label='Your name',
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'}))
#     user_age = forms.IntegerField(
#         label='Your age',
#         widget=forms.NumberInput(attrs={'class': 'form-control'}))

from django.forms import ModelForm, TextInput, NumberInput
from polls.models import Survey

class SurveyForm(ModelForm):
    # https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
    class Meta:
        model = Survey
        # fields = ['user_name', 'user_age'] # select the fields
        fields = '__all__' # select the al l the fields
        labels = {
            "user_name": "User Name",
            "user_age": "User Age"
        }
        widgets = {
            'user_name': TextInput(attrs={'class': 'form-control'}),
            'user_age': NumberInput(attrs={'class': 'form-control'}),
        }
