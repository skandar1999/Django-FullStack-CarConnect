from django import forms
from .models import Message, RentList

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'phone', 'message']


class RentForm(forms.ModelForm):
    class Meta:
        model = RentList
        fields = ['start_date', 'end_date', 'message', 'email', 'phone']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }