from django import forms
from .models import StudentModel


class StudentForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Name here '
    }))
    age = forms.CharField( max_length=200, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Age '
    }))
    address = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Address '
    }))
    email = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email '
    }))
    pin = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'PIN '
    }))

    mob = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mobile '
    }))
    class Meta():
        model=StudentModel
        fields=['name','age','address','email','pin','mob']

