from django import forms
from .models import Payment 

class PaymentForm(forms.ModelForm):
    payment_date = forms.DateTimeField(
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
        model = Payment
        fields = ['guest', 'amount', 'payment_type', 'payment_date']
        error_messages = {
            'guest': {
                'required': "Please select a guest."
            },
            'amount': {
                'required': "Please enter the payment amount."
            },
            'payment_type': {
                'required': "Please select a payment type."
            },
            'payment_date': {
                'required': "Please enter the payment date."
            }
        }