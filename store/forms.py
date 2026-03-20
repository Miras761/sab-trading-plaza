from django import forms
from .models import Listing, Comment, DELETE_REASON_CHOICES


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['category', 'title', 'description', 'brainrot',
                  'custom_brainrot_name', 'custom_brainrot_image', 'want_description']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Название объявления...'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4, 'placeholder': 'Опишите подробно...'}),
            'brainrot': forms.Select(attrs={'class': 'form-select'}),
            'custom_brainrot_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Или введите имя вручную...'}),
            'custom_brainrot_image': forms.FileInput(attrs={'class': 'form-file', 'accept': 'image/*'}),
            'want_description': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Что хотите получить взамен?'}),
        }
        labels = {
            'category': 'Категория',
            'title': 'Заголовок',
            'description': 'Описание',
            'brainrot': 'Брейнрот (из списка)',
            'custom_brainrot_name': 'Или свой брейнрот (имя)',
            'custom_brainrot_image': 'Фото брейнрота',
            'want_description': 'Хочу получить',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'is_trade_offer']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'comment-input',
                'rows': 3,
                'placeholder': 'Напишите предложение о трейде или вопрос...',
                'maxlength': 500,
            }),
            'is_trade_offer': forms.CheckboxInput(attrs={'class': 'trade-checkbox'}),
        }
        labels = {
            'text': '',
            'is_trade_offer': '🔄 Это предложение о трейде',
        }


class DeleteListingForm(forms.Form):
    reason = forms.ChoiceField(
        choices=DELETE_REASON_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'reason-radio'}),
        label='Причина удаления',
    )
