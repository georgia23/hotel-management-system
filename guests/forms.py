from django import forms
from .models import Guest

class GuestForm(forms.ModelForm):
    date_registered = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'required': True
            }
        )
    )

    class Meta:
        model = Guest
        fields = '__all__'
        error_messages = {
            'first_name': {
                'required': 'First name is required.',
            },
            'last_name': {
                'required': 'Last name is required.',
            },
            'contact': {
                'required': 'Contact number is required.',
            },
            'email': {
                'required': 'Email is required.',
                'unique': 'A guest with this email already exists.',
            },
            'date_registered': {
                'required': 'Date registered is required.',
            },
        }