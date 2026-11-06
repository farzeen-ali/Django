from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['user_name', 'user_email', 'message']
        widgets = {
            'user_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your name'}),
            'user_email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'rows': 4, 'placeholder': 'Write your feedback here...'}),
        }