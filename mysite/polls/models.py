from django.db import models
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator
)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    owner = models.CharField(
        max_length=200,
        blank=True,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(10)])

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
