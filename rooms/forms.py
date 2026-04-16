from django import forms
from .models import Room , Category

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'category', 'status']
        error_messages = {
            'room_number': {
                'required': 'Room number is required.',
                'unique': 'A room with this number already exists.',
            },
            'category': {
                'required': 'Category is required.',
            },
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        error_messages = {
            'name': {
                'required': 'Category name is required.',
                'unique': 'A category with this name already exists.',
            },
        }