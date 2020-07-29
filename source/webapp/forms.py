from django import forms
from django.forms import DateInput

from .models import STATUS_CHOICE

default_status = STATUS_CHOICE[0][0]


class ArticleForm(forms.Form):
    name = forms.CharField(max_length=1000, required=True, label='Название')
    description = forms.CharField(max_length=3000, required=True, label='Описание', widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICE, required=True, initial=default_status, label='Статус')
    create_at = forms.DateField(required=False, label=' Дата выполнения', widget=DateInput)