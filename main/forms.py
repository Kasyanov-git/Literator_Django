from .models import Feedback
from django.forms import ModelForm, TextInput, Textarea, EmailInput

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'anons', 'full_text', 'email']

    widgets = {
        "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Как к тебе обращаться?',
        }),
        "anons": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Тема послания...',
        }),

        "full_text": Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Отзывы, предложения о сотрудничестве и конструктивную критику приветствуем!',
        }),

        "email": EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Если ждёшь ответ, оставляй почту:',
        })
        }