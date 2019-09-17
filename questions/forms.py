from django import forms
from .models import TestIdentifier


class CandidateForm(forms.Form):
    username = forms.CharField(max_length=60)
    email = forms.EmailField()
    tests = forms.ModelChoiceField(queryset=TestIdentifier.objects.all(),empty_label="select a test")


class RetakeForm(forms.Form):
    test = forms.ModelChoiceField(queryset=TestIdentifier.objects.all(),empty_label="select a test")
