from django import forms
from .models import Room , Category

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'category', 'status']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']