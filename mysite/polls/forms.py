from django import forms

class SurveyForm(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=100)
    user_age = forms.IntegerField(label='Your age')
