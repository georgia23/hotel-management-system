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


    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 3:
            raise forms.ValidationError("First name must be more than 2 characters.")
        if not first_name.isalpha():
            raise forms.ValidationError("First name must contain only letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) < 3:
            raise forms.ValidationError("Last name must be more than 2 characters.")
        if not last_name.isalpha():
            raise forms.ValidationError("Last name must contain only letters.")
        return last_name