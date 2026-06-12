from django import forms
from .models import ConsultationRequest

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = ConsultationRequest
        fields = ['full_name', 'email', 'phone_number', 'service', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Business Email', 'class': 'form-input'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-input'}),
            'service': forms.Select(attrs={'class': 'form-input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Tell us about your project or specific IT needs...', 'rows': 4, 'class': 'form-input'}),
        }