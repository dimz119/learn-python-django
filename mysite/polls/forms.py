from django import forms

class SurveyForm(forms.Form):
    # https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#built-in-widgets
    user_name = forms.CharField(
        label='Your name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_age = forms.IntegerField(
        label='Your age',
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
